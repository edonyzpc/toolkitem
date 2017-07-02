from __future__ import print_function
import sys
sys.path.append('./')
import time
import pytest
from spinner.spinner import make_spin, BOX1, Spinner


class TestClass(object):
    def test_make_spin(self):
        @make_spin(BOX1, "Download youtube video")
        def demo():
            time.sleep(5)

        print("Downloading a youtube video, it would cost much time.")
        demo()

    def test_Spinner(self):
        spin = Spinner(BOX1)
        assert spin.current() == u'⠋'
        assert spin.next() == u'⠙'
        spin.reset()
        assert spin.position == 0
