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
 # Last modified: 2015-07-21 00:56
 #
 # Filename: gifviewer.py
 #
 # Description: All Rights Are Reserved
 #
"""
import sys
if sys.version.startswith("2.7."):
    import Tkinter as tkinter 
elif sys.version.startswith("3.4."):
    import tkinter
from PIL import Image
from PIL import ImageTk
from filemanage import GUI
#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np

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


class GIFWin(tkinter.Label):
    def __init__(self, master, filename):
        self.im = Image.open(filename)
        self.master = master
        self.seq = []
        try:
            while 1:
                self.seq.append(self.im.copy())
                self.im.seek(len(self.seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = self.im.info['duration']
        except KeyError:
            self.delay = 100
        self.first = self.seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(self.first)]
        tkinter.Label.__init__(self, self.master, image=self.frames[0])

        temp = self.seq[0]
        for image in self.seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))
        self.idx = 0
        self.cancel = self.after(self.delay, self.Play)
        #self.button = tkinter.Button(self.master, text='stop', command=Stop)

    def Play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.Play)        

    def Stop(self):
        self.after_cancel(self.cancel)

def ViewGUI(filename):
    root = tkinter.Tk()
    root.title("GIF Viewer")
    anim = GIFWin(root, filename)
    anim.grid(row=0, columnspan=3, sticky=tkinter.N)
    fram = tkinter.LabelFrame(root, text="info")
    fram.grid(column=0, columnspan=2, rowspan=2, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    labtext_1 = tkinter.Label(fram, text="File: ")
    labtext_1.grid(row=1, column=0, sticky=tkinter.W)
    labtext_11 = tkinter.Label(fram,text=anim.im.filename[anim.im.filename.rfind("/")+1:])
    labtext_11.grid(row=1, column=1, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    labtext_2 = tkinter.Label(fram,text="GIF Delay: ")
    labtext_2.grid(row=2, column=0, sticky=tkinter.W)
    labtext_22 = tkinter.Label(fram,text=anim.im.info["duration"])
    labtext_22.grid(row=2, column=1, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    button = tkinter.Button(root, text="stop", command=anim.Stop)
    button.grid(row=1, column=2, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    button_q = tkinter.Button(root, text="quit", command=root.destroy)
    button_q.grid(row=2, column=2, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    root.wm_attributes("-topmost", 1)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ViewGUI(sys.argv[1])
    else:
        WIN = tkinter.Tk()
        WIN.title("File Manager")
        WIN.resizable(width=False, height=False)
        GUI = GUI(WIN)
        WIN.wm_attributes("-topmost", 1)
        WIN.mainloop()
        file = GUI.gif_file
        if file:
            ViewGUI(file)
        else:
            pass
