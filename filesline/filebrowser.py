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
 # Last modified: 2015-07-31 20:56
 #
 # Filename: filebrowser.py
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
import multiprocessing
from time import sleep
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

def init(path):
    directions = DirBrowser(path)
    directions.parallelprocess()
    tasks = set(directions.total_dirs)
    return tasks

def task(path):
    global queue,lock
    lock.acquire()
    init_tasks = init(path)
    for direction in init_tasks:
        queue.put(direction)
    lock.release()

def find_file(direction):
    dir_list = os.listdir(direction)
    file_list = [file for file in dir_list if os.path.isfile(file)]
    return file_list

def solver(files):
    global queue,lock1,result,queue1
    lock1.acquire()
    while True:
        if not queue.empty():
            direction = queue.get()
            file_list = find_file(direction)
            files.append(file_list)
            result[direction] = file_list[:]
            queue1.put([direction+"/"+file for file in file_list])
        else:
            break
    print "NOT"
    lock1.release()

def parallelengine(path, files):
    global queue,lock,lock1
    task_process = [multiprocessing.Process(target=task,args=(path,)) for i in range(1)]
    for tp in task_process:
        tp.start()
    for tp in task_process:
        tp.join()
    solver_process = [multiprocessing.Process(target=solver,args=(files,)) for i in range(3)]
    for sp in solver_process:
        sp.start()
    for sp in solver_process:
        sp.join()

if __name__ == "__main__":
    path = "/home/edony/code/github/toolkitem"
    files = []
    global queue,lock,lock1,result
    queue = multiprocessing.Queue()
    queue1 = multiprocessing.Queue()
    lock = multiprocessing.Lock()
    lock1 = multiprocessing.Lock()
    result = {}
    parallelengine(path, files)
    print queue1.qsize()
    print queue1.get()
    print files
