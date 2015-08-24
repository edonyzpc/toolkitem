#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2015-07-28 17:11
 #
 # Filename: browser.py
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
import threading
import multiprocessing

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = r"""
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


def find_subdir(path):
    all_subdir = []
    for item in os.listdir(path):
        if os.path.isdir(item) and not os.path.islink(item):
            all_subdir.append(path + '/' + item)
    return all_subdir
def all_dir(path, total_dirs):
    os.chdir(path)
    tmp_dir = find_subdir(path)
    total_dirs.append(path)
    if len(tmp_dir) == 0:
        return
    else:
        for item in tmp_dir:
            total_dirs.append(item)
            all_dir(item, total_dirs)

def find_subdir_p(path):
    all_subdir = []
    for item in os.listdir(path):
        if os.path.isdir(item) and not os.path.islink(item):
            all_subdir.append(path + '/' + item)
    return all_subdir
def all_dir_p(path, total_dirs):
    os.chdir(path)
    tmp_dir = find_subdir_p(path)
    total_dirs.append(path)
    if len(tmp_dir) == 0:
        return
    else:
        for item in tmp_dir:
            total_dirs.append(item)
            all_dir_p(item, total_dirs)
def all_dir_p_(path):
    dirs = []
    all_dir_p(path, dirs)
    return dirs

def _find_subdir(path):
    all_subdir = []
    for item in os.listdir(path):
        if os.path.isdir(item) and not os.path.islink(item):
            all_subdir.append(path + '/' + item)
    return all_subdir
def _all_dir(path, total_dirs):
    os.chdir(path)
    tmp_dir = _find_subdir(path)
    total_dirs.append(path)
    if len(tmp_dir) == 0:
        return
    else:
        for item in tmp_dir:
            total_dirs.append(item)
            _all_dir(item, total_dirs)
if __name__ == "__main__":
    import time
    import platform 
    global lock
    total = [] 
    totalp = multiprocessing.Queue() 
    l = multiprocessing.Lock()
    lock = threading.Lock()
    lock.acquire()
    if platform.system == "Linux":
        path = "/usr"
    else:
        path = "/usr/local/Cellar/opencv"
    paths = []
    for i in os.listdir(path):
        os.chdir(path)
        if os.path.isdir(i):
            paths.append(path+"/"+i)
    ALL = []
    os.chdir(path)
    start = time.time()
    _all_dir(path, ALL)
    end1 = time.time()
    for i in paths:
        os.chdir(i)
        t=threading.Thread(target=all_dir, args=(i,total))
        t.setDaemon(True)
        t.start()
        t.join()
    end2 = time.time()
    p = multiprocessing.Pool(len(paths))
    tmp = p.map(all_dir_p_, paths)
    #for i in paths:
    #    os.chdir(i)
    #    t=multiprocessing.Process(target=all_dir_p_, args=(i,totalp,l))
    #    t.start()
    #    t.join()
    #a = []
    #for m in totalp:
    #    a.extend(m.get())
    end3 = time.time()
    print end1-start
    print end2-end1
    print end3-end2
    print len(set(ALL))
    print len(set(total))
    a = []
    for i in tmp:
        a.extend(i)
    print len(set(a))
