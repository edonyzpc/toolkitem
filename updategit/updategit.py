#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
 # Last modified: 2015-04-23 09:29
 # 
 # Filename: updategit.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "F2" call Addpy() function to add this class which is defined
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
    WARNING = '\033[0;37;41m'
    ENDC = '\033[0m'
    TIPS = '\033[0;31;42m'
    def disable(self):
        self.ENDC = ''
        self.WARNING = ''
 
import numpy as np
import scipy as sp
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
from matplotlib import cm
 
def gitrepos(path='~/code/github'):
    '''
    find the git repositroies in the direction 
    '''
    from filesline.filesline import fileline as fl
    rec = []
    gitdir = []
    fl.dirlist(path,rec)
    for direction in rec:
        tmp = direction.split('/')
        __delblank(tmp)
        if '.git' in tmp:
            tmpgitdir = __gitroot(tmp)
            gitdir.append(tmpgitdir)
    return set(gitdir)

def updategit(gitdir):
    import os
    for dir in gitdir:
        os.chdir(dir)
        status = os.popen('git pull')
        print pcolor.WARNING + dir + pcolor.ENDC
        __outstatus(status)
    print pcolor.TIPS + 'update git repositroies finished' + pcolor.ENDC


def __gitroot(gitpath):
    root = ''
    for item in gitpath:
        if item == '.git':
            break
        else:
            root += '/'+item
    return root

def __delblank(ls):
    for item in ls:
        if item=='':
            ls.remove(item)

def __outstatus(f):
    for line in f.readlines():
        if line == '':
            break
        elif 'error:' in line.split()or 'waring:' in line.split():
            print pcolor.WARNING + line + pcolor.ENDC
        else:
            print line

def main():
    tardir = raw_input('git repositroies path: ')
    dir = gitrepos(tardir)
    updategit(dir)

if __name__ == '__main__':
    main()