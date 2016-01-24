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
 # Last modified: 2016-01-24 23:19
 #
 # Filename: pymail.py
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
from getpass import getpass
import poplib

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

class mail(object):
    def __init__(self, host='pop3.163.com', username='edonyzpc@163.com', pwd=None):
        self.host = host # 'pop3.163.com'
        self.username = username # 'edonyzpc@163.com'
        self.pwd = getpass("Email password: ")
        # create pop3 object and connect the server
        self.connect_server = poplib.POP3(self.host)
        # set the debug module to get the interactive info
        self.connect_server.set_debuglevel(1)
        # send the user name
        self.connect_server.user(self.username)
        # send the password
        print(self.pwd)
        self.connect_server.pass_(self.pwd)

    def mails_info(self):
        # fetch the info of mails in the mail server
        return self.connect_server.stat() # mail_info = (`number of mails`, `total bytes`)

    def header_info(self, id=1):
        # get the head of the mail
        for i in range(1, self.mail_info()[0]+1): # id of mails start from 1
            mail_list = self.connect_server.top(i, 0)
            print(mail_list)

    def mail_list(self):
        # list the id and the bytes of emails
        return self.connect_server.list()

    def mail_detail(self):
        # fetch the whole mail
        download = self.connect_server.retr(1) # download=(`return status`, `details line by line`)
        if download[0]:
            print(download[1])

    def quit():
        # stop the connection
        self.connect_server.quit()

if __name__ == '__main__':
    mail = mail()
    print(mail.mails_info())
    print(mail.mail_list())

