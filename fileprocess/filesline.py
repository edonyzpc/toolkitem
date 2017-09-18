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
        # TODO(edony): optimize algorithm of sum_lines method
        filesname = []
        for item_dir in self.dirlist.keys():
            for item_file in self.dirlist[item_dir][1]:
                filesname.append(item_dir + '/' + item_file)
        for filename in filesname:
            with open(filename, 'rb') as filebuf:
                self.filesline += len(filebuf.readlines())

        return self.filesline

""" comment this line to test with __main__
if __name__ == "__main__":
    import time
    tmp = DirList('/Users/edony/coding/toolkitem')
    #print(tmp.dirlist)
    #print(sys.path)
    #print(os.path.split(os.path.realpath(__file__)))
    tmp1 = FilesLine('/Users/edony/coding/toolkitem')
    print(tmp1.dirlist)
    print(time.time())
    tmp1.sum_lines()
    print(time.time())
comment this line to test with __main__ """
