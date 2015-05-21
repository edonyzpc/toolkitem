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
 # Last modified: 2015-05-21 16:33
 #
 # Filename: ZJUcrawler.py
 #
 # Description: All Rights Are Reserved
 #
 # A web crawler based on Scrapy and BeautifulSoup4 to get updated career info from ZJU job web site.
"""
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

#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np
import html2text
from bs4 import BeautifulSoup as BS
import requests
import os
import re

class ZJUCareer(object):
    def __init__(self):
        self.url_main = u'http://www.career.zju.edu.cn/ejob/login_student.do'
        self.url_main_id = 'con'
        self.url_main_class = 'con list2'
        self.url_main_li = 'ul'
        self.tabs_num = 8
        
    def crawler(self):
        source = requests.get(self.url_main)
        char_encode = source.encoding
        if source:
            soup = BS(source.content)
            file_buf = open("buf", 'w')
            for i in range(self.tabs_num):
                #ID = self.url_main_id + str(i)
                info_tmp = soup.findAll("a")
                tmp_str = str(info_tmp)
                file_buf.write(tmp_str)
            file_buf.close()
            os.system("dos2unix -o buf")
        else:
            raise ValueError("Can not access the WEB: %s"%self.url_main)

    def info_filter(self):
        file_buf = open('buf', 'r')
        file_info = open('career', 'w')
        for line in file_buf.readlines():
            file_info.write(re.sub('.*title="', '', line))
        file_info.close()
        file_buf.close()


if __name__ == '__main__':
    test = ZJUCareer()
    test.crawler()
    test.info_filter()


