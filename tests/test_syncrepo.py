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

class TestClass:
    def test_has_local_upstream(self):
        assert False == syncrepo.has_local_upstream()

    def test_sync_up2master(self):
        with pytest.raises(Exception):
            syncrepo.sync_up2master()

    def test_exec_cmd(self):
        stat, output = syncrepo.exec_cmd('echo hello')
        assert stat == 0 and output == 'hello'

    def test_print_cmd_result(self):
        stat, output = getstatusoutput('echo "test print_cmd_result"')
        syncrepo.print_cmd_result('echo "test print_cmd_result"', stat, output)
        with pytest.raises(Exception):
            stat, output = getstatusoutput('python xxxxx')
            syncrepo.print_cmd_result('python xxxxx', stat, output)

    def test_add_upstream(self):
        os.chdir("/home")
        with pytest.raises(Exception):
            syncrepo.add_upstream('https://github.com/edonyM/toolkitem.git')

    def test_sync_up2master(self):
        with pytest.raises(Exception) as err:
            syncrepo.sync_up2master()
