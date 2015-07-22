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
    from tkinter import messagebox as tkMessageBox
elif sys.version.startswith('2.7'):
    import Tkinter as tkinter
    import tkMessageBox
import shutil
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

class FileGUI(object):
    def __init__(self, root):
        self.root = root
        self.path = ""
        self.files = {}
        self.gif_file = ""
        #self.stl_file = ""
        #self.igs_file = ""
        self.init_gui()
        #self.pack(fill=tkinter.BOTH, expand=1)

    def get_files(self, path=None):
        if path:
            path = GD.normal_path(path)
            files_list = GD(path)
        else:
            self.path = GD.normal_path(self.path)
            files_list = GD(self.path)
        files_list.get_dir()
        files_list.all_files()
        self.files = files_list.files

    def update_files(self, path):
        if self.path != path:
            self.get_files(path)
        else:
            self.get_files(self.path)

    def update_listbox(self):
        self.lsbox.delete(0, self.lsbox.size())
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".gif"):
                    self.lsbox.insert(tkinter.END, name)

    def update_listbox_search(self, search_txt):
        self.lsbox_pc.delete(0, self.lsbox_pc.size())
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".sp") and search_txt in name:
                    self.lsbox_pc.insert(tkinter.END, name)

    def full_path_file(self, name):
        for path, item in self.files.items():
            if name in item:
                return path + "/" + name

    def init_gui(self):
        # labelframe of frame
        self.labframe = tkinter.LabelFrame(self.root, text="Animinate File", background="white")
        self.labframe.grid(row=0, columnspan=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)
        # listbox
        # listbox of point cloud labelframe
        ## lsbox_pc event handler
        def selectfile(event):
            event = self.lsbox.get(self.lsbox.curselection())
            self.gif_file = self.full_path_file(event)
            txt.set(self.lsbox.get(self.lsbox.curselection()))
            txt.set(self.gif_file)

        def rmfile(event):
            if tkMessageBox.askokcancel("Remove", "Are you sure to remove the file?"):
                event = self.lsbox_pc.get(self.lsbox_pc.curselection())
                remove_file = self.full_path_file(event)
                os.remove(remove_file)
                self.get_files()
                self.update_listbox()

        def addfile(evect):
            topdlg = tkinter.Toplevel(self.root)
            topdlg.title("Add Files")
            topdlg.geometry("250x80+300+200")
            def mvfile():
                if self.path:
                    event = enter_add_file.get()
                    #print event
                    filename = event[event.rfind("/"):]
                    shutil.move(event, self.path+"/"+filename)
                    self.get_files()
                    self.update_listbox()
                    topdlg.destroy()
                else:
                    txt.set("Please Set The Root Path")
                    topdlg.destroy()
            enter_add_file = tkinter.Entry(topdlg, width=250)
            label = tkinter.Label(topdlg, text="New File Name With Path", width=250, anchor="w", justify="left")
            label.pack(side=tkinter.TOP)
            #enter_add_file.bind("<Retrun>", mvfile)
            enter_add_file.pack()
            button_add_file = tkinter.Button(topdlg, text="Add Single File", command=mvfile)
            button_add_file.pack(side=tkinter.LEFT)
            button_add_file_list = tkinter.Button(topdlg, text="Add Multiple File", command=mvfile)
            button_add_file_list.pack(side=tkinter.RIGHT)

        self.lsbox = tkinter.Listbox(self.labframe, selectmode=tkinter.BROWSE, background="yellow")
        self.lsbox.bind("<Double-Button-1>", selectfile)
        self.lsbox.bind("<Double-Button-3>", rmfile)
        self.lsbox.bind("<Button-2>", addfile)
        for file in self.files:
            for name in self.files[file]:
                if name.endswith(".gif"):
                    self.lsbox_pc.insert(tkinter.END, name)
        self.lsbox.pack(expand=1, fill=tkinter.BOTH)
        # entry
        # entry of labframe
        ## enter event handler
        def getin(content):
            content = enter.get()
            self.path = content
            self.update_files(content)
            self.update_listbox()
            txt.set(enter.get())

        enter = tkinter.Entry(self.root, background="red")
        enter.grid(row=1, column=0, sticky=tkinter.S)
        enter.bind("<Return>", getin)

        # button
        button = tkinter.Button(self.root, text="Show", command=self.root.destroy)
        button.grid(row=1, column=1, sticky=tkinter.S)

        # message
        txt = tkinter.StringVar()
        message = tkinter.Message(self.root, textvariable=txt,
                                  text="INFO", anchor=tkinter.W,
                                  justify=tkinter.LEFT, width=200, background="cyan")
        message.grid(row=2, columnspan=2, sticky=tkinter.S+tkinter.N+tkinter.W+tkinter.E)

    def gif(self):
        return self.gif_file

if __name__ == "__main__":
    WIN = tkinter.Tk()
    WIN.title("File Manager")
    WIN.resizable(width=False, height=False)
    GUI = FileGUI(WIN)
    WIN.wm_attributes("-topmost", 1)
    WIN.mainloop()
    STL = GUI.gif_file
    print(STL)
