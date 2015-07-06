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
#import os
import sys
if sys.version.startswith('3.4'):
    import tkinter
else:
    import Tkinter as tkinter
from packages.filesline.getdirections import GetDirections as GD

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
        self.path = ""
        self.files = {}
        self.pc_file = ""
        self.stl_file = ""
        self.igs_file = ""
        self.init_gui()
        self.pack(fill=tkinter.BOTH, expand=1)

    def get_files(self, path=None):
        if path:
            files_list = GD(path)
        else:
            files_list = GD(self.path)
        files_list.get_dir()
        files_list.all_files()
        self.files = files_list.files

    def update_files(self, path):
        if self.path != path:
            self.get_files(path)

    def update_listbox(self):
        self.lsbox_pc.delete(0, self.lsbox_pc.size())
        self.lsbox_stl.delete(0, self.lsbox_stl.size())
        self.lsbox_igs.delete(0, self.lsbox_igs.size())
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".sp"):
                    self.lsbox_pc.insert(tkinter.END, name)
                if name.endswith(".stl"):
                    self.lsbox_stl.insert(tkinter.END, name)
                if name.endswith(".igs"):
                    self.lsbox_igs.insert(tkinter.END, name)

    def update_listbox_search(self, search_txt):
        self.lsbox_pc.delete(0, self.lsbox_pc.size())
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".sp") and search_txt in name:
                    self.lsbox_pc.insert(tkinter.END, name)

    def match_files(self, match_re):
        self.lsbox_stl.delete(0, self.lsbox_stl.size())
        self.lsbox_igs.delete(0, self.lsbox_igs.size())
        for file in self.files:
            for name in self.files[file]:
                if name.startswith(match_re+".") and name.endswith("stl"):
                    self.lsbox_stl.insert(tkinter.END, name)
                if name.startswith(match_re+".") and name.endswith("igs"):
                    self.lsbox_igs.insert(tkinter.END, name)

    def full_path_file(self, name):
        for path, item in self.files.items():
            if name in item:
                return path + "/" + name

    def init_gui(self):
        #self.get_files()
        # main frame
        self.frame_top = tkinter.Frame(self.root, height=400, width=800, background="black")
        self.frame_top.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.frame_bottom = tkinter.Frame(self.root, height=100, width=400, background="black")
        self.frame_bottom.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        self.frame_bottom_l = tkinter.Frame(self.root, height=100, width=400, background="black")
        self.frame_bottom_l.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

        # labelframe of bottom frame
        self.labframe = tkinter.LabelFrame(self.frame_bottom, text="Console",
                                           height=50, width=400, background="white")
        self.labframe.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
        # labelframel of bottom frame
        self.labframel = tkinter.LabelFrame(self.frame_bottom_l, text="Enter",
                                            height=50, width=400, background="white")
        self.labframel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        # labelframe of top frame
        self.labframe_bottom = tkinter.LabelFrame(self.frame_top, text="Point Cloud",
                                                  height=400, width=800, background="cyan")
        self.labframe_bottom.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
        self.labframe_left = tkinter.LabelFrame(self.frame_top, text="STL",
                                                height=400, width=400, background="cyan")
        self.labframe_left.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        self.labframe_right = tkinter.LabelFrame(self.frame_top, text="IGS",
                                                 height=400, width=400, background="cyan")
        self.labframe_right.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

        # message
        # message of labframe
        txt = tkinter.StringVar()
        msm_status = tkinter.Message(self.labframe, textvariable=txt, width=200, background="white")
        msm_status.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        txt.set("FILE MANAGEMENT START...")

        # button
        # quit button
        quit_button = tkinter.Button(self.labframe, text="Browser", relief=tkinter.SUNKEN,
                                     fg="blue", height=50,
                                     activebackground="green", command=self.root.destroy)
        quit_button.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
        # entry
        # entry of labframe
        ## enter event handler
        def getin(content):
            content = enter.get()
            self.update_files(content)
            self.update_listbox()
            txt.set(enter.get())

        enter_str = tkinter.StringVar()
        enter = tkinter.Entry(self.labframel, textvariable=enter_str, width=400, background="red")
        enter.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        enter.bind("<Return>", getin)

        # listbox
        # listbox of point cloud labelframe
        ## lsbox_pc event handler
        def selectpcfile(event):
            event = self.lsbox_pc.get(self.lsbox_pc.curselection())
            name_without = event.split(".")[0]
            self.match_files(name_without)
            self.pc_file = self.full_path_file(event)
            txt.set(self.lsbox_pc.get(self.lsbox_pc.curselection()))
            txt.set(self.pc_file)

        self.lsbox_pc = tkinter.Listbox(self.labframe_bottom,
                                        selectmode=tkinter.BROWSE, background="yellow")
        self.lsbox_pc.bind("<Double-Button-1>", selectpcfile)
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".sp"):
                    self.lsbox_pc.insert(tkinter.END, name)
        self.lsbox_pc.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        ## entry for lsbox_pc search
        ### enter for lsbox_pc  event handler
        def getsearch(content):
            content = enter_pc.get()
            self.update_listbox_search(content)
            txt.set(enter_pc.get())

        enter_str_pc = tkinter.StringVar()
        enter_pc = tkinter.Entry(self.labframe, textvariable=enter_str_pc, background="cyan")
        enter_pc.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
        enter_pc.bind("<Return>", getsearch)
        # listbox of STL labelframe
        def selectstlfile(event):
            event = self.lsbox_stl.get(self.lsbox_stl.curselection())
            self.stl_file = self.full_path_file(event)
            txt.set(self.stl_file)

        self.lsbox_stl = tkinter.Listbox(self.labframe_left,
                                         selectmode=tkinter.BROWSE, background="yellow")
        self.lsbox_stl.bind("<Double-Button-1>", selectstlfile)
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".stl"):
                    self.lsbox_stl.insert(tkinter.END, name)
        self.lsbox_stl.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # listbox of IGS labelframe
        def selectigsfile(event):
            event = self.lsbox_igs.get(self.lsbox_igs.curselection())
            self.igs_file = self.full_path_file(event)
            txt.set(self.igs_file)

        self.lsbox_igs = tkinter.Listbox(self.labframe_right,
                                         selectmode=tkinter.BROWSE, background="yellow")
        self.lsbox_igs.bind("<Double-Button-1>", selectigsfile)
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".igs"):
                    self.lsbox_igs.insert(tkinter.END, name)
        self.lsbox_igs.pack(side=tkinter.TOP, fill=tkinter.BOTH)

if __name__ == "__main__":
    WIN = tkinter.Tk()
    WIN.geometry("800x450+200+300")
    WIN.title("File Manager")
#    root.resizable(width=False, height=False)
    GUI = GUI(WIN)
    WIN.mainloop()
    STL = GUI.stl_file
    IGS = GUI.igs_file
    print(STL)
    print(IGS)
