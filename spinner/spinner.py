#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import sys
import time
from functools import wraps
from concurrent.futures import ThreadPoolExecutor

try:
    SPINSTR = unicode
except NameError as namerr:
    SPINSTR = str

BOX1 = u'⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
BOX2 = u'⠋⠙⠚⠞⠖⠦⠴⠲⠳⠓'
BOX3 = u'⠄⠆⠇⠋⠙⠸⠰⠠⠰⠸⠙⠋⠇⠆'
BOX4 = u'⠋⠙⠚⠒⠂⠂⠒⠲⠴⠦⠖⠒⠐⠐⠒⠓⠋'
BOX5 = u'⠁⠉⠙⠚⠒⠂⠂⠒⠲⠴⠤⠄⠄⠤⠴⠲⠒⠂⠂⠒⠚⠙⠉⠁'
BOX6 = u'⠈⠉⠋⠓⠒⠐⠐⠒⠖⠦⠤⠠⠠⠤⠦⠖⠒⠐⠐⠒⠓⠋⠉⠈'
BOX7 = u'⠁⠁⠉⠙⠚⠒⠂⠂⠒⠲⠴⠤⠄⠄⠤⠠⠠⠤⠦⠖⠒⠐⠐⠒⠓⠋⠉⠈⠈'
SPIN1 = u'|/-\\'
SPIN2 = u'◴◷◶◵'
SPIN3 = u'◰◳◲◱'
SPIN4 = u'◐◓◑◒'
SPIN5 = u'▉▊▋▌▍▎▏▎▍▌▋▊▉'
SPIN6 = u'▌▄▐▀'
SPIN7 = u'╫╪'
SPIN8 = u'■□▪▫'
SPIN9 = u'←↑→↓'
DEFAULT = BOX1


class Spinner(object):
    def __init__(self, words, frames=DEFAULT):
        self.frames = frames
        self.length = len(frames)
        self.position = 0
        self.words = words

    def current(self):
        return self.frames[self.position]

    def next(self):
        current_frame = self.current()
        self.position = (self.position + 1) % self.length
        return SPINSTR(current_frame)

    def reset(self):
        self.position = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(func, *args, **kwargs)
                while future.running():
                    sys.stdout.flush()
                    print(SPINSTR("\r{0}    {1} ").format(self.words, self.next()), end="")
                    sys.stdout.flush()
                    time.sleep(0.15)
                print("\r{0}.....{1}".format(self.words, "[Done]"), end="\n")
            return future.result()
        return wrapper



def spinner(words="", spin_style=DEFAULT, ending="\n"):
    spinner = Spinner(spin_style)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(func, *args, **kwargs)

                while future.running():
                    sys.stdout.flush()
                    print(SPINSTR("\r{0}    {1} ").format(words, spinner.next()), end="")
                    sys.stdout.flush()
                    time.sleep(0.15)
                print("\r{0}.....{1}".format(words, "[Done]"), end=ending)
            return future.result()
        return wrapper
    return decorator
