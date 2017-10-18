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
        os.system('cp gitmgr/log_config.ini ./')
        syncrepo('./TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir("../")

    def test_SyncUpstreamRepo(self):
        #os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        #os.system('cp gitmgr/log_config.ini ./')
        syncer = SyncUpstreamRepo('./TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        syncer.sync_upstream()
        os.chdir("../")

    def test_is_git_repo(self):
        #os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        #os.system('cp gitmgr/log_config.ini ./')
        syncer = SyncUpstreamRepo('./TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir('./TPM2.0-TSS')
        assert syncer.is_git_repo()
        os.chdir('../')
        #os.system('rm -rf ../TPM2.0-TSS ../log_config.ini')

    def test_is_git_repo_fail_dir(self):
        #os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        #os.system('cp gitmgr/log_config.ini ./')
        syncer = SyncUpstreamRepo('./TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir('.')
        assert not syncer.is_git_repo()
        os.system('rm -rf ./TPM2.0-TSS ./log_config.ini')

    def test_is_git_repo_fail_not_git_repo(self):
        curdir = os.path.realpath(os.path.curdir)
        os.system('cp gitmgr/log_config.ini ./')
        os.chdir('/tmp/')
        os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        os.chdir(curdir)
        syncer = SyncUpstreamRepo('/tmp/TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir('/tmp/TPM2.0-TSS')
        os.system('mv .git git.bak')
        assert not syncer.is_git_repo()
        os.system('mv git.bak .git')
        os.chdir(curdir)

    def test_has_upstream(self):
        curdir = os.path.realpath(os.path.curdir)
        #os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        os.system('cp gitmgr/log_config.ini ./')
        syncer = SyncUpstreamRepo('/tmp/TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir('/tmp/TPM2.0-TSS')
        os.system('git remote remove upstream')
        assert not syncer.has_upstream()
        os.chdir(curdir)
        #os.system('rm -rf ../TPM2.0-TSS ../log_config.ini')

    def test_has_no_upstream(self):
        curdir = os.path.realpath(os.path.curdir)
        print("##########1" + curdir)
        #os.system('git clone https://edonyM:123456789@github.com/edonyM/TPM2.0-TSS.git')
        os.system('cp gitmgr/log_config.ini ./')
        syncer = SyncUpstreamRepo('/tmp/TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir('/tmp/TPM2.0-TSS')
        syncer.add_upstream()
        assert syncer.has_upstream()
        os.chdir(curdir)

    def test_add_upstream(self):
        curdir = os.path.realpath(os.path.curdir)
        print("##########2" + curdir)
        os.system('cp gitmgr/log_config.ini ./')
        syncer = SyncUpstreamRepo('/tmp/TPM2.0-TSS', 'https://github.com/01org/tpm2-tss.git')
        os.chdir(curdir)
        assert not syncer.add_upstream()
        os.system('rm -rf /tmp/TPM2.0-TSS ./log_config.ini')
