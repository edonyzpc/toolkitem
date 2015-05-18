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
 # Last modified: 2015-05-18 11:36
 #
 # Filename: pdfconvertor.py
 #
 # Description: All Rights Are Reserved
 #
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
from im2pdf import Img2Pdf
from txt2pdf import Txt2Pdf
from packages.PyPDF2.PyPDF2 import PdfFileWriter, PdfFileReader
import os

class PdfConvertor:
    """
    Convertor for converting different types files into pdf.

    For now, types in [`*.txt`, `*.md`, `*.rst`, `*.jpg`, `*.png`] are supported.
    """
    def __init__(self, files):
        self.files = files
        self.img_files = []
        self.txt_files = []

    def type_filter(self):
        """
        Tell the files with type.
        """
        for file in self.files:
            if file.split('.')[1] in ['jpg', 'png']:
                self.img_files.append(file)
            if file.split('.')[1] in ['txt', 'md', 'rst']:
                self.txt_files.append(file)
    def img_convert(self):
        imgpdf = Img2Pdf(self.img_files, 1, 'img.pdf')
        imgpdf.img2pdf()
        imgpdf.convertor()

    def txt_convert(self):
        txtpdf = Txt2Pdf('fireflysung', self.txt_files)
        txtpdf.convertor()

    def merge_all(self):
        merge_pdf = PdfFileWriter()
        merge_tmp_img = PdfFileReader(open('img.pdf', 'rb'))
        merge_tmp_txt = PdfFileReader(open('txt.pdf', 'rb'))
        img_page_num = merge_tmp_img.getNumPages()
        txt_page_num = merge_tmp_txt.getNumPages()
        for i in range(img_page_num):
            merge_pdf.addPage(merge_tmp_img.getPage(i))
        for i in range(txt_page_num):
            merge_pdf.addPage(merge_tmp_txt.getPage(i))
        os.remove('img.pdf')
        os.remove('txt.pdf')
        with open('merger_pdf.pdf', 'wb') as outputstream:
            merge_pdf.write(outputstream)



if __name__ == '__main__':
    files = ['txt1.txt', 'txt2.txt','img1.png', 'img2.png']
    tmp = PdfConvertor(files)
    tmp.type_filter()
    tmp.img_convert()
    tmp.txt_convert()
    tmp.merge_all()
