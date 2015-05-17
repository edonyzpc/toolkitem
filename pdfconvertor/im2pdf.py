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
 # Last modified: 2015-05-17 19:09
 #
 # Filename: im2pdf.py
 #
 # Description: All Rights Are Reserved
 #
Reference from im2pdf.
# im2pdf.py
------------

#!/usr/bin/env python
# coding: UTF-8

__description__ = 'Tool to convert images to pdf and unite them.'
__author__ = '@tkmru'
__version__ = '0.1'
__date__ = '2014/12/29'
__minimum_python_version__ = (2, 7, 6)
__maximum_python_version__ = (3, 4, 2)
__copyright__ = 'Copyright (c) @tkmru'
__license__ = 'MIT License'

import PIL
import PIL.Image
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import argparse


def convert(input_file, output_file):
    im = PIL.Image.open(input_file)
    im.save(output_file, 'PDF', resoultion = 100.0)
    print('completed.')
    print(input_file + ' --> ' + output_file)


def union(input_files, output_file):
    output = PdfFileWriter()

    for input_file in input_files:
        if input_file.endswith('.pdf'):
            input = PdfFileReader(open(input_file, 'rb'))
            num_pages = input.getNumPages()

            for i in range(0, num_pages):
                output.addPage(input.getPage(i))

        else: # input_file isn't pdf ex. jpeg, png  
            im = PIL.Image.open(input_file)
            input_file_pdf = input_file.split('.')[0]+'.pdf'
            im.save(input_file_pdf, 'PDF', resoultion = 100.0)

            input = PdfFileReader(open(input_file_pdf, 'rb'))
            num_pages = input.getNumPages()

            for i in range(0, num_pages):
                output.addPage(input.getPage(i))

            os.remove(input_file_pdf)


    with open(output_file, 'wb') as outputStream:
        output.write(outputStream)

    print('completed.')
    print('Union of some file is ' + output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert image to pdf and union them.')
    parser.add_argument('-o', '--output', default='output.pdf')
    parser.add_argument('-i', '--input', nargs='*', required=True)
    parser.add_argument('-v', '--version', action='version', version=__version__)

    args = vars(parser.parse_args())

    if len(args['input']) == 1:
        convert(args['input'][0], args['output'])

    elif len(args['input']) > 1:
        union(args['input'], args['output'])

    else:
        pass
------------
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

import PIL
import PIL.Image
from packages.PyPDF2.PyPDF2 import PdfFileWriter, PdfFileReader
import os
import argparse

class Img2Pdf:
    def __init__(self, img_files, add_positions, out_pdf_name):
        self.imgs = img_files
        self.add_position = add_positions
        self.out_pdf_name = out_pdf_name
        self.img_pdf_file = []

    def img2pdf(self):
        for img in self.imgs:
            print img
            im = PIL.Image.open(img)
            input_file_pdf = img.split('.')[0]+'.pdf'
            self.img_pdf_file.append(input_file_pdf)
            im = im.convert('RGB')
            im.save(input_file_pdf, 'PDF', resoultion = 100.0)
            #im.close()

    def convertor(self):
        merge_img2pdf = PdfFileWriter()
        for img_pdf in self.img_pdf_file:
            merge_tmp = PdfFileReader(open(img_pdf, 'rb'))
            num_pages = merge_tmp.getNumPages()
            for i in range(num_pages):
                merge_img2pdf.addPage(merge_tmp.getPage(i))
            os.remove(img_pdf)
        with open(self.out_pdf_name, 'wb') as outputStream:
            merge_img2pdf.write(outputStream)



if __name__ == '__main__':
    images = ['img1.png', 'img2.png']
    pdf = 'imgtest.pdf'
    test = Img2Pdf(images, 1, pdf)
    test.img2pdf()
    test.convertor()
