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
 # Last modified: 2015-05-28 22:20
 #
 # Filename: extractor.py
 #
 # Description: All Rights Are Reserved
 #
 # ******
 # Extract the specific content from text with the given keys.
"""
import os
import re
class Extractor(object):
    """
    Extract the specific content with keys.
    """
    def __init__(self, keys, extracted_file, output_file=None, flag=None):
        if type(keys) is list:
            self.keys = keys
        elif type(keys) is str:
            self.keys =[keys]
        else:
            raise ValueError("Wrong Key type")
        if output_file:
            self.output_file = output_file
        else:
            self.output_file = 'EXTRACT'
        if flag:
            self.flag = [0, 0]  #flag are controlling add the keys into write file
        else:
            self.flag = flag
        self.pattern = Extractor.re_pattern(self.keys)
        self.extracted_file = extracted_file

    @staticmethod
    def re_pattern(keys):
        if len(keys) > 2:
            raise ValueError("The keys are too much, simplify them less than 2.\n")
        regular_expression = keys[0] + '(?P<con>.*)'
        if len(keys) == 2:
            regular_expression += keys[1]
        return re.compile(regular_expression)

    def parser(self):
        with open(self.output_file, 'w') as out:
            with open(self.extracted_file) as exfile:
                for line in exfile.readlines():
                    g = self.pattern.search(line)
                    if g:
                        if self.flag[0]:
                            print('test')
                            out.write(self.keys[0])
                        out.write(g.group('con'))
                        if self.flag[1]:
                            out.write(self.keys[1])
                        out.write('\n')
        print('Finish Extract')

if __name__ == '__main__':
    tmp = Extractor('http:', 'career_old')
    tmp.flag = [1,0]
    tmp.parser()
