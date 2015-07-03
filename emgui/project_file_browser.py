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
 # Last modified: 2015-07-03 21:38
 #
 # Filename: project_file_browser.py
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
import sys
if sys.version.startswith('3.4'):
    import tkinter
else:
    import Tkinter as tkinter

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

class GUI(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root, background="white")
        self.root = root
        self.root.title("File Manager")
        self.path = "./"
        self.InitUI()
        self.pack(fill=tkinter.BOTH, expand=1)

    def InitUI(self):
        # main frame
        frame_top =  tkinter.Frame(root, height=350, width=800, background="black")
        frame_top.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        frame_bottom =  tkinter.Frame(root, height=100, width=800, background="black")
        frame_bottom.pack(after=frame_top, fill=tkinter.BOTH)

        # labelframe of bottom frame
        labframe = tkinter.LabelFrame(frame_bottom, text="Console",
                height=100, width=800, background="white")
        labframe.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
        # labelframe of top frame
        labframe_bottom = tkinter.LabelFrame(frame_top, text="Point Cloud",
                height=350, width=800, background="cyan")
        labframe_bottom.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

        labframe_left= tkinter.LabelFrame(frame_top, text="STL",height=350, width=400, background="cyan")
        labframe_left.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        labframe_right = tkinter.LabelFrame(frame_top, text="IGS",height=350,  width=400, background="cyan")
        labframe_right.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

        # message 
        # message of labframe
        txt = tkinter.StringVar()
        msm_status = tkinter.Message(labframe, textvariable=txt, width=400, background="white")
        msm_status.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        
        # listbox
        # listbox of point cloud labelframe
        def selectpcfile(event):
            txt.set("selected!")
            return lsbox_pc.get(lsbox_pc.curselection())
        lsbox_pc = tkinter.Listbox(labframe_bottom, selectmode=tkinter.BROWSE, background="yellow")
        lsbox_pc.bind("<Double-Button-1>", selectpcfile)
        for ind, file in enumerate(os.listdir(self.path)):
            lsbox_pc.insert(tkinter.END, file)
        print(lsbox_pc.size())
        lsbox_pc.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # listbox of STL labelframe
        def selectstlfile(event):
            return lsbox_stl.get(lsbox_stlpc.curselection())
        lsbox_stl = tkinter.Listbox(labframe_left, selectmode=tkinter.BROWSE, background="yellow")
        lsbox_stl.bind("<Double-Button-1>", selectstlfile)
        for ind, file in enumerate(os.listdir(self.path)):
            lsbox_stl.insert(tkinter.END, file)
        print(lsbox_stl.size())
        lsbox_stl.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # listbox of IGS labelframe
        def selectigsfile(event):
            return lsbox_igs.get(lsbox_igs.curselection())
        lsbox_igs = tkinter.Listbox(labframe_right, selectmode=tkinter.BROWSE, background="yellow")
        lsbox_igs.bind("<Double-Button-1>", selectigsfile)
        for ind, file in enumerate(os.listdir(self.path)):
            lsbox_igs.insert(tkinter.END, file)
        print(lsbox_igs.size())
        lsbox_igs.pack(side=tkinter.TOP, fill=tkinter.BOTH)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("800x450")
    root.resizable(width=False, height=False)
    gui = GUI(root)
    root.mainloop()


