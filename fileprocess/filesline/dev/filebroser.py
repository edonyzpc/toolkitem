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
 # Last modified: 2015-07-31 13:54
 #
 # Filename: filebroser.py
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
import multiprocessing
import os
from dirbrowser import DirBrowser

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

class FindFile(object):
    def __init__(self, direction):
        self.direction = direction
        os.chdir(self.direction)
        self.files = {}

    def find_file(self):
        dir_list = os.listdir(self.direction)
        file_list = [file for file in dir_list if os.path.isfile(file)]
        self.files[self.direction] = file_list

class DirProduce(multiprocessing.Process):
    def __init__(self, direction):
        multiprocessing.Process.__init__(self)
        self.direction = direction#dirbrowser.total_dirs

    def run(self):
        global queue,lock
        queue.put(self.direction)
            #lock.notify()

class DirConsume(multiprocessing.Process):
    def __init__(self, files):
        multiprocessing.Process.__init__(self)
        self.files = files

    def run(self):
        global queue,lock
        direction = queue.get()
        tmp = FindFile(direction)
        tmp.find_file()
        self.files[direction] = tmp.files[direction]
        print self.files[direction]
            #lock.notify()

def process(direction, files):
    global queue,lock
    queue = multiprocessing.Queue(50)
    lock = multiprocessing.Condition()
    produce = DirProduce(direction)
    consume = DirConsume(files)
    produce.start()
    consume.start()

if __name__ == "__main__":
    #path = "/home/edony/code/github/toolkitem/filesline"
    path = "/home/edony/code/github/toolkitem"
    dirbrowser = DirBrowser(path, speedup=True)
    dirbrowser.parallelprocess()
    print len(dirbrowser.total_dirs)
    print len(set(dirbrowser.total_dirs))
    #tmp = FileBrowser(path)
    #tmp.process()
    #global queue, lock
    #queue = multiprocessing.Queue()
    #lock = multiprocessing.Condition()
    file = {}
    file1 = {}
    for direction in set(dirbrowser.total_dirs):
        tmp = FindFile(direction)
        tmp.find_file()
        file1[direction] = tmp.files[direction]
    global queue,lock
    queue = multiprocessing.Queue(50)
    lock = multiprocessing.Condition()
    for direction in dirbrowser.total_dirs:
        produce = DirProduce(direction)
    produce.start()
    while not queue.empty():
        consume = DirConsume(file)
        consume.start()
    print file
