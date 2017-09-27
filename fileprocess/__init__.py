import os
import sys

sys.path.append(os.path.split(os.path.realpath(__file__))[0])
__all__ = ['dirlist', 'DirList']

from dirlist import DirList
