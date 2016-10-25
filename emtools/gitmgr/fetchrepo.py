#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2016-10-19 21:18
 #
 # Filename: fetchrepo.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = """
        STYLE: \033['display model';'foreground';'background'm
        DETAILS:
        FOREGROUND        BACKGOUND       COLOR
        ---------------------------------------
        30                40              black
        31                41              red
        32                42              green
        33                43              yellow
        34                44              blue
        35                45              purple
        36                46              cyan
        37                47              white
        DISPLAY MODEL    DETAILS
        -------------------------
        0                default
        1                highlight
        4                underline
        5                flicker
        7                reverse
        8                non-visiable
        e.g:
        \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
        \033[0m         <!--set all into default-->
        """
        self.warningcolor = '\033[0;31m'
        self.tipcolor = '\033[0;32m'
        self.endcolor = '\033[0m'
        self._newcolor = ''
    @property
    def new(self):
        """
        Customized Python Print Color.
        """
        return self._newcolor
    @new.setter
    def new(self, color_str):
        """
        New Color.
        """
        self._newcolor = color_str
    def disable(self):
        """
        Disable Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''

from urllib.request import urlopen
import subprocess as sp
import os

def get_repo_url(repo_path):
    cmd = 'cd ' + repo_path + ';git remote -v'
    (status, output) = sp.getstatusoutput(cmd)
    tmp = [item for item in output.split() if item.find('git@github.com:edonyM') > -1]
    if len(set(tmp)) > 1:
        print('You have more than one repository URL address')
        return None
    else:
        url_addr = 'https://github.com/' + tmp[0].split(':')[1]
        if status > -1:
            return url_addr
        else:
            print('Wrong repository directory!')
            return None


def get_forkedrepo_url(url_addr):
    buf = urlopen(url_addr).readlines()
    for line in buf:
        if line.decode('utf-8').find('forked from') > -1:
            web_buf = line.decode('utf-8')
            break
        else:
            web_buf = None
    if web_buf is None:
        return None
    else:
        return 'https://github.com' + web_buf.split('"')[3]


def gen_fetch_cmds(repo_path):
    #cur_dir = os.getcwd()
    os.chdir(repo_path)
    url = get_repo_url(repo_path)
    fork_url = get_forkedrepo_url(url)
    remote_branch_cmd = 'git remote -v'
    status, output = sp.getstatusoutput(remote_branch_cmd)
    if status > -1:
        ls_remote = output.split()
        if fork_url in ls_remote:
            inx = ls_remote.index(fork_url)
        else:
            inx = None

        if inx > 0:
            fetch_cmd = 'git fetch ' + ls_remote[inx - 1]
            add_remote_cmd = None
        else:
            add_remote_cmd = 'git remote add ' + fork_url.split('/')[-1]\
                             + ' ' + fork_url
            fetch_cmd = 'git fetch ' + fork_url.split('/')[-1]

        merge_cmd = 'git merge ' + fork_url.split('/')[-1] + '/master'
        push_cmd = 'git push origin master'

        if add_remote_cmd is not None:
            cmds = [add_remote_cmd, fetch_cmd, merge_cmd, push_cmd]
        else:
            cmds = [fetch_cmd, merge_cmd, push_cmd]

        #os.chdir(cur_dir)
        return cmds
    else:
        #os.chdir(cur_dir)
        return None

def gen_sh(cmds):
    _, sh_dir = sp.getstatusoutput("which sh")
    sh_template = "#!" + sh_dir + "\n\nif [ ! -x update_fork.sh ]; then\n"\
                  + "touch update_fork.sh\nchmod 777 update_fork.sh\n"\
                  + "./update_fork.sh\nexit 0\nfi\n"
    judge_cmd = "if [ $? -eq 0 ]; then\n"
    exit_code = -1
    file_buf = sh_template

    for cmd in cmds:
        new_lines = "\n" + cmd + "\n" + judge_cmd + "echo \"" + cmd\
                    + " done\"\nelse\nexit " + str(exit_code) + "\nfi\n"
        file_buf += new_lines
        exit_code -= 1

    with open("update_fork.sh", "w") as sh_file:
        sh_file.write(file_buf)

def update_fork_branch(repo_paht):
    pass

if __name__ == "__main__":
    #furl = repo_web(get_repo_url('~/coding/script-utility'))
    #print(furl)
    #furl1 = repo_web(get_repo_url('./'))
    #print(furl1)
    cmds = gen_fetch_cmds('/Users/edony/coding/script-utility')
    gen_sh(cmds)
