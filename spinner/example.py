#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import time

from spinner import spinner, BOX1, BOX2, Spinner


@spinner("Download youtube video")
def demo():
    time.sleep(5)

@Spinner("Fetching spider", BOX2)
def demo1():
    time.sleep(3)

if __name__ == '__main__':
    print("Downloading a youtube video, it would cost much time.")
    demo()
    demo1()
    #print("Download success!")
