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
 # Last modified: 2017-03-19 21:24
 #
 # Filename: pycolor.py
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
from __future__ import print_function

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self, format=None):
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
        self.magic = '\033['
        self.color = format
        self.__formats = {'red':(0, 31, 40), 'green':(0, 32, 40), 'cyan':(0, 36, 40),
                         'purple':(0, 35, 40), 'yellow':(0, 33, 40), 'white':(0, 37, 40),
                         'ured':(4, 31, 40), 'ugreen':(4, 32, 40), 'ucyan':(4, 36, 40),
                         'upurple':(4, 35, 40), 'uyellow':(4, 33, 40), 'uwhite':(4, 37, 40),
                         'fred':(5, 31, 40), 'fgreen':(5, 32, 40), 'fcyan':(5, 36, 40),
                         'fpurple':(5, 35, 40), 'fyellow':(5, 33, 40), 'fwhite':(5, 37, 40),
                         'nred':(5, 31, 40), 'ngreen':(5, 32, 40), 'ncyan':(5, 36, 40),
                         'npurple':(5, 35, 40), 'nyellow':(5, 33, 40), 'nwhite':(5, 37, 40)
                        }
        if format in self.__formats.keys():
            fmt = self.__formats[format]
            self._mod = str(fmt[0]) + ';'                       # display model: [0, 1, 4, 5, 7, 8]
            self._fg_color = str(fmt[1]) + ';'                  # foreground color: [30, 31, 32, 33, 34, 35, 36, 37]
            self._bg_color = str(fmt[2]) + 'm'                  # background color: [40m, 41m, 42m, 43m, 44m, 45m, 46m, 47m]
        else:
            self._mod = '0;'
            self._fg_color = '37;'
            self._bg_color = '40m'
        # output format string
        self._format = self.magic +\
                       self._mod +\
                       self._fg_color +\
                       self._bg_color
        # reset the format
        self.reset = '\033[0m'

    def __call__(self, func):
        def wrapper(fmt_str):
            func(self.colorstr(fmt_str))
        return wrapper

    @property
    def format(self):
        """
        Customized Python Print Color.
        """
        return self.color

    @format.setter
    def format(self, color_str):
        """
        New Color.
        """
        self.color = color_str
        self._format = self.__formats[color_str]

    def disable(self):
        """
        Disable Color Print.
        """
        self.color = ''
        self._format = ''

    def __str2fmts(self, color_str):
        """
        Convert description of format into format number
        """
        self.color = color_str
        self.format = self.__formats[color_str]

    def colorstr(self, string, color=None):
        """Contert string to colorful format string
        """
        if color is None:
            return self._format + string + self.reset
        else:
            self.__str2fmts(color)
            return self._format + string + self.reset

def cprint(color, out_str):
    """Colorful print function instead of standard print
    """
    @PyColor(color)
    def printer(out_str):
        print(out_str)

    printer(out_str)
