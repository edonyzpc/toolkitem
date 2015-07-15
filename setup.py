#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2015-07-15 16:44
 #
 # Filename: setup.py
 #
 # Description: All Rights Are Reserved
 #
"""
import os
from setuptools import setup
from setuptools import find_packages

def read(readme):
    return open(os.path.join(os.path.dirname(__file__), readme)).read()

setup(
        name="toolkitem",
        version="0.1.2",
        author="Edony Murphy",
        author_email="edonyzpc@gmail.com",
#        contact="Edony Murphy",
#        contact_email="edonyzpc@gmail.com",
        description="personal tool for daily code",
        license="MIT",
        keywords="\033[0;31m file manager, \033[0;32m GUI boost::python,"
                  "\033[0;33m project code management\033[0m",
        url="https://github.com/edonyM/toolkitem",
        packages=find_packages(),
        long_description=read('README.md'),
        install_requires=[
            "html2text>=2015.6.6",
            "BeautifulSoup4>=4.3.2",
            "requests>=2.7.0",
            "getpass",
            "calendar",
            "time",
            "argparse",
            "platform",
            "hashlib",
            "subprocess",
            "functools",
            ],
        )
