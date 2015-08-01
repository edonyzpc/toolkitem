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
    tasks = list(set(directions.total_dirs))
    tasks.append(path)
    return tasks

def find_file(direction,files):
    print direction
    dir_list = os.listdir(direction)
    os.chdir(direction)
    file_list = [file for file in dir_list if os.path.isfile(file)]
    files[direction] = file_list
    print files

# create direction to find files tasks into queue
def task(directions):
    global queue,lock
    while directions:
        lock.acquire()
        queue.put(directions[0])
        directions.remove(directions[0])
        lock.release()

# pick direction from queue and generate the files in it
def solver(direction, num, files):
    while True and num >0:
        global lock,queue,condition,queue1
        if not queue.empty():
            lock.acquire()
            direction = queue.get()
            num -= 1
            #print "dir",direction
            find_file(direction,files)
            #queue1.put([direction+"/"+file for file in file_list])
            lock.release()

# manager
def parallelengine(path):
    global queue,lock,lock1,files
    files = {}
    directions = init(path)
    num = len(directions)/3
    task_process = [multiprocessing.Process(target=task,args=(directions[i*num:(i+1)*num],)) for i in range(3)]
    for tp in task_process:
        tp.start()
    for tp in task_process:
        tp.join()
    solver_process = [multiprocessing.Process(target=solver, args=(dir,num*3,files,))]
    for sp in solver_process:
        sp.start()
    for sp in solver_process:
        sp.join()

if __name__ == "__main__":
    path = "/home/edony/code/github/toolkitem/filesline"
    #ddd = {}
    #find_file(path, ddd)
    #print ddd
    global queue,lock,condition,files
    queue = multiprocessing.Queue()
    queue1 = multiprocessing.Queue()
    lock = multiprocessing.Lock()
    condition = multiprocessing.Condition()
#    result = {}
    parallelengine(path)
    print files.keys()
    print "main",id(files)
