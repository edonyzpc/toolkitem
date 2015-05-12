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
 # Last modified: 2015-05-12 16:46
 #
 # Filename: pairfile.py
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
from packages.filesline.filesline import FileLine as FL
from filebuf import FileBuf as FB

class FilePair(FL):
    """
    FILEPAIR: class to pair the files in direction and pair-direction according with file name
    """
    def __init__(self, dir, pair_dir):
        """
        Initialize the instance attribute: [FileLine Class with `dir`, pair direction]
        """
        self.fileline = FL(dir)    # direction to compared with
        self.pair_dir = pair_dir   # direction compared with
        self.paired_file = []
        self.nonpaired_file = []

    def __filelist(self, dir):
        """
        List file in direction
        """
        self.fileline.alldir = [dir]
        self.fileline.filelist()

    def pairfiles(self):
        """
        Browse the files and mark up the paired files and the new files
        """
        self.__filelist(self.fileline.dir)
        self.__filelist(self.pair_dir)
        for file in self.fileline.files[self.fileline.dir]:
            if file in self.fileline.files[self.pair_dir]:
                self.paired_file.append(file)
            else:
                self.nonpaired_file.append(file)

class FileCheck(FB):
    """
    FILECHECK: class to check the paired files and record the different lines
    """
    def __init__(self, paired_files, to_paire_dir, paired_dir):
        self.paired_files = paired_files
        self.to_paire_dir = to_paire_dir
        self.paired_dir = paired_dir
        self.buffer = []
        self.new_file = []

    def check_diff(self):
        for filename in self.paired_files:
            self.buffer.append('FILE ' + filename + '\n')
            self.file1 = self.to_paire_dir + '/' + filename
            self.file2 = self.paired_dir + '/' + filename
            self.file1_line_num = len(open(self.file1).readlines())
            self.file2_line_num = len(open(self.file2).readlines())
            self.mark_diff()

    def record_diff(self):
        os.chdir(self.to_paire_dir)
        self.write_file()

    def new_file(self):
        """
        Check the to pair direction to find if there are new files.
        """
        directlist = os.listdir(self.to_paire_dir)
        os.chdir(self.to_paire_dir)
        for filename in directlist:
            if os.path.isfile(filename):
                if filename not in self.paired_files:
                    self.new_file.append(filename)

if __name__ == '__main__':
    dir = '/home/edony/code/github/toolkitem/mergefile'
    tmp = FilePair(dir+'/f1', dir+'/f2')
    tmp.pairfiles()
    print tmp.paired_file
    print tmp.nonpaired_file
    tmp1 = FileCheck(tmp.paired_file, dir+'/f1', dir+'/f2')
    tmp1.check_diff()
    tmp1.record_diff()
