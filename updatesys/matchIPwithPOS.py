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
 # Last modified: 2015-11-20 20:50
 #
 # Filename: matchIPwithPOS.py
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
import json
#import chardet
if sys.version.startswith('3.'):
    from urllib.request import urlopen
else:
    from urllib import urlopen

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

class IP2Pos(object):
    """
    Call Sina IP API To Match The IP And Physical Position.
    """
    def __init__(self, ipadd=None):
        # default URL is not good codec for default IP matching.
        self.ip_api_url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip="
        self.ip = ipadd
        self.data = {}
    
    def matchip2pos(self):
        if self.ip:
            response = urlopen(self.ip_api_url + self.ip)
        else:
            response = urlopen(self.ip_api_url.split('?')[0])
        json_string = str(response.read(), encoding='utf-8')
        #coding = chardet.detect(json_string)['encoding'] if chardet.detect(json_string)['encoding'] != 'ascii' else 'utf-8'
        result_data = json.loads(json_string, encoding='utf-8')
        return result_data

    def match_default(self):
        self.data['Default'] = self.matchip2pos()

    def match_taobao(self):
        # taobao.com not support the default IP query
        self.ip_api_url = 'http://ip.taobao.com//service/getIpInfo.php?ip='
        self.data['TB'] = self.matchip2pos()

    def match_ipapi(self):
        self.ip_api_url = 'http://ip-api.com/json/'
        self.data['IA'] = self.matchip2pos()

if __name__ == "__main__":
    ip2add = IP2Pos('222.205.15.30')
    ip2add.matchip2pos()
    ip2add.match_taobao()
    ip2add.match_ipapi()
    print(ip2add.data)
    ip2add_ = IP2Pos()
    #ip2add_.matchip2pos()
    ip2add_.match_ipapi()
    print(ip2add_.data)
