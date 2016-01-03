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
 # Last modified: 2015-07-29 14:41
 #
 # Filename: dirbrowser.py
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

class DirBrowser(object):
    """
    Class DirBrowser aims to list the all the directories of the given directory.
    And, to speed up, try the MAP/REDUCE method by using subprocess pool.
    """
    def __init__(self, path, speedup=None):
        """Args:
        path: to listed directory(the given path)
        speedup: flag to make sure to use fast method list the directory
        """
        self.path = path
        os.chdir(path)
        self.path_sub = [path+"/"+i for i in os.listdir(path) if os.path.isdir(i)]
        self.path_sub.append(path)
        self.total_dirs = []
        self.speedup = speedup

    @staticmethod
    def find_subdir(path):
        """Browser All Sub-Directory In Current Path
        Args:
            path: the root of the listed directory

        A static method intended to work as interface for external purpose
        """
        all_subdir = []
        for item in os.listdir(path):
            if os.path.isdir(item):
                all_subdir.append(path + '/' + item)
        return all_subdir

    @staticmethod
    def all_dir(path, total_dirs):
        """Browser All Sub-Directory Recursivly In Current Path
        Args:
            path: the root of the listed directory
            total_dirs: record all the directories

        A static method intended to work as interface for external purpose
        """
        os.chdir(path)
        tmp_dir = DirBrowser.find_subdir(path)
        total_dirs.append(path)
        if tmp_dir:
            for item in tmp_dir:
                total_dirs.append(item)
                DirBrowser.all_dir(item, total_dirs)
        else:
            return

    def browser(self):
        """Walk The Path and Get The directories"""
        self.all_dir(self.path, self.total_dirs)

    @staticmethod
    def speedup_browser(path, queue, lock):
        """List The Directories With One Process
        Multi-Process speedup with queue for data share.
        """
        lock.acquire()
        dir_process = []
        DirBrowser.all_dir(path, dir_process)
        queue.put(dir_process)
        lock.release()

    def parallelprocess(self):
        """List All Directories With Multi-Process
        """
        queue = multiprocessing.Queue()
        lock = multiprocessing.Lock()
        processes = [multiprocessing.Process(target=DirBrowser.speedup_browser, args=(path,queue,lock,))
                     for path in self.path_sub]
        for p in processes:
            p.start()
        results = [queue.get() for p in processes]
        [self.total_dirs.extend(item) for item in results]

    @staticmethod
    def pool_browser(path):
        """Same Function With DirBrowser.browser(path)
        """
        dir_process = []
        DirBrowser.all_dir(path, dir_process)
        return dir_process

    def poolprocess(self):
        """
        Map/Reduce mtheod to speedup the listing
        """
        pool = multiprocessing.Pool(len(self.path_sub))
        total = pool.map_async(DirBrowser.pool_browser, self.path_sub)
        self.total_dirs = []
        [self.total_dirs.extend(item) for item in results]

    @property
    def directions(self):
        """
        Private the listed results
        """
        return list(set(self.total_dirs))

def find_files(direction):
    """
    List files in the given directon.
    """
    dir_list = os.listdir(direction)
    os.chdir(direction)
    file_list = [file for file in dir_list if os.path.isfile(file)]
    return file_list

def find_files_directions(directions, queue, lock):
    """
    Find the files with one process.
    """
    files = {}
    for dir in directions:
        f_tmp = find_files(dir)
        files[dir] = f_tmp
    lock.acquire()
    queue.put(files)
    lock.release()

def filebrowser(path,files):
    """
    List All Files With Multi-Process
    """
    db = DirBrowser(path)
    db.parallelprocess()
    length = len(db.directions)
    queue = multiprocessing.Queue()
    lock = multiprocessing.Lock()
    processes = [multiprocessing.Process(target=find_files_directions,
                 args=(db.directions[i:j],queue,lock,))
                 for i,j in [(0,length/3),(length/3,2*length/3),(2*length/3,None)]]
    for p in processes:
        p.start()
    results = [queue.get() for p in processes]
    for item in results:
        files.update(item)

def filebrowser_(path,files):
    """
    List All Files With Builtin Speedup Way.
    """
    db = DirBrowser(path)
    db.parallelprocess()
    for dir in db.directions:
        files[dir] = find_files(dir)

if __name__ == "__main__":
    import time
    path = "/home/edony/code/github/toolkitem"
    files = {}
    s1 = time.time()
    filebrowser(path, files)
    s2 = time.time()
    filebrowser_(path, files)
    s3 = time.time()
    print s2-s1
    print s3-s1
    print len(files.keys())
    #import platform
    #if platform.system == "Linux":
    #    path = "/usr"
    #else:
    #    path = "/usr/local/Cellar/opencv"
    #db = DirBrowser(path)
    #paths = db.path_sub
    #speedup = True
    #queue = multiprocessing.Queue()
    #lock = multiprocessing.Lock()
    #start2 = time.time()
    #processes = [multiprocessing.Process(target=DirBrowser.speedup_browser, args=(path,queue,lock,))
    #             for path in paths]
    #end2 = time.time()
    #for p in processes:
    #    p.start()
    #results = [queue.get() for p in processes]
    #b = []
    #[b.extend(item) for item in results]
    #print len(set(b))
    #print end2-start2
    #db1 = DirBrowser(path)
    #start3 = time.time()
    #db1.parallelprocess()
    #end3 = time.time()
    #print len(set(db1.total_dirs))
    #print end3-start3
    #db2 = DirBrowser(path)
    #start4 = time.time()
    #db2.poolprocess()
    #end4 = time.time()
    #print len(set(db2.total_dirs))
    #print end4-start4
