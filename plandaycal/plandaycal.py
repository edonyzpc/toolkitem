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
 # Last modified: 2015-04-20 15:25
 # 
 # Filename: plandaycal.py
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
 
import calendar as cal
import time as ti

class daycal:
    '''
    a calculator for plan end's date
    Input: year_start, month_start, day_start, planslist
    Output: year_end, month_end, day_end for each plan
    '''
    loct = ti.localtime()
    MONTH = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    def __init__(self,year=loct[0],month=loct[1],day=loct[2]):
        self.year_start = year
        self.month_start = month
        self.day = day
        self.enummonth = daycal.monthls(self.year_start)

    @staticmethod
    def monthls(year):
        '''
        get the month list of the year
        '''
        if(cal.isleap(year)):
            return {"Jan":31,"Feb":29,"Mar":31,"Apr":30,"May":31,"June":30,"July":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
        else:
            return {"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"June":30,"July":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}

    def calend(self,pls):
        '''
        get the deadline day of the plan list
        '''
        for day in pls:
            preday = day / 30
            DAY = 0
            for i in range(1,preday):
                DAY += self.enummonth[MONTH[self.month + i]]
            if day < DAY:
                self.day_end = self.day + day
                self.month_end = self.month_start
                self.year_end = self.year_start

           
