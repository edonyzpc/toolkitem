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
 # Last modified:	2016-01-06 21:08
 #
 # Filename:		scheduler.py
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
from apscheduler.schedulers.blocking import BlockingScheduler as bs
from time import localtime as lt
import os
import sys
import pickle as cP

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

def job_trigger(job, *kargs):
    print("Edony, Anthelion's Pulling The Trigger")
    job(kargs)

def sched_tasks(jobs, timestr=None, **kwargs):
    sched = bs(daemonic=True)
    if timestr:
        timels = timestr.split('-') # input time string with cmd `$(date +%Y/%m/%d/%H/%M/%S)`
        y = int(timels[0])
        m = int(timels[1])
        d = int(timels[2])
        h = int(timels[3])
        min = int(timels[4])
        sec = int(timels[5])
    else:
        y = lt().tm_year
        m = lt().tm_mon
        d = lt().tm_mday
        h = lt().tm_hour
        min = lt().tm_min
        sec = lt().tm_sec
    time_ls = [y, m, d, h, min, sec]
    if 'timstring.pickle' in os.listdir('/home/edony/code/github/toolkitem/emtools'):
        with open('/home/edony/code/github/toolkitem/emtools/timstring.pickle','rb') as filebuf:
            ls_tmp = cP.load(filebuf)
            tick = [y - ls_tmp[0], m - ls_tmp[1], d - ls_tmp[2],\
                    h - ls_tmp[3], min - ls_tmp[4], sec - ls_tmp[5]]
            #convert all time(Y.M.D.H.Min.Sec) to seconds
            timeticking = 60*(60*(24*(30*(365*tick[0]+tick[1])+tick[2])+tick[3])+tick[4])+tick[5]
    else:
        with open('timstring.pickle', 'wb') as filebuf:
            cP.dump(time_ls, filebuf, cP.HIGHEST_PROTOCOL)
            timeticking = 0

    if timeticking > 0:
        print("Be Activated")
    else:
        for job in jobs:
            #print(kwargs[job.__name__])
            sched.add_job(job, 'cron', kwargs[job.__name__], year=y,\
                    month=m, day=d, hour=h, minute=min, second=sec+3, id=job.__name__)
        try:
            print("Hi Edony, Anthelion's Pulling The Trigger")
            sched.start()
        except(KeyboardInterrupt, SystemExit):
            sched.shutdown()


if __name__ == '__main__':
    #sched_tasks(('edony'))
    def job1(a):print(a)
    def job2(c, d):print(c+d)
    jobs = [job1, job2]
    args = {job1.__name__:[12], job2.__name__:[2,5]}
    sched_tasks(jobs, timestr=sys.argv[1], **args)
