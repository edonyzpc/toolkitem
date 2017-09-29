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

    def test_err_DirList(self):
        with pytest.raises(Exception):
            tmp = DirList('')

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
        os.system('ln -sf ' + __file__ + ' xxtestlnk')
        assert DirList.getattr('xxtestlnk') == "LINK"
        os.system('rm -rf xxtestlnk')

    def test_shadow_key(self):
        assert DirList.shadow_key('123') == b'fKHdCVgwViFR1Cj7ANzZtlrO1zzGZLwK9eKQmM3eXes='
        assert DirList.shadow_key(b'123') == b'fKHdCVgwViFR1Cj7ANzZtlrO1zzGZLwK9eKQmM3eXes='
        assert DirList.shadow_key(123) == None

    def test_enc_bytes(self):
        pwd_bytes = DirList.enc_bytes('123', b'123')
        assert DirList.dec_bytes('123', pwd_bytes) == b'123'

    def test_serial(self):
        pwd = '123'
        filename = 'test.test'
        curdir = os.path.split(os.path.realpath(__file__))[0]
        filename = curdir + '/' + filename
        tmp = DirList(curdir)
        tmp.serial(pwd, filename)
        assert os.path.isfile(filename)
        os.system('rm -rf ' + filename)

    def test_unserail(self):
        pwd = '123'
        filename = 'test.test'
        curdir = os.path.split(os.path.realpath(__file__))[0]
        filename = curdir + '/' + filename
        tmp = DirList(curdir)
        tmp.serial(pwd, filename)
        tmp1 = DirList.unserial(pwd, filename)
        os.system('rm -rf ' + filename)
