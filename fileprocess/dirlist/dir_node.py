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
 # Last modified: 2016-10-15 21:20
 #
 # Filename: dir_node.py
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

def dfs_myDir(path, printDir = None, printFile = None):
    stack = []
    ret = []
    stack.append(path)
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if(os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                stack.append(os.path.join(tmp, item))
            if printDir:
                printDir(tmp)
        elif(os.path.isfile(tmp)):
            ret.append(tmp)
            if printFile:
                printFile(tmp)
    return ret

def printDir(path):
    print "dir: " + path

def printFile(path):
    print "file: " + path



class dir_node(object):
    """
    Encapsulate the attributes of directory recursively into this class.
    Type: directory, file, link
    Path: full path of directory node
    """
    def __init__(self, root_path):
        self.root_path = root_path
        self.dir = []
        self.file = []
        self.link = []

    def _list_member(self):
        """
        Get the entries in `root_path`
        """
        pass

    def _gen_attr(self):
        pass

    def _list_dir(self):
        pass

    def _list_file(self):
        pass

    def _list_link(self):
        pass

    def _parent_dir(self):
        pass

    def _sub_dir(self):
        pass

    def _dfs(self, printDir = None, printFile = None):
        stack = []
        ret = []
        stack.append(path)
        while len(stack) > 0:
            tmp = stack.pop(len(stack) - 1)
            if(os.path.isdir(tmp)):
                ret.append(tmp)
                for item in os.listdir(tmp):
                    stack.append(os.path.join(tmp, item))
                if printDir:
                    printDir(tmp)
            elif(os.path.isfile(tmp)):
                ret.append(tmp)
                if printFile:
                    printFile(tmp)
        return ret
