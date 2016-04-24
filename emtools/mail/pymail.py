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
import sys
import os
from getpass import getpass
import poplib
from progressive.bar import Bar
from time import sleep
import tkinter as tk

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
        # connect to the mail server
        self.host = host # 'pop3.163.com'
        self.username = username # 'edonyzpc@163.com'
        self.pwd = getpass("Email password: ")
        # create pop3 object and connect the server
        self.connect_server = poplib.POP3(self.host)
        # set the debug module to get the interactive info
        #self.connect_server.set_debuglevel(1) # this is optional
        # send the user name
        self.connect_server.user(self.username)
        # send the password
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

    def quit(self):
        # stop the connection
        self.connect_server.quit()

class warn_gui(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.lbl = tk.Label(self.root, text="You Got New Mails\nPlease Check It!")
        self.btn = tk.Button(self.root, text="Ok", relief=tk.SUNKEN, activebackground='green', command=self.root.destroy)
        self.lbl.pack()
        self.btn.pack()

def playsound(file="./3.wav"):
    if sys.platform == "darwin":
        os.system("open /Applications/iTunes.app ./3.wav")
        # TODO
        # Driver development for MacOS
    elif sys.platform == "linux":
        # TODO
        # Driver development for Linux
        pass

def check_mail(step=3): # check emails per `step` minutes
    pymail = mail()
    info = pymail.mails_info()
    sleep_time = step/100
    #sleep_time = 0.02 # for test
    try:
        while 1:
            bar = Bar(max_value=10, fallback=True, filled_color=1, title='Check Emails...')
            bar.cursor.clear_lines(2)
            bar.cursor.save()
            for i in range(11):
                sleep(sleep_time)
                # We restore the cursor to saved position before writing
                bar.cursor.restore()
                # Now we draw the bar
                bar.draw(value=i)
            if pymail.mails_info()[0] >= info[0]:
                info = pymail.mails_info()
                win = tk.Tk()
                win.title("Mail Checking")
                win.resizable(False, False)
                win.update()
                scrn_width, scrn_height = win.maxsize()
                win.geometry('200x70+%d+%d'%((scrn_width-200)/2,(scrn_height-65)/2))
                warn_gui(win)
                playsound()
                win.mainloop()
                print('\033[0;32mChecked...\033[0m')
                pymail.quit()
                return
    except(KeyboardInterrupt, SystemExit):
        pymail.quit()

if __name__ == '__main__':
    #mail = mail()
    #print(mail.mails_info())
    #print(mail.mail_list())
    check_mail()
