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
#from packages.filesline.browser import getfiles as GF
#from packages.filesline.getdirections import GetDirections as GD

import os
import re
import hashlib
from getpass import getpass
import platform as pf
import subprocess as sp
import argparse as ap
from packages.filesline.browser import getdirections as GD
from kernelclean import KernelClean as KC
from weather import autoweather as autoweat

__version__ = '2.0.0'
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
        self.pwd_sha512 = 'a071944ce3ecfc42ea3e17cd666afb66bfd32b14f0bb03b61\
4665f66b888b62b9a4308268baa522804572cff30b816c299d73b1a97fc3a017f2bc94fa9adb1fc'
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
        if self:
            for line in outstatus_file.readlines():
                if isinstance(line, bytes):
                    line = line.decode()
                print(line.rstrip())

    def __updatebrew(self):
        """
        Mange MacOS builtin tools.
        """
        print(self.pcolor.warningcolor + 'brew updating' + self.pcolor.endcolor)
        brewstatus = os.popen('brew update')
        self.__outstatus(brewstatus)
        print(self.pcolor.tipcolor + 'end brew update' + self.pcolor.endcolor)

    def upbrew(self):
        """
        Protected Function For MacOS Builtin Manage Tools.
        """
        self.__updatebrew()

    def getpassword(self):
        """
        Access to the administor with enter password
        """
        password = getpass("Enter your password: ")
        counter = 1
        while counter < 3:
            if isrightpwd(password, self.pwd_sha512):
                return password
            else:
                print(self.pcolor.warningcolor +\
                        "Wrong Password!" +\
                        self.pcolor.endcolor)
                password = getpass("Try again: ")
                counter += 1
        if counter >= 3:
            raise ValueError("Wrong Password!")

    def __updateyum(self):
        """
        Manage Linux builtin tools.
        """
        print(self.pcolor.warningcolor + 'Packages Updating ...' + self.pcolor.endcolor)
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
        print(self.pcolor.tipcolor + 'End Packages Update' + self.pcolor.endcolor)

    def uplinux(self):
        """
        Protected Function For Linux Builtin Manage Tool
        """
        self.__updateyum()

    def updategit(self, gitpath=None):
        """
        Update git projects in default path.
        If gitpath is given, Update project in the given path.
        """
        if gitpath:
            # Input Check For Avoiding `self.path` equals `/home/edony/.vim/bundle//nerdtree`
            if gitpath.endswith('/'):
                self.path = gitpath[:-1]
            else:
                self.path = gitpath
        else:
            if pf.system() == 'Darwin':
                self.path = '/Users/edony/coding'
            if pf.system() == 'Linux':
                self.path = '/home/edony/code/github'
        self.__gitrepos()
        print(self.pcolor.warningcolor + 'Updating GitHub Repository ...' + self.pcolor.endcolor)
        print('>> to update GitHub repositories path: %s'%self.path)
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
            # Input Check For Avoiding `self.path` equals `/home/edony/.vim/bundle//vim-19`
            if hgpath.endswith('/'):
                self.path = hgpath[:-1]
            else:
                self.path = hgpath
        self.__gitrepos()
        print(self.pcolor.tipcolor + 'Updating Bitbucket ...' + self.pcolor.endcolor)
        print('>> to update Bitbucket repositories path: %s'%self.path)
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
        -a      : Get Details in Document of Attributes
        -v      : Tool and System Information
        -w      : Get Local Weather In 24 Hours
        """
        self.parser.add_argument('-l', '--linux',
                                 action=LinuxExecAction, nargs=0,
                                 help='Manage and Update Linux Builtin Tools')
        self.parser.add_argument('-m', '--mac',
                                 action=MacExecAction, nargs=0,
                                 help='Manage and Update Mac Brewed Tools')
        self.parser.add_argument('-g', '--git',
                                 action=GitExecAction, nargs='*',
                                 help='Update Git Repositories in Default Path')
        self.parser.add_argument('-H', '--hg',
                                 action=HgExecAction, nargs='*',
                                 help='Update HG Repositories in Default Path')
        self.parser.add_argument('-c', '--cleanup',
                                 action=CleanupExecAction, nargs=0,
                                 help='Cleanup All Repositories Cache and Old Kernel in System')
        self.parser.add_argument('-p', '--path',
                                 action=PathExecAction, nargs='+',
                                 help='Repository Path Where to Management')
        self.parser.add_argument('-a', '--attribute',
                                 action=AttrExecAction, nargs='+',
                                 help='Help for Details On Component')
        self.parser.add_argument('-v', '--version',
                                 action='version',
                                 version="\033[32mTool Version:" +\
                                         __version__ + ", " +\
                                         pf.system() + ":" + pf.uname().release + ", " +\
                                         "Python:" + sys.version.split('(')[0] + "\033[0m",
                                 help='Tool and System Information')
        self.parser.add_argument('-w', '--weather', nargs=0,
                                 action=WeatherExecAction,
                                 help='Get Local Weather In 24 Hours')

    def main(self):
        """
        Updatesys management main pipe to execution.
        """
        self.cmd_parser()
        if len(sys.argv) < 2:
            self.default()
        else:
            self.parser.parse_args()

class WeatherExecAction(ap.Action):
    """
    Action of Getting Weather Information In 24h.
    """
    def info(self):
        self.__doc__ += "Action of Getting Weather Information In 24h."

    def action(self):
        self.info()
        autoweat()

    def __call__(self, parser, namespace, values, option_string=None):
        self.action()
        setattr(namespace, self.dest, autoweat)

class LinuxExecAction(ap.Action):
    """
    Action of Linux Builtin Packages Management.
    """
    def info(self):
        self.__doc__ += "Action of Linux Builtin Packages Management."

    def action(self):
        self.info()
        update = UpdateSys()
        return update.uplinux()

    def __call__(self, parser, namespace, values, option_string=None):
        val = self.action()
        setattr(namespace, self.dest, val)

class MacExecAction(ap.Action):
    """
    Action of MacOS Builtin Packages Management.
    """
    def info(self):
        self.__doc__ += "Action of MacOS Builtin Packages Management."

    def action(self):
        self.info()
        update = UpdateSys()
        return update.upbrew()

    def __call__(self, parser, namespace, values, option_string=None):
        #print(self.namespace)
        val = self.action()
        setattr(namespace, self.dest, val)

class GitExecAction(ap.Action):
    """
    Action of Git Repositories Management.
    """
    def info(self):
        self.__doc__ += "Action of Git Repositories Management."

    def action(self):
        self.info()
        print("system info: " + pf.system())
        update = UpdateSys()
        if len(sys.argv) > 2:
            result = []
            for path in sys.argv[2:]:
                result.append(update.updategit(path))
            return result
        else:
            return update.updategit()

    def __call__(self, parser, namespace, values, option_string=None):
        val = self.action()
        setattr(namespace, self.dest, val)

class HgExecAction(ap.Action):
    """
    Action of Hg Repositories Management.
    """
    def info(self):
        self.__doc__ += "Action of Hg Repositories Management."

    def action(self):
        self.info()
        print("system info: " + pf.system())
        update = UpdateSys()
        if len(sys.argv) > 2:
            result = []
            for path in sys.argv[2:]:
                result.append(update.updatehg(path))
            return result
        else:
            return update.updatehg()

    def __call__(self, parser, namespace, values, option_string=None):
        val = self.action()
        setattr(namespace, self.dest, val)

class PathExecAction(ap.Action):
    """
    Action of Identified Path Including Git And Hg Repositories Management.
    """
    def info(self):
        self.__doc__ += "Action of Identified Path Including \
                             Git And Hg Repositories Management."

    def action(self):
        self.info()
        print("system info: " + pf.system())
        update = UpdateSys()
        result = []
        if len(sys.argv) > 2:
            for path in sys.argv[2:]:
                result.append(update.updategit(path))
                result.append(update.updatehg(path))
        else:
            result.append(update.updategit())
            result.append(update.updatehg())
        return result

    def __call__(self, parser, namespace, values, option_string=None):
        val = self.action()
        setattr(namespace, self.dest, val)

class CleanupExecAction(ap.Action):
    """
    Action of OS Cleanup.
    """
    def info(self):
        self.__doc__ += "Action of OS Cleanup."

    def action(self):
        self.info()
        update = UpdateSys()
        update.cleanup()

    def __call__(self, parser, namespace, values, option_string=None):
        self.action()
        setattr(namespace, self.dest, self.action)

class AttrExecAction(ap.Action):
    """
    Action of Getting UpdateSys Attributes Informations.
    """
    def info(self):
        self.__doc__ += "Action of Getting UpdateSys Attributes Informations."

    def action(self):
        self.info()
        update = UpdateSys()
        if len(sys.argv) > 2:
            result = []
            for attr in sys.argv[2:]:
                print("UpdateSys Class Method <{}> DOC:".format(attr))
                result.append(update.help(attr))
            return result

    def __call__(self, parser, namespace, values, option_string=None):
        val = self.action()
        setattr(namespace, self.dest, val)

def isrightpwd(pwd, encrypted_pwd):
    """
    Make Sure The Password(pwd) Is The Right One.
    Judge By The SHA512 Encrypted Password(encrypted_pwd).
    """
    if hashlib.sha512(pwd.encode('utf-8')).hexdigest() == encrypted_pwd:
        return True
    else:
        return False

if __name__ == '__main__':
    import sys
    UPDATE = UpdateSys()
    UPDATE.main()
