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

import os
import sys
import subprocess as sp

def print_cmd_result(cmd, status, output):
    color = PyColor()
    if status != 0:
        raise Exception(color.warningcolor + cmd_fetch + ' executed in {} failed\n'.formate(os.getcwd()))
    print(color.tipcolor)
    for item in output.split():
        print(item)
    print(color.endcolor)

def has_local_upstream():
    cmd = 'git remote -v'
    (status, output) = sp.getstatusoutput(cmd)
    #if status != 0:
    #    raise Exception("`git remote -v` executed in {} failed\n".format(os.getcwd()))
    print_cmd_result(cmd, status, output)
    if 'upstream' not in output.split():
        return False
    else:
        return True

def add_upstream(upstream_url):
    cmd = 'git add upstream ' + upstream_url
    (status, output) = sp.getstatusoutput(cmd)
    print_cmd_result(cmd, status, output)
    #if status != 0:
    #    raise Exception(cmd + ' executed in {} failed\n'.formate(os.getcwd()))
    #for item in output.split():
    #    print(item)

def sync_up2master():
    cmd_fetch = 'git fetch upstream'
    cmd_merge = 'git checkout master\ngit merge upstream/master --no-ff'
    cmd_push = 'git push origin master'
    (status_fetch, output_fetch) = sp.getstatusoutput(cmd_fetch)
    print_cmd_result(cmd_fetch, status_fetch, output_fetch)
    (status_merge, output_merge) = sp.getstatusoutput(cmd_merge)
    print_cmd_result(cmd_merge, status_merge, output_merge)
    (status_push, output_push) = sp.getstatusoutput(cmd_push)
    print_cmd_result(cmd_push, status_push, output_push)


if __name__ == "__main__":
    if len(sys.argv) > 1 and has_local_upstream():
        add_upstream(sys.argv[1])
    sync_up2master()


