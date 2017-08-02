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
 # Last modified: 2017-08-02 20:57
 #
 # Filename: dirlist.py
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
import os

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


class DirList(object):
    """ list the directory recursively and
        get all directories including all sub-directories
    """

    def __init__(self, rootpath):
        """ initialize `DirList' with root `rootpath'
        """
        self.root = rootpath
        self.dirlist = {}
        # buffer for multiprocess speedup directory walking
        self._dl_buf = []
        self._listdir()

    def _listdir(self, path=None):
        """ list root path recursively including sub-directories
        """
        if path is not None:
            for root_, dir_, file_ in os.walk(path):
                dir_ctx = []
                dir_ctx.insert(0, file_)
                dir_ctx.insert(0, dir_)
                buf_dl = {}
                buf_dl[root_] = dir_ctx
                self._dl_buf.insert(0, buf_dl)
        else:
            for root_, dir_, file_ in os.walk(self.root):
                dir_ctx = []
                dir_ctx.insert(0, file_)
                dir_ctx.insert(0, dir_)
                self.dirlist[root_] = dir_ctx

    @staticmethod
    def getattr(path):
        """ fetch the `path' attribute
        """
        types = ['DIR', 'FILE', 'LINK', 'OTHERS']
        if os.path.isdir(path):
            return types[0]
        elif os.path.isfile(path):
            return types[1]
        elif os.path.islink(path):
            return types[2]
        return types[3]


if __name__ == "__main__":
    OBJ = DirList("/Users/edony/coding/toolkitem")
    print(OBJ.dirlist)
