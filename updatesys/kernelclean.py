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
from __future__ import absolute_import

import os
import re
import sys
import subprocess as sp
import platform as pf
from getpass import getpass
import hashlib
if sys.version.startswith("3.4."):
    from functools import reduce
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

class KernelClean(object):
    """
    Cleanup the Fedora Linux kernel after `dnf(yum) update`.
    """
    def __init__(self, check=0):
        self._filebuf = 'kernelclean'
        self.kernel = ''
        self.exist_kernels = []
        self.old_kernel = []
        self.kernel_clean = []
        self.color = PyColor()
        # self.check for manual check to remove system kernel(1 for check, 0 for not check)
        self.check = check
        self.record = []

    def in_using_kernel(self):
        """
        RPM query about the kernel existing in the system => self._filebuf
        Get the version of running kernel => self.kernel

        ***rewrite the using kernel finding***
        command_rpm_kernel = 'rpm -qa | grep "^kernel-" > '
        command_rpm_kernel += self._filebuf
        os.system(command_rpm_kernel)
        command_kernel = 'uname -r'
        pipeout = sp.Popen(command_kernel.split(), stdout=sp.PIPE)
        self.kernel = pipeout.stdout.readline().rstrip().decode('utf-8')
        """
        pipeout = sp.Popen('uname -r'.split(), stdout=sp.PIPE)
        self.kernel = pipeout.stdout.readline().rstrip().decode('utf-8')
        out = sp.Popen('rpm -qa'.split(), stdout=sp.PIPE)
        for ls in out.stdout.readlines():
            pattern = '^kernel-'
            ls = ls.rstrip().decode('utf-8')
            if re.match(pattern, ls):
                self.exist_kernels.append(ls)

    def find_old_kernel(self):
        """
        Find the old kernel in system => self.old_kernel
        """
        pattern = "^kernel-[a-zA-Z-]*([0-9.-]*)([a-zA-Z]+)(.*)"
        self.record = set([re.match(pattern, item).groups() for item in self.exist_kernels])
        self.old_kernel = [item for item in self.record if item[0] not in self.kernel]

    def to_cleaned_kernel(self):
        """
        Ensure the to be cleaned kernel in queried list => self.kernelclean
        """
        if self.old_kernel:
            kernel_clean_id = []
            [kernel_clean_id.append(''.join(item)) for item in list(self.old_kernel)]
            for id in kernel_clean_id:
                [self.kernel_clean.append(item) for item in self.exist_kernels if id in item]

    def cleanup(self):
        """
        Cleanup the old kernel
        """
        if self.old_kernel:
            reboot = input(self.color.endcolor + 'Do You Need to Reboot System?(y or n)\n')
            if reboot == 'y':
                os.system('reboot')
            elif reboot == 'n':
                print(self.color.warningcolor + 'Cleanup Kernel ...' + self.color.endcolor)
                pwd_md5 = 'b04c541ed735353c44c52984a1be27f8'
                pwd = getpass("Enter Your Password: ")
                if hashlib.md5(pwd.encode('utf-8')).hexdigest() != pwd_md5:
                    print(self.color.warningcolor + "Wrong Password" + self.color.endcolor)
                    print('\033[0;36m' + "Try Angain" + '\033[0m')
                    pwd = getpass("Enter Your Password: ")
                    if hashlib.md5(pwd.encode('utf-8')).hexdigest() != pwd_md5:
                        return
                echo = ['echo']
                echo.append(pwd)
                if pf.linux_distribution()[1] > '21':
                    command = 'sudo -S dnf -y remove '
                    for item in self.kernel_clean:
                        command += item
                        command += ' '
                else:
                    command = 'sudo -S yum -y remove '
                    for item in self.kernel_clean:
                        command += item
                        command += ' '
                pipein = sp.Popen(echo, stdout=sp.PIPE)
                pipeout = sp.Popen(command.split(), stdin=pipein.stdout, stdout=sp.PIPE)
                for line in pipeout.stdout.readlines():
                    if line == '':
                        break
                    if isinstance(line, bytes):
                        line = line.decode()
                    print(line)
                print(self.color.tipcolor + 'End Cleanup!' + self.color.endcolor)
                print(self.color.warningcolor +\
                        'Your Kernel is Update!' +\
                        self.color.endcolor)

    def main(self):
        """
        Union the cleanup stream
        """
        self.in_using_kernel()
        self.find_old_kernel()
        self.to_cleaned_kernel()
        if self.check == 1:
            if self.old_kernel:
                print(self.color.tipcolor + 'Your Old Kernel: ')
                for item in self.old_kernel:
                    print(''.join(item))
                print(self.color.warningcolor + 'In Using Kernel: ')
                print(self.kernel + self.color.endcolor)
                check_cmd = input('Remove the old kernel?(y or n)\n')
                if check_cmd == 'y':
                    self.cleanup()
                else:
                    print('\033[36m' + 'Do Not Remove Old kernel' + '\033[0m')
            else:
                print(self.color.tipcolor +\
                        'Your System Has No Old Kernel To Cleanup!' +\
                        self.color.endcolor)

if __name__ == '__main__':
    TEST = KernelClean(1)
    TEST.in_using_kernel()
    TEST.find_old_kernel()
    TEST.to_cleaned_kernel()
