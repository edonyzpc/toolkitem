#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2017-03-14 22:49
 #
 # Filename: test_syncrepo.py
 #
 # Description: All Rights Are Reserved
 #
"""
import sys
sys.path.append('./')
import pytest
import os
try:
    from commands import getstatusoutput
except ImportError:
    from subprocess import getstatusoutput
from gitmgr import syncrepo
from gitmgr import SyncUpstreamRepo

class TestClass:
    def test_syncrepo(self):
        os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        syncrepo('./TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.system('rm -rf ../TPM2.0-TSS')