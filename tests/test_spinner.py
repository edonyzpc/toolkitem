from __future__ import print_function
import sys
sys.path.append('./')
import time
from spinner.spinner import make_spin, BOX1


class TestClass(object):
    def test_make_spin(self):
        @make_spin(BOX1, "Download youtube video")
        def demo():
            time.sleep(5)

        print("Downloading a youtube video, it would cost much time.")
        demo()
