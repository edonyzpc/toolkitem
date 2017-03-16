#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2017-03-16 23:17
 #
 # Filename: plandaycal.py
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
import calendar as cal
import time as ti


class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = """
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

class daycal:
    '''
    a calculator for plan end's date
    Input: year_start, month_start, day_start, planslist
    Output: year_end, month_end, day_end for each plan
    '''
    loct = ti.localtime()
    monthmap = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    def __init__(self,pls,year=loct[0],month=loct[1],day=loct[2]):
        self.year_start = int(year)
        self.month_start = int(month)
        self.day_start = int(day)
        self.month = daycal.monthls(self.year_start)
        self.pls = []
        for item in pls:
            self.pls.append(int(item))

    @staticmethod
    def monthls(year):
        '''
        get the month list of the year
        '''
        if(cal.isleap(year)):
            return {"Jan":31,"Feb":29,"Mar":31,"Apr":30,"May":31,"June":30,"July":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
        else:
            return {"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"June":30,"July":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}

    def calend(self):
        '''
        get the deadline day of the plan list
        '''
        self.planend = []
        month = self.month_start
        day = self.day_start
        for plan in self.pls:
            while plan > 0:
                plan -= self.month[daycal.monthmap[month%12]]
                if plan > 0:
                    month += 1
                else:
                    month_end = month
                    tday = plan + self.month[daycal.monthmap[month%12]]
                    day_end = day + tday
                    if day_end > self.month[daycal.monthmap[month%12]]:
                        month_end += 1
                        day_end = day_end - self.month[daycal.monthmap[month%12]]
                        month += 1
                    day = day_end
            if month/12 > 0:
                year_end = self.year_start + 1
            else:
                year_end = self.year_start
            self.planend.append((year_end,month_end,day_end))

    def __sumpls(self):
        return np.sum(np.array(self.pls))

    def __crossYear(self):
        '''
        check the plan list will go cross the year(feature year)
        '''
        all = self.__sumpls()
        start = self.month_start
        while True:
            all -= self.month[pycal.monthmap[start]]
            start += 1
            if all < 0:break
        return start/12

    def __displayplan(self):
        print('your plan arrangement:\n')
        length = len(self.planend)
        start = [(self.year_start,self.month_start,self.day_start)]
        for i in range(length-1):
            start.append((self.planend[i][0],self.planend[i][1],self.planend[i][2]+1))
        print start
        print self.planend

    def main(self):
        self.calend()
        self.__displayplan()

if __name__ == '__main__':
    plan = [10,42,7]
    tmp = daycal(plan)
    tmp.main()
    import sys
    p = sys.argv[1].split(',')
    tmp1 = daycal(p,sys.argv[2],sys.argv[3],sys.argv[4])
    tmp1.main()
