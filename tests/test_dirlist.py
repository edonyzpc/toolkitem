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

    def test__listdir(self):
        with pytest.raises(Exception):
            tmp = DirList(None)

    def test__listdir_exclude_dir(self):
        curdir = os.path.split(os.path.realpath(__file__))[0]
        tmp = DirList(curdir, excludedir=curdir)
        assert tmp.dirlist == {}

    def test_getattr(self):
        assert DirList.getattr(__file__) == 'FILE'
        assert DirList.getattr(os.path.split(os.path.realpath(__file__))[0]) == 'DIR'
        assert DirList.getattr('/dev/ttyxxxx')

    def test_shadow_key(self):
        assert DirList.shadow_key('123') == b'fKHdCVgwViFR1Cj7ANzZtlrO1zzGZLwK9eKQmM3eXes='
        assert DirList.shadow_key(b'123') == b'fKHdCVgwViFR1Cj7ANzZtlrO1zzGZLwK9eKQmM3eXes='
        assert DirList.shadow_key(123) == None

    def test_enc_bytes(self):
        pwd_bytes = DirList.enc_bytes('123', b'123')
        assert DirList.dec_bytes('123', pwd_bytes) == b'123'
