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
 # Last modified: 2015-06-05 15:48
 #
 # Filename: getdirections.py
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
import sys
if sys.version.startswith("3."):
    from functools import reduce
import os
#import platform

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
        self.warningcolor = '\033[0;37;41m'
        self.tipcolor = '\033[0;31;42m'
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

class GetDirections(object):
    """
    Class GetDirections:
        Get all the contents in the given path recursively and record the contents
        into directions and files.
    """
    def __init__(self, path):
        """
        path: given path
        directions: all directions in path (include sub-directions)
        files: all files in the paht (include the files in sub-directions)
        """
        self.path = path
        self.directions = []
        self.files = {}
        self.color = PyColor()

    @staticmethod
    def normal_path(path):
        """
        Normalize the path string split with "/"
        """
        def add(head, tail):
            """
            Replace \\ with / in path
            """
            if tail == "\\":
                tail = "/"
            return head + tail
        return reduce(add, path)

    @staticmethod
    def _find_subdir(path):
        """
        A protected method for list all the sub-directions in the path.
        """
        path = GetDirections.normal_path(path)
        all_subdir = []
        for item in os.listdir(path):
            if os.path.isdir(item):
                all_subdir.append(path + '/' + item)
        return all_subdir

    @staticmethod
    def _all_dir(path, total_dirs):
        """
        A protected method for list all the directions in path and record them.
        """
        path = GetDirections.normal_path(path)
        os.chdir(path)
        tmp_dir = GetDirections._find_subdir(path)
        total_dirs.append(path)
        if len(tmp_dir) == 0:
            return
        else:
            for item in tmp_dir:
                total_dirs.append(item)
                GetDirections._all_dir(item, total_dirs)

    def structed_dir(self):
        """
        Structure the all directions found with their names.
        """
        if self.directions:
            self.directions = sorted([direction for direction in self.directions])
        else:
            raise ValueError("Directions is empty!")

    def get_dir(self):
        """
        Main to get all the structured directions.
        """
        self._all_dir(self.path, self.directions)
        self.structed_dir()

    def all_files(self):
        """
        Get all the files in the directions.
        """
        if self.directions:
            for direction in self.directions:
                os.chdir(direction)
                list_dir = os.listdir(direction)
                self.files[direction] = \
                        [file_name for file_name in list_dir if os.path.isfile(file_name)]

    def file_tree(self):
        """
        Get visualization of the path structure.
        """
        self.get_dir()
        self.all_files()
        if self.files:
            print(self.color.tipcolor, self.path, self.color.endcolor, '\n')
            for key in self.files.keys():
                print(self.color.warningcolor, "|-- .%s\\"%key.split(self.path)[1],\
                        self.color.endcolor)
                for file_name in self.files[key]:
                    print(" |    %s"%file_name)
                print(" |")

if __name__ == '__main__':
    TEST = GetDirections('/home/edony/code/github/pyexer')
#    TEST.get_dir()
#    TEST.all_files()
#   for testdir in TEST.directions:
#       print testdir
#   for key in TEST.files.keys():
#       print key
#       print TEST.files[key]
    TEST.file_tree()


