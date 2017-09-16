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
 # Last modified: 2017-09-15 15:33
 #
 # Filename: filesline.py
 #
 # Description: All Rights Are Reserved
 #
"""
import sys
import os
from dirlist import DirList

class FilesLine(DirList):
    """generate the line number of files located in directory
    """
    def __init__(self, directory):
        super(FilesLine, self).__init__(directory)
        self.filesline = 0

    def sum_lines(self):
        pass

if __name__ == "__main__":
    tmp = DirList('/Users/edony/coding/toolkitem')
    #print(tmp.dirlist)
    #print(sys.path)
    #print(os.path.split(os.path.realpath(__file__)))
    tmp1 = FilesLine('/Users/edony/coding/toolkitem')
    print(tmp1.dirlist)
