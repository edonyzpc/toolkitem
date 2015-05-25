#!/usr/bin/env python
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
import sys
import re

class ZJUCareer(object):
    def __init__(self):
        self.url_main = u'http://www.career.zju.edu.cn/ejob/login_student.do'
        self.url_sub = u'http://www.career.zju.edu.cn/ejob/'
        self.url_main_id = 'con'
        self.url_main_class = 'con list2'
        self.url_main_li = 'ul'
        self.tabs_num = 8
        self.char_encode = ''
        
    def crawler(self):
        source = requests.get(self.url_main)
        self.char_encode = source.encoding
        reload(sys)
        sys.setdefaultencoding(self.char_encode)
        if source:
            soup = BS(source.content, from_encoding=self.char_encode)
            file_buf = open("buf", 'w')
            info_tmp = soup.findAll("a")
            file_buf.write(str(info_tmp))
            file_buf.close()
            os.system("dos2unix -o buf")
        else:
            raise ValueError("Can not access the WEB: %s"%self.url_main)

    def info_filter(self):
        file_buf = open('buf', 'r')
        file_info = open('career', 'w')
        for line in file_buf.readlines():
            #tmp_line = re.sub('.*title="', '', line)
            pattern = re.compile('.*href="(.*)" style.*title="(.*)".*')
            tmp_line = pattern.search(line)
            if tmp_line:
                group = tmp_line.groups()
                file_info.write(group[1]+'\n')
                file_info.write(self.url_sub + group[0]+'\n')
                file_info.write("\n")
            else:
                continue
        file_info.close()
        file_buf.close()


if __name__ == '__main__':
    os.system('mv career career_old')
    test = ZJUCareer()
    test.crawler()
    test.info_filter()
    print "\aIf the web site got ^M, you need remove it for better reading\n"
    opt = raw_input('REMOVE or NOT?\n')
    if opt == 'Y' or opt == 'y':
        opt = os.system('vim career')
        if opt == 0:
            opt1 = os.system('vim -d career career_old')
            if opt1 == 0:
                os.system('mv career career_old')



