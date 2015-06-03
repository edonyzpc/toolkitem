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
 # Last modified: 2015-06-02 20:50
 #
 # Filename: kernelclean.py
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
import subprocess as sp
from packages.fileparser.extractor import Extractor

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

class KernelClean(object):
    """
    Cleanup the Fedora Linux kernel after `dnf(yum) update`.
    """
    def __init__(self, check=0):
        self._filebuf = 'kernelclean'
        self.command_rpm_kernel = 'rpm -qa | grep kernel- > kernelclean'
        os.system(self.command_rpm_kernel)
        self.command_kernel = 'uname -r'
        self.kernel = ''
        self.old_kernel = ''
        self.kernel_clean = ''
        self.color = PyColor()
        self.check = check

    def using_kernel(self):
        pipeout = sp.Popen(self.command_kernel.split(), stdout=sp.PIPE)
        self.kernel = pipeout.stdout.readline().rstrip()
        
    def find_old_kernel(self):
        with open(self._filebuf) as buf:
            counter = 0
            for line in buf.readlines():
                if line.rstrip().endswith(self.kernel):
                    if counter < len(buf.readlines()):
                        counter += 1
                        continue
                    else:
                        return
                else:
                    head = line.rstrip().split(self.kernel)[0]
                    self.old_kernel = line.rstrip().split(head)[1]
                    break

    def clean_kernel(self):
        if self.old_kernel:
            with open(self._filebuf) as buf:
                for line in buf.readlines():
                    if line.rstrip().endswith(self.old_kernel):
                        self.kernel_clean += line.rstrip()
                        self.kernel_clean += ' '

    def cleanup(self):
        if self.kernel_clean:
            print self.color.warningcolor + 'cleanup kernel' + self.color.endcolor
            pwf = open(self.pwd)
            password = pwf.readline().rstrip()
            pwf.close()
            echo = ['echo']
            echo.append(password)
            if pf.linux_distribution()[1] > '21':
                command = 'sudo -S dnf -y remove '
                command += self.kernel_clean
            else:
                command = 'sudo -S yum -y remove '
                command += self.kernel_clean
            pipein = sp.Popen(echo, stdout=sp.PIPE)
            pipeout = sp.Popen(command.split(), stdin=pipein.stdout, stdout=sp.PIPE)
            for line in pipeout.stdout.readlines():
                if line == '':
                    break
                elif 'error:' in line.split()\
                        or 'warning:' in line.split()\
                        or 'fatal:' in line.split():
                    print self.pcolor.warningcolor + line + self.pcolor.endcolor
                else:
                    print line
            print self.color.tipcolor + 'end cleanup' + self.color.endcolor
        else:
            print self.color.warningcolor +\
                    'Your Kernel is Update!' +\
                    self.color.endcolor

    def main(self):
        self.using_kernel()
        self.find_old_kernel()
        self.clean_kernel()
        if self.check == 1:
            print self.color.warningcolor +\
                    'Your Using Kernel is ' +\
                    self.kernel +\
                    self.color.endcolor +\
                    '\n' +\
                    self.color.tipcolor +\
                    'Your Old Kernel is ' +\
                    self.old_kernel +\
                    self.color.endcolor +\
                    '\n' +\
                    'To Be Removed Kernel Packages ' +\
                    self.kernel_clean
            check_cmd = raw_input('Remove the old kernel?(y or n)')
        if check_cmd == 'y':
            self.cleanup()
        else:
            print 'Do Not Remove Old kernel\n'

if __name__ == '__main__':
    test = KernelClean(1)
    test.main()
