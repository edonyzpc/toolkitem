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

class SyncUpstreamRepo(object):
    """Sync source code from upstream in forked repository
       e.g. Github Project
    """
    def __init__(self, path, upstream_url):
        self.repo_path = os.path.realpath(path)
        self.upstream_url = upstream_url
        self.remotelist = None
        self.isgit = None

    def _is_crt_dir(self):
        if os.path.realpath(os.path.curdir) == self.repo_path:
            return True
        return False

    def is_git_repo(self):
        """check if path is a git repository"""
        if not self._is_crt_dir():
            print("Not a correct repository path")
            return False
        gitstatus = 'git status'
        status, logs = getstatusoutput(gitstatus)
        print(status)
        print(logs)
        if status == 0:
            return True
        else:
            return False

    def _remote_list(self):
        if not self._is_crt_dir():
            return
        if self.is_git_repo():
            return
        gitremote = 'git remote -v'
        status, remotelist = getstatusoutput(gitremote)
        if status == 0:
            self.remotelist = remotelist.split('\n')

    def has_upstream(self):
        if not self._is_crt_dir():
            return False

        if self.remotelist is not None:
            for item in self.remotelist:
                if self.upstream_url in item:
                    return True
        else:
            return False

    def add_upstrem(self):
        if not self._is_crt_dir():
            return False

        if not self.has_upstream():
            gitremoteadd = 'git remote add upstream ' + self.upstream_url
            status, _ = getstatusoutput(gitremoteadd)

    def sync_upstream(self, branch='master'):
        if not self._is_crt_dir():
            print("changing the current directory into {}".format(self.repo_path))
            os.chdir(self.repo_path)

        if not self.is_git_repo():
            print(os.getcwd())
            print("ERROR: Not a git repository")
            return

        if not self.has_upstream():
            print("add upstream {} into repository".format(self.upstream_url))
            self.add_upstrem()

        gitfetch = 'git fetch upstream'
        gitcheckout = 'git checkout ' + branch
        gitmerge = 'git merge upstream/' + branch
        gitpush = 'git push origin ' + branch
        exec_cmds = [gitfetch, gitcheckout, gitmerge, gitpush]
        for cmd in exec_cmds:
            status, logs = getstatusoutput(cmd)
            print("[" + cmd + "]" + logs)
            if status != 0:
                print("ERROR: " + cmd)
                print(logs)
                break

def syncrepo(path, upstream, branch='master'):
    syncer = SyncUpstreamRepo(path, upstream)
    syncer.sync_upstream(branch)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please specific the path and upstream URL")
    else:
        print(sys.argv)
        syncrepo(sys.argv[1], sys.argv[2])
