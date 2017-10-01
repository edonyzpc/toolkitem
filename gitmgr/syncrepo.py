#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
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
 # Last modified: 2017-02-28 23:38
 #
 # Filename: syncrepo.py
 #
 # Description: All Rights Are Reserved
 # This tool aim to keep forked github repository update with upstream repository
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
import os
import sys
try:
    from subprocess import getstatusoutput
except ImportError:
    from commands import getstatusoutput

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


color = PyColor()
color.new = '\033[0;36m'

class SyncUpstreamRepo(objec):
    def __init__(self, path, upstream):
        self.repo_path = path
        self.upstream_url = upstream_url
        self.remotelist = None

    def is_git_repo(self):
        """check if path is a git repository"""
        gitstatus = 'git status'
        status, _ = getstatusoutput(gitstatus)
        if status == 0:
            self.isgit = True
        else:
            self.isgit = False

    def _remote_list(self):
        if self.is_git_repo(self):
            return
        gitremote = 'git remote -v'
        status, remotelist = getstatusoutput(gitremote)
        if status == 0:
            self.remotelist = remotelist.split('\n')

    def has_upstream(self):
        if self.remotelist is not None:
            for item in self.remotelist:
                if self.upsream_url in item:
                    return True
        else:
            return False

    def add_upstrem(self):
        if not has_upsream:
            gitremoteadd = 'git remote add upstream ' + self.upstream_url
            status, _ = getstatusoutput(gitremoteadd)

    def sync_upstream(self, branch='master'):
        gitfetch = 'git fetch upstream'
        gitcheckout = 'git checkout ' + branch
        gitmerge = 'git merge upsream/' + branch
        gitpush = 'git push origin ' + branch

def print_cmd_result(cmd, status, output):
    if status != 0:
        raise Exception(color.warningcolor + cmd + \
                        ' executed in {} failed\n'.format(os.getcwd()))
    print(color.tipcolor + output + color.endcolor)


def exec_cmd(cmd):
    (status, output) = getstatusoutput(cmd)
    print_cmd_result(cmd, status, output)
    return (status, output)


def has_local_upstream():
    cmd = 'git remote -v'
    status, output = getstatusoutput(cmd)
    if status != 0:
        return False
    else:
        if 'upstream' not in output.split():
            return False
        else:
            return True


def add_upstream(upstream_url):
    cmd = 'git remote add upstream ' + upstream_url
    exec_cmd(cmd)


def sync_up2master():
    cmd_fetch = 'git fetch upstream'
    cmd_merge = 'git checkout master\ngit merge upstream/master --no-ff'
    cmd_push = 'git push origin master'
    fetch_stat, fetch_output = getstatusoutput(cmd_fetch)
    if len(fetch_output) <= 0:
        print(color.new + 'Repo already update!' + color.endcolor)
        return
    merge_stat, merge_output = exec_cmd(cmd_merge)
    push_stat, push_output = exec_cmd(cmd_push)
    return [(fetch_stat, fetch_output), (merge_stat, merge_output), (push_stat, push_output)]


if __name__ == "__main__":
    if not has_local_upstream():
        if len(sys.argv) > 1:
            add_upstream(sys.argv[1])
        else:
            raise Exception(color.warningcolor +\
                            'upstream url needed' + color.endcolor)
    sync_up2master()
