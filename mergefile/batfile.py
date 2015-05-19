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
 # Last modified: 2015-05-19 19:58
 #
 # Filename: batfile.py
 #
 # Description: All Rights Are Reserved
 #
"""
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
    def new(self,color_str):
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

#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np
import os
from packages.filesline.filesline import FileLine

class BatchFileMerge(FileLine):
    def __init__(self, dir1, dir2, dir3):
        FileLine.__init__(self, dir1)
        self.mergeinto_direction = dir1
        self.mergefrom_direction = dir2
        self.main_direction = dir3
        self.new_files = []
        self.mergeinto_files = []
        self.mergefrom_files = []

    def find_file_list(self, file_dir):
        self.alldir = [file_dir]
        self.filelist()

    def match_file_name(self):
        self.find_file_list(self.mergeinto_direction)
        self.find_file_list(self.mergefrom_direction)
        for file in self.files[self.mergeinto_direction]:
            if file in self.files[self.mergefrom_direction]:
                self.mergeinto_files.append(self.mergeinto_direction + "/" + file)
            else:
                self.new_files.append(self.mergeinto_direction + "/" +  file)
        for file in self.files[self.mergefrom_direction]:
            if file in self.files[self.mergeinto_direction]:
                self.mergefrom_files.append(self.mergefrom_direction + "/" +  file)
            else:
                self.new_files.append(self.mergefrom_direction + "/" +  file)
        if len(self.mergefrom_files) != len(self.mergeinto_files):
            raise Exception("WRONG FILES")

    def backupfiles(self, backup_dir):
        os.chdir(backup_dir)
        for file in self.files[backup_dir]:
            command = "cp "
            command += file + " " + file + "_bak"
            print command
            val = os.system(command)

    def mergefiles(self):
        self.mergeinto_files = sorted(self.mergeinto_files)
        self.mergefrom_files = sorted(self.mergefrom_files)
        file_counter = 0
        os.chdir(self.main_direction)
        for file in self.mergeinto_files:
            merge_command = "./analysefile.sh "
            merge_command += "." + file.split(self.main_direction)[1]
            merge_command += " " + "."
            merge_command += self.mergefrom_files[file_counter].split(self.main_direction)[1]
            print merge_command
            os.system(merge_command)
            file_counter += 1

if __name__ == "__main__":
    dir1 = "/home/edony/code/github/toolkitem/mergefile/f1"
    dir2 = "/home/edony/code/github/toolkitem/mergefile/f2"
    dir3 = "/home/edony/code/github/toolkitem/mergefile"
    test = BatchFileMerge(dir1, dir2, dir3)
    test.match_file_name()
    test.backupfiles(dir1)
    print test.mergeinto_files
    print test.mergefrom_files
    test.mergefiles()
