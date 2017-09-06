# encoding: utf-8
from __future__ import print_function
import sys
sys.path.append('./')
import time
import pytest
from spinner.spinner import spinner, BOX1, Spinner

try:
    SPINSTR = unicode
except:
    SPINSTR = str

class TestClass(object):
    def test_spinner(self):
        @spinner("Download youtube video")
        def demo():
            time.sleep(5)

        print("Downloading a youtube video, it would cost much time.")
        demo()

    def test_Spinner(self):
        spin = Spinner("test_Spinner")
        assert SPINSTR(spin.current()) == u'⠋'
        spin.next()
        assert spin.position == 1
        spin.reset()
        assert spin.position == 0
