#!/usr/bin/env python
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
 # Last modified: 2015-07-03 20:06
 #
 # Filename: frameset.py
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
import os
if sys.version.startswith('2.7'):
    import Tkinter as tkinter
else:
    import tkinter

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

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("500x500")
    root.title("file list")
    f1 = tkinter.LabelFrame(root, text="f1",height=300, width=200, background="red")
    f1.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f2 = tkinter.Frame(root, height=200, width=200, background="white")
    f2.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
    b1 = tkinter.Button(f1, background="white")
    b1.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
    def printlist(event):
        print(lsbox1.get(lsbox1.curselection()))
    lsbox1 = tkinter.Listbox(root, selectmode=tkinter.BROWSE, background="yellow")
    lsbox1.bind("<Double-Button-1>", printlist)
    for ind, file in enumerate(os.listdir("./")):
        lsbox1.insert(tkinter.END, file)
    print(lsbox1.size())
    #lsbox1.selection_set(1,6)
    #print(lsbox1.curselection())
    lsbox1.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    lsbox = tkinter.Listbox(f1, height=120,background="blue")
    lsbox.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    root.mainloop()
