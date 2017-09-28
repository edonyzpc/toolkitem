from __future__ import print_function
import sys
import os
import pytest
sys.path.append('./')

from fileprocess.filesline import FilesLine
from fileprocess.filesline import _filecounter

class TestClass(object):
    def test_FilesLine(self):
        curdir = os.path.split(os.path.realpath(__file__))[0]
        tmp = FilesLine(curdir)

    def test_sum_lines(self):
        curdir = os.path.split(os.path.realpath(__file__))[0]
        tmp = FilesLine(curdir)
        tmp.sum_lines()

    def test_filecounter(self):
        _filecounter(__file__)

    def test_nospeedup_sum_lines(self):
        curdir = os.path.split(os.path.realpath(__file__))[0]
        tmp = FilesLine(curdir)
        tmp.sum_lines(SPEEDUP=False)
