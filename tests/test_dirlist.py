from __future__ import print_function
import sys
import os
import pytest
sys.path.append('./')

from fileprocess.dirlist import DirList


class TestClass(object):
    def test_DirList(self):
        curdir = os.path.split(os.path.realpath(__file__))[0]
        tmp = DirList(curdir)
