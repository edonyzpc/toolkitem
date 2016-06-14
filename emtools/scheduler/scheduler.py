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
import platform as plf

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
    """
    Scheduler for Jobs.
    """
    sched = bs(daemonic=True)
    color = PyColor()
    linuxpath='/home/edony/code/github/toolkitem/emtools'
    macpath='/Users/edony/coding/toolkitem/emtools'
    if plf.system() == "Darwin":
        path = macpath
    elif plf.system() == "Linux":
        path = linuxpath
    sched = bs(daemonic=True)
    if timestr:
        timels = timestr.split('-') # input time string with cmd `$(date +%Y/%m/%d/%H/%M/%S)`
        y, m, d, h, min, sec = int(timels[0]), int(timels[1]),\
                int(timels[2]), int(timels[3]), int(timels[4]), int(timels[5])
    else:
        y, m, d, h, min, sec = lt().tm_year, lt().tm_mon,\
                lt().tm_mday, lt().tm_hour, lt().tm_min, lt().tm_sec
    for job in jobs:
        #print(kwargs[job.__name__])
        sched.add_job(job, 'cron', kwargs[job.__name__], year=y,\
                month=m, day=d, hour=h, minute=min, second=sec+3, id=job.__name__)
    try:
        print("\033[0;36mHi Edony, Anthelion's Pulling The Trigger")
        sched.start()
    except(KeyboardInterrupt, SystemExit):
        print(color.warningcolor + "Be Activated" + color.endcolor)
        sched.shutdown()

if __name__ == '__main__':
    #sched_tasks(('edony'))
    def job1(a):print(a)
    def job2(c, d):print(c+d)
    jobs = [job1, job2]
    args = {job1.__name__:[12], job2.__name__:[2,5]}
    sched_tasks(jobs, timestr=sys.argv[1], **args)
