#! /usr/bin/python
#encoding: utf-8
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
 # ########################################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-04-16 23:44
 # 
 # Filename: filesline.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "py" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    
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
    
    e.g：
    \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
    \033[0m         <!--set all into default-->
    '''
    WARN = '\033[0;37;41m'
    NOTE = '\033[4;32m'
    ENDC = '\033[0m'
    def disable(self):
        self.ENDC = ''
        self.WARNING = ''
 
#import numpy as np
#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
import os
import re


class FileLine:
    def __init__(self,dir):
        self.dir = dir
        os.chdir(dir)
        self.files = {}

    @staticmethod
    def dirlist(dir,rec):
        '''
        record all the directions of included in the given direction and its sub-direction
        '''
        tmpls = os.listdir(dir)
        os.chdir(dir)
        dirls = [item for item in tmpls if os.path.isdir(item)]
        rec.extend([dir+'/'+item for item in dirls])
        if dirls:
            for item in dirls:
                #print(dir+'/'+item)
                fileline.dirlist(dir+'/'+item,rec)
                #print dirls
        else:
            #dirls.append(dir)
            return dirls

    def adddirs(self):
        rec = []
        fileline.dirlist(self.dir,rec)
        self.alldir = rec
        self.alldir.append(self.dir)

    def filelist(self):
        for dir in self.alldir:
            os.chdir(dir)
            tmpls = os.listdir(dir)
            self.files[dir] = [item for item in tmpls if os.path.isfile(item)]

    def filter(self):
        self.ffilter()

    @staticmethod
    def lofdir(file):
        lofdir = 0
        for item in file:
            f = open(item)
            for line in f.readlines():
                lofdir += 1
            f.close()
        return lofdir

    def popexceptdir(self,exceptdir):
        import re
        pattern = exceptdir+'/.*'
        p = re.compile(str(pattern))
        for d in self.alldir:
            if not p.match(d) is None:
                print 'poping',
                self.alldir.remove(d)

class FileFilter(FileLine):
    def ffilter(self):
        p = re.compile(r'.*(\.(py|h|cpp|cxx|c|hpp))$')
        #tmp = [item for item in self.files.values() if p.match(item) is None]
        #for key in self.files.keys():#remove the blank value
        #    if not self.files[key]:
        #        self.files.pop(key)
        for key in self.files.keys():
            for item in self.files[key]:
                if p.match(item) is None:
                    cou = self.files[key].index(item)
                    self.files[key][cou] = None

if __name__ == '__main__':
    dir = raw_input('Enter the direction you want to count: ')
    #dt = []
    #tmp = fileline.dirlist(dir,dt)
    #print dt
    #delegation rule of filtering the files

    tmp = FileFilter(dir)
    tmp.adddirs()
    exceptdir = raw_input("Enter the direction you want ignore: ")
    tmp.popexceptdir(exceptdir)
    tmp.FileList()
    tmp.filter()
    key = tmp.files.keys()
    files = []
    for i in key:
        for item in tmp.files[i]:
            if not item == None:
                files.append(i+'/'+item)
    #for f in files:
    #    print f
    lines = fileline.lofdir(files)
    print('total lines are %d'%lines)
                
