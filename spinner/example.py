#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import time

from spinner import make_spin, BOX1


@make_spin(BOX1, "Download youtube video")
def demo():
    time.sleep(5)


if __name__ == '__main__':
    print("Downloading a youtube video, it would cost much time.")
    demo()
    #print("Download success!")
