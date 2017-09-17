__all__ = ['dirlist', 'DirList']
import sys

if sys.version_info.major == 3:
    from dirlist.dirlist import DirList
elif sys.version_info.major == 2:
    from dirlist import DirList
