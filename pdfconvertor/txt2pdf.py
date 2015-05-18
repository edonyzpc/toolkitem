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
 # Last modified: 2015-05-15 14:41
 #
 # Filename: pdf2txt.py
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

from packages.pyfpdf.fpdf import FPDF

class PDF:
    """
    Formatting the pdf file.
    """
    def __init__(self, font):
        self.font = font
        self.pdf = FPDF()
        self.pdf.add_font('fireflysung', '', '/usr/share/fonts/fireflysung/fireflysung.ttf', uni=True)

    def header(self, title):
        """
        Write title into pdf.
        """
        self.pdf.set_font(self.font, '', 18)
        # Move to the right
        #print self.pdf.h
        #self.pdf.cell(80, 210)
        # Title
        self.pdf.set_y(self.pdf.h/2)
        self.pdf.cell(0, 10, title, 0, 0, 'C')
        # Line break
        #self.pdf.ln(1)

    def footer(self, font=None):
        # Position at 1.5cm from bottom
        self.pdf.set_y(-35)
        if font:
            self.pdf.set_font(font, 'I', 8)
        else:
            self.pdf.set_font(self.font, '', 8)
        # Page number
        self.pdf.cell(0, 10, str(self.pdf.page_no())+'\n', 'T', 0, 'C')

    def body(self, font=None):
        if font:
            self.pdf.add_font(font, '', font+'.ttf', uni=True)
            self.pdf.set_font(font, '', 16)
        else:
            self.pdf.add_font(self.font, '', self.font+'.ttf', uni=True)
            self.pdf.set_font(self.font, '', 16)

class Txt2Pdf(PDF):
    """
    PDF Convertor for text files.
    """
    def __init__(self, font, txt_files):
        PDF.__init__(self, font)
        self.files = txt_files
        self.convert_one_pdf = 1  # default to convert txt_files into one pdf file
        self.file_buf = {}

    def convertor(self):
        for file in self.files:
            file_open = open(file)
            self.file_buf[file] = file_open.readlines()
            file_open.close()
        if self.convert_one_pdf:
            self.pdf.add_page('', 'A4', True)
            pdf_name = raw_input('\aPDF file name: ')
            self.header(pdf_name)
            self.pdf.add_page('', 'A4', True)
            counter = 0
            file_counter = 0
            for file in self.files:
                file_counter += 1
                for line in self.file_buf[file]:
                    self.body()
                    self.pdf.write(12, line)
                    counter += 1
                    if counter == 60:
                        self.footer()
                        self.pdf.add_page('', 'A4', True)
                        counter = 0
                if counter != 60 and file_counter < len(self.files):
                    self.footer()
                    self.pdf.add_page('', 'A4', True)
            self.pdf.output(pdf_name + '.pdf')
        else:
            for file in self.files:
                counter = 0
                for line in self.file_buf[file]:
                    self.pdf.add_page('', 'A4', True)
                    self.pdf.header(file.split('.')[0])
                    self.pdf.add_page('', 'A4', True)
                    self.body()
                    self.pdf.write(12, line)
                    counter += 1
                    if counter == 60:
                        self.footer()
                        self.pdf.add_page('', 'A4', True)
                        counter = 0
                self.pdf.output(file.split('.')[0] + '.pdf')
            

        
if __name__ == '__main__':
    pdf = FPDF()
    pdf.add_page('','A4',True)
    pdf.add_font('fireflysung', '', '/usr/share/fonts/fireflysung/fireflysung.ttf', uni=True)
    pdf.set_font('fireflysung', '', 16)
    pdf.write(10, u'edony糯米517吃货节!\n')
    pdf.ln(10)
    pdf.output('test.pdf', 'F')
    pdf2 = PDF('fireflysung', 'test2.pdf')
    pdf2.pdf.add_page('', 'A4', True)
    #pdf2.add_font('fireflysung', '', '/usr/share/fonts/fireflysung/fireflysung.ttf', uni=True)
    pdf2.header('TEST2.PDF')
    #pdf2.footer('Arial')
    pdf2.pdf.add_page('', 'A4', True)
    pdf2.body()
    pdf2.pdf.write(20, u'edony糯米517吃货节!\n')
    pdf2.pdf.ln(20)
    pdf2.footer('Arial')
    pdf2.pdf.output('test2.pdf', 'F')

    # TODO(edony):class Txt2Pdf test
