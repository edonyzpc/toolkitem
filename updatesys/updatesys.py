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
 # Last modified: 2015-05-07 20:57
 #
 # Filename: updategit.py
 #
 # Description: All Rights Are Reserved
 #
 # This module is a tool for managing system.
"""
from __future__ import absolute_import
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
import hashlib
from getpass import getpass
import platform as pf
import subprocess as sp
import argparse as ap
#from packages.filesline.getdirections import GetDirections as GD
from packages.filesline.browser import getdirections as GD
from packages.filesline.browser import getfiles as GF
from kernelclean import KernelClean as KC

__version__ = 1.0
__author__ = 'edony'

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    """
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
        Disable the Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''

class UpdateSys(object):
    """
    UPDATESYS: class to make the work system automatic management.

    This tool update your system, manage your builtin tools, update your project.

    See UpdateSys.updategit, UpdateSys.main, UpdateSys.cmd_parser.

    Usage updategit [-l | -m | -g | -c | -p | -a]...[argv]
    default : Update System and Repositories
    -l      : Manage Linux Builtin Tools
    -m      : Manage MacOS Builtin Tools
    -g      : Update projects in default diection or given path
    -c      : Cleanup the old kernel in Fedora system or cleanup Mac brew pkg
    -p      : Specific the Path to Manage
    -a      : Get Details in Document of Attributes

    >>> tmp = UpdateSys()
    >>> tmp.main()
    """
    def __init__(self, path=None):
        """
        Initialize the path of to be managed projects, it takes path parameter.
        The path has its default direction with different platform.
        """
        self.gitdir = []
        self.hgdir = []
        self.pcolor = PyColor()
        self.parser = ap.ArgumentParser()
        self.pwd_md5 = 'b04c541ed735353c44c52984a1be27f8'
        if path:
            self.path = path
        else:
            self.path = ''

    def __gitrepos(self):
        """
        Find the git repositroies in the self.path
        """
        tmp_getdirection = GD(self.path)
        #tmp_getdirection.get_dir()
        for direction in tmp_getdirection:
            os.chdir(direction)
            if '.git' in os.listdir(direction) and direction not in self.gitdir:
                self.gitdir.append(direction)
            if '.hg' in os.listdir(direction) and direction not in self.hgdir:
                self.hgdir.append(direction)

    def __outstatus(self, outstatus_file):
        """
        Print highlight the executed cmd results.
        """
        for line in outstatus_file.readlines():
            if isinstance(line, bytes):
                line = line.decode()
            if line == '':
                break
            print(line.rstrip())

    def __updatebrew(self):
        """
        Mange MacOS builtin tools.
        """
        print(self.pcolor.warningcolor + 'brew updating' + self.pcolor.endcolor)
        brewstatus = os.popen('brew update')
        self.__outstatus(brewstatus)
        print(self.pcolor.tipcolor + 'end brew update' + self.pcolor.endcolor)

    @property
    def pwd(self):
        """
        Protected Password
        """
        return self.pwd_md5

    @pwd.setter
    def pwd(self, password):
        """
        Change the Protected Password
        """
        self.pwd_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()

    def getpassword(self):
        """
        Access to the administor with enter password
        """
        password = getpass("Enter your password: ")
        counter = 1
        while counter < 3:
            if self.pwd_md5 != hashlib.md5(password.encode('utf-8')).hexdigest():
                print(self.pcolor.warningcolor +\
                        "Wrong Password!" +\
                        self.pcolor.endcolor)
                password = getpass("Try again: ")
                counter += 1
            else:
                return password
        if counter >= 3:
            raise ValueError("Wrong Password!")

    def __updateyum(self):
        """
        Manage Linux builtin tools.
        """
        print(self.pcolor.warningcolor + 'yum updating...' + self.pcolor.endcolor)
        password = self.getpassword()
        echo = ['echo']
        echo.append(password)
        if pf.linux_distribution()[1] > '21':
            cmd = 'sudo -S dnf -y upgrade'
        else:
            cmd = 'sudo -S yum -y update'
        pipein = sp.Popen(echo, stdout=sp.PIPE)
        pipeout = sp.Popen(cmd.split(), stdin=pipein.stdout, stdout=sp.PIPE)
        self.__outstatus(pipeout.stdout)
        print(self.pcolor.tipcolor + 'end yum update' + self.pcolor.endcolor)

    def updategit(self, gitpath=None):
        """
        Update git projects in default path.
        If gitpath is given, Update project in the given path.
        """
        if gitpath:
            self.path = gitpath
        else:
            if pf.system() == 'Darwin':
                self.path = '/Users/edony/coding'
            if pf.system() == 'Linux':
                self.path = '/home/edony/code/github'

        self.__gitrepos()
        print(self.pcolor.tipcolor + 'updating git...' + self.pcolor.endcolor)
        print('>> to update git repositories path: %s'%self.path)
        print('>> to update %d repositroies'%len(self.gitdir))
        for direction in self.gitdir:
            os.chdir(direction)
            status = os.popen('git pull')
            print(self.pcolor.warningcolor + direction + self.pcolor.endcolor)
            self.__outstatus(status)
        print(self.pcolor.tipcolor + 'update git repositroies finished' + self.pcolor.endcolor)

    def updatehg(self, hgpath=None):
        """
        Update hg projects in default path.
        If hgpath is given, Update project in the given path.
        """
        if hgpath:
            self.path = hgpath
        self.__gitrepos()
        print(self.pcolor.tipcolor + 'updating hg...' + self.pcolor.endcolor)
        print('>> to update hg repositories path: %s'%self.path)
        print('>> to update %d repositroies'%len(self.hgdir))
        for direction in self.hgdir:
            os.chdir(direction)
            status = os.popen('hg update')
            print(self.pcolor.warningcolor + direction + self.pcolor.endcolor)
            self.__outstatus(status)
        print(self.pcolor.tipcolor + 'update hg repositroies finished' + self.pcolor.endcolor)

    @staticmethod
    def cleanup():
        """
        Manage to Cleanup System Cache and Old Kernel
        """
        if pf.system() == 'Linux':
            os.system('dnf clean all')
            clean_kernel = KC(1)
            clean_kernel.main()
        elif pf.system() == 'Darwin':
            os.system('brew cleanup')

    def default(self):
        """
        Manage system with default operation, update builtin tools and projects.
        """
        print("system info: " + pf.system())
        if pf.system() == 'Darwin':
            self.__updatebrew()
        elif pf.system() == 'Linux':
            self.__updateyum()
        self.updategit()

    def help(self, attr=None):
        """
        Class UpdateSys Attributes Documents Details
        """
        if attr:
            if attr in UpdateSys.__dict__.keys():
                print(self.__getattribute__(attr).__doc__)
            else:
                print(self.pcolor.warningcolor +\
                        "ERROR" +\
                        self.pcolor.endcolor +\
                        ": You get wrong attribute for help.")
                print(self.pcolor.tipcolor+\
                        "They must in: " +\
                        self.pcolor.endcolor)
                for item in UpdateSys.__dict__.keys():
                    if re.match("^_+/w+", item):
                        continue
                    else:
                        print(item + ",",)
        else:
            print(self.__doc__)

    def cmd_parser(self):
        """
        Command Line Parser:
        Usage updategit [-l | -m | -g | -gp]...[argv]
        default : Update System and Repositories
        -l      : Manage Linux Builtin Tools
        -m      : Manage MacOS Builtin Tools
        -g      : Update projects in default diection or given path
        -c      : Cleanup the old kernel in Fedora system or cleanup Mac brew pkg
        -p      : Specific the Path to Manage
        -a   : Get Details in Document of Attributes
        """
        self.parser.add_argument('-l', '--linux',
                                 action='store_true',
                                 help='Manage and Update Linux Builtin Tools')
        self.parser.add_argument('-m', '--mac',
                                 action='store_true',
                                 help='Manage and Update Mac Brewed Tools')
        self.parser.add_argument('-g', '--git',
                                 action='store_true',
                                 help='Update Git Repositories in Default Path')
        self.parser.add_argument('-H', '--hg',
                                 action='store_true',
                                 help='Update HG Repositories in Default Path')
        self.parser.add_argument('-c', '--cleanup',
                                 dest='c',
                                 action='store_true',
                                 help='Cleanup All Repositories Cache and Old Kernel in System')
        self.parser.add_argument('-p', '--path',
                                 nargs='*',
                                 help='Repository Path Where to Management')
        self.parser.add_argument('-a', '--attribute',
                                 nargs='+',
                                 help='Help for Details On Component')

    def main(self):
        """
        Updatesys management main pipe to execution.
        """
        self.cmd_parser()
        if self.parser.parse_args().linux:
            self.__updateyum()
        elif self.parser.parse_args().mac:
            self.__updatebrew()
        elif self.parser.parse_args().git:
            print("system info: " + pf.system())
            self.updategit()
        elif self.parser.parse_args().hg:
            print("system info: " + pf.system())
            self.updatehg()
        elif self.parser.parse_args().path:
            print("system info: " + pf.system())
            for path in self.parser.parse_args().path:
                self.updategit(path)
            for path in self.parser.parse_args().path:
                self.updatehg(path)
        elif self.parser.parse_args().c:
            UpdateSys.cleanup()
        elif self.parser.parse_args().attribute:
            for attr in self.parser.parse_args().attribute:
                self.help(attr)
        else:
            self.default()

if __name__ == '__main__':
    import sys
    UPDATE = UpdateSys()
    UPDATE.pcolor.new = '\033[0;36m'
    print(UPDATE.pcolor.new, sys.version, UPDATE.pcolor.endcolor)
    UPDATE.main()
