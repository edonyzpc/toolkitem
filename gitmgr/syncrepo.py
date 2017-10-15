#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
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
 # Last modified: 2017-02-28 23:38
 #
 # Filename: syncrepo.py
 #
 # Description: All Rights Are Reserved
 # This tool aim to keep forked github repository update with upstream repository
 #
"""

#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np
import os
import sys
import logging
from logging.config import fileConfig
try:
    from subprocess import getstatusoutput
except ImportError:
    from commands import getstatusoutput

class SyncUpstreamRepo(object):
    """Sync source code from upstream in forked repository
       e.g. Github Project
    """
    def __init__(self, path, upstream_url):
        self.repo_path = os.path.realpath(path)
        self.upstream_url = upstream_url
        self.remotelist = None
        self.log_config = 'log_config.ini'
        fileConfig(self.log_config)
        self.logger = logging.getLogger()

    def _is_crt_dir(self):
        if os.path.realpath(os.path.curdir) == self.repo_path:
            return True
        return False

    def is_git_repo(self):
        """check if path is a git repository"""
        if not self._is_crt_dir():
            self.logger.warning("Not a correct repository path")
            return False
        gitstatus = 'git status'
        status, logs = getstatusoutput(gitstatus)
        self.logger.info(logs)
        self.logger.info("git status return code: %d", status)
        if status == 0:
            return True
        else:
            return False

    def _remote_list(self):
        if not self._is_crt_dir():
            self.logger.warning("current dir: %s, repo dir: %s", os.getcwd(), self.repo_path)
            return
        if not self.is_git_repo():
            self.logger.warning("not a correct repository")
            return

        gitremote = 'git remote -v'
        status, remotelist = getstatusoutput(gitremote)
        self.logger.info(remotelist)
        if status == 0:
            self.remotelist = remotelist.split('\n')

    def has_upstream(self):
        if not self._is_crt_dir():
            self.logger.warning("current dir: %s, repo dir: %s", os.getcwd(), self.repo_path)
            return False

        self._remote_list()
        self.logger.info(self.remotelist)
        if self.remotelist is not None:
            for item in self.remotelist:
                if self.upstream_url in item:
                    return True
        else:
            return False

    def add_upstrem(self):
        if not self._is_crt_dir():
            return False

        if not self.has_upstream():
            gitremoteadd = 'git remote add upstream ' + self.upstream_url
            _, logs = getstatusoutput(gitremoteadd)
            self.logger.info(logs)

    def sync_upstream(self, branch='master'):
        if not self._is_crt_dir():
            self.logger.warning("changing the current directory into %s", self.repo_path)
            os.chdir(self.repo_path)

        if not self.is_git_repo():
            self.logger.warning("current directory is %s", os.getcwd())
            self.logger.warning("Not a git repository")
            return

        if not self.has_upstream():
            self.logger.warning("add upstream %s into repository", self.upstream_url)
            self.add_upstrem()

        gitfetch = 'git fetch upstream'
        gitcheckout = 'git checkout ' + branch
        gitmerge = 'git merge upstream/' + branch
        gitpush = 'git push origin ' + branch
        exec_cmds = [gitfetch, gitcheckout, gitmerge, gitpush]
        for cmd in exec_cmds:
            status, logs = getstatusoutput(cmd)
            self.logger.info(logs)
            if status != 0:
                break

def syncrepo(path, upstream, branch='master'):
    syncer = SyncUpstreamRepo(path, upstream)
    syncer.sync_upstream(branch)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please specific the path and upstream URL")
    else:
        syncrepo(sys.argv[1], sys.argv[2])
