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
from functools import reduce
from multiprocessing.pool import Pool
from dirlist import DirList

class FilesLine(DirList):
    """generate the line number of files located in directory
    """
    def __init__(self, directory, CPURES=8):
        super(FilesLine, self).__init__(directory)
        self.filesline = 0
        self.MAX_RES = CPURES

    def _count_filelines(self, file):
        with open(file, 'rb') as filebuf:
            return len(filebuf.readlines())

    def _adder(self, a, b):
        return a + b

    def sum_lines(self, SPEEDUP=True):
        filesname = []
        for item_dir in self.dirlist.keys():
            for item_file in self.dirlist[item_dir][1]:
                filesname.append(item_dir + '/' + item_file)

        if SPEEDUP:
            with Pool(self.MAX_RES) as res_pool:
                return reduce(self._adder, res_pool.map(self._count_filelines, filesname))
        else:
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
    print("==== Not Speedup ====")
    print(time.time())
    tmp1.sum_lines(SPEEDUP=False)
    print(time.time())
    print("==== Do Speedup ====")
    print(time.time())
    tmp1.sum_lines()
    print(time.time())
#comment this line to test with __main__ """
