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
 # Last modified: 2015-10-18 22:01
 #
 # Filename: FilterColumn.py
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
import TextRead as TR

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

def filecolumn(lines, col_num):
    """
    Get col_num(th) Column
    """
    return [item[col_num] for item in lines]

def maxitem(items):
    """
    Find the Maximum Item According to Its Literal Value
    """
    tmp = [float(item) for item in items]
    tmp.sort(reverse=True)
    return str(tmp[0])

def paircolumn(columns, rule):
    """
    Match the Column Item
    """
    return rule(columns)

def extractline(lines, col_num):
    """
    Extract the Match Line According to Paired Column Item
    """
    columns = filecolumn(lines, col_num)
    matched = paircolumn(columns, maxitem)
    return columns.index(matched)

def preprocess(proc, *args):
    """
    Do Some Pre-Process When Handle The Text
    """
    proc(*args)

if __name__ == "__main__":
    lines = TR.read2columns('kernelclean.test')
    lines = TR.removeblankline(lines)
    print(len(lines))
    counter = 3
    while counter > 0:
        preprocess(TR.rmline, (lines, 0))
        counter -= 1
    #TR.rmline(lines,0)
    #TR.rmline(lines,0)
    #TR.rmline(lines,0)
    print(extractline(lines, 3))
    print(lines[extractline(lines,3)])
