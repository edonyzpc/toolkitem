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
import platform as pf
import subprocess as sp
import argparse as ap
from packages.filesline.filesline import FileLine as fl
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

    Usage updategit [-l | -m | -g | -c | -p | -attr]...[argv]
    default : Update System and Repositories
    -l      : Manage Linux Builtin Tools
    -m      : Manage MacOS Builtin Tools
    -g      : Update projects in default diection or given path
    -c      : Cleanup the old kernel in Fedora system or cleanup Mac brew pkg
    -p      : Specific the Path to Manage
    -attr   : Get Details in Document of Attributes
    """
    def __init__(self, path=None):
        """
        Initialize the path of to be managed projects, it takes path parameter.
        The path has its default direction with different platform.
        """
        self.gitdir = []
        self.pcolor = PyColor()
        self._password_linux = '/home/edony/code/github/toolkitem/updatesys/pwd.pyo'
        if path:
            self.path = path
        if pf.system() == 'Darwin':
            self.path = '/Users/edony/coding/'
        if pf.system() == 'Linux':
            self.path = '/home/edony/code/github/'

    def __gitrepos(self):
        """
        Find the git repositroies in the self.path
        """
        rec = []
        gitdir = []
        fl.dirlist(self.path, rec)
        for direction in rec:
            tmp = direction.split('/')
            self.__delblank(tmp)
            if '.git' in tmp:
                tmpgitdir = self.__gitroot(tmp)
                gitdir.append(tmpgitdir)
        self.gitdir = set(gitdir)

    @staticmethod
    def __gitroot(gitpath):
        """
        Get the git project root path
        """
        root = ''
        for item in gitpath:
            if item == '.git':
                break
            else:
                root += '/'+item
        return root

    @staticmethod
    def __delblank(linels):
        """
        Delete the blank line in lines list
        """
        for item in linels:
            if item == '':
                linels.remove(item)

    def __outstatus(self, outstatus_file):
        """
        Print highlight the executed cmd results.
        """
        for line in outstatus_file.readlines():
            if line == '':
                break
            elif 'error:' in line.split()\
                    or 'warning:' in line.split()\
                    or 'fatal:' in line.split():
                print self.pcolor.warningcolor + line + self.pcolor.endcolor
            else:
                print line

    def __updatebrew(self):
        """
        Mange MacOS builtin tools.
        """
        print self.pcolor.warningcolor + 'brew update' + self.pcolor.endcolor
        brewstatus = os.popen('brew update')
        for line in brewstatus:
            if line == '':
                break
            elif 'error:' in line.split()\
                    or 'warning:' in line.split()\
                    or 'fatal:' in line.split():
                print self.pcolor.warningcolor + line + self.pcolor.endcolor
            else:
                print line
        print self.pcolor.tipcolor + 'end brew update' + self.pcolor.endcolor

    @property
    def pwd(self):
        """
        Protected Password
        """
        return self._password_linux

    @pwd.setter
    def pwd(self, password_path):
        """
        Change the Protected Password
        """
        self._password_linux = password_path

    def __updateyum(self):
        """
        Manage Linux builtin tools.
        """
        print self.pcolor.warningcolor + 'yum update' + self.pcolor.endcolor
        pwf = open(self.pwd)
        password = pwf.readline().rstrip()
        pwf.close()
        echo = ['echo']
        echo.append(password)
        if pf.linux_distribution()[1] > '21':
            cmd = 'sudo -S dnf -y update'
        else:
            cmd = 'sudo -S yum -y update'
        pipein = sp.Popen(echo, stdout=sp.PIPE)
        pipeout = sp.Popen(cmd.split(), stdin=pipein.stdout, stdout=sp.PIPE)
        for line in pipeout.stdout.readlines():
            if line == '':
                break
            elif 'error:' in line.split()\
                    or 'warning:' in line.split()\
                    or 'fatal:' in line.split():
                print self.pcolor.warningcolor + line + self.pcolor.endcolor
            else:
                print line
        print self.pcolor.tipcolor + 'end yum update' + self.pcolor.endcolor

    def updategit(self, gitpath=None):
        """
        Update projects in default path.
        If gitpath is given, Update project in the given path.
        """
        if gitpath:
            self.path = gitpath
        else:
            if pf.system() == 'Darwin':
                self.path = '/Users/edony/coding/'
            elif pf.system() == 'Linux':
                self.path = '/home/edony/code/github/'

        self.__gitrepos()
        print 'update git path %s'%self.path
        print 'update %d repositroies'%len(self.gitdir)
        for direction in self.gitdir:
            os.chdir(direction)
            status = os.popen('git pull')
            print self.pcolor.warningcolor,
            print direction,
            print self.pcolor.endcolor
            self.__outstatus(status)
        print self.pcolor.tipcolor,
        print 'update git repositroies finished',
        print self.pcolor.endcolor

    def main(self):
        """
        Manage system builtin tools and update projects.
        """
        print "system info: " + pf.system()
        if pf.system() == 'Darwin':
            self.__updatebrew()
        elif pf.system() == 'Linux':
            self.__updateyum()
        print 'git repositroies path: %s'%self.path
        self.__gitrepos()
        print 'update %d repositroies'%len(self.gitdir)
        self.updategit()

    def help(self, attr=None):
        """
        Class UpdateSys Attributes Documents Details
        """
        if attr:
            print self.__getattribute__(attr).__doc__
        else:
            print self.__doc__

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
        -attr   : Get Details in Document of Attributes
        """
        parser = ap.ArgumentParser()
        parser.add_argument('-l', '--linux', action='store_true',
                            help='Manage and Update Linux Builtin Tools')
        parser.add_argument('-m', '--mac', action='store_true',
                            help='Manage and Update Mac Brewed Tools')
        parser.add_argument('-g', '--git', action='store_true',
                            help='Update Git Repositories in Default Path')
        parser.add_argument('-c', '--cleanup', dest='c', action='store_true',
                            help='Update Git Repositories in Default Path')
        parser.add_argument('-p', nargs='*', help='Path Where to Management')
        parser.add_argument('-attr', '--attribute', nargs='+',
                            help='Help for Details On Component')
        args = parser.parse_args()
        if args.linux:
            self.__updateyum()
        elif args.mac:
            self.__updatebrew()
        elif args.git:
            print "system info: " + pf.system()
            if args.path:
                for path in args.path:
                    self.updategit(path)
            else:
                self.updategit()
        elif args.c:
            if pf.system() == 'Linux':
                os.system('dnf clean all')
                clean_kernel = KC(1)
                clean_kernel.main()
            elif pf.system() == 'Darwin':
                os.system('brew cleanup')
        elif args.attribute:
            for attr in args.attribute:
                self.help(attr)
        else:
            self.main()

if __name__ == '__main__':
    UPDATE = UpdateSys()
    UPDATE.cmd_parser()
#    if len(sys.argv) == 1:
#        UPDATE.main()
#    elif len(sys.argv) > 1:
#        UPDATE.cmd_exec()
