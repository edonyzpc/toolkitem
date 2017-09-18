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
 # Last modified: 2017-08-02 20:57
 #
 # Filename: dirlist.py
 #
 # Description: All Rights Are Reserved
 #
"""
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
try:
    import cPickle as pickle
    def bstr(*kargs, **kwargs):
        """ bytes convertor function of python2.x
        """
        return str(*kargs, **kwargs)
except ImportError:
    import pickle
    def bstr(*kargs, **kwargs):
        """ bytes convertor function of python3.x with default utf-8 encoding
        """
        return bytes(encoding='utf-8', *kargs, **kwargs)

class DirList(object):
    """ list the directory recursively and
        get all directories including all sub-directories
    """

    def __init__(self, rootpath):
        """ initialize `DirList' with root `rootpath'
        """
        self.root = rootpath
        self.dirlist = {}
        # buffer for multiprocess speedup directory walking
        self._dl_buf = []
        self._listdir()
        # choose highest pickle protocol type
        self.protocol = pickle.HIGHEST_PROTOCOL
        self.__shawodkey = b''

    def _listdir(self, path=None):
        """ list root path recursively including sub-directories
        """
        if self.root is None:
            if path is not None:
                for root_, dir_, file_ in os.walk(path):
                    dir_ctx = []
                    dir_ctx.insert(0, file_)
                    dir_ctx.insert(0, dir_)
                    buf_dl = {}
                    buf_dl[root_] = dir_ctx
                    self._dl_buf.insert(0, buf_dl)
            else:
                raise Exception("Error DirList class initialize")
        else:
            for root_, dir_, file_ in os.walk(self.root):
                dir_ctx = []
                dir_ctx.insert(0, file_)
                dir_ctx.insert(0, dir_)
                self.dirlist[root_] = dir_ctx

    def _slistdir(self):
        """ speedup list root path recursively including sub-directories
        """
        # TODO
        pass

    @staticmethod
    def getattr(path):
        """ fetch the `path' attribute
        """
        types = ['DIR', 'FILE', 'LINK', 'OTHERS']
        if os.path.isdir(path):
            return types[0]
        elif os.path.isfile(path):
            return types[1]
        elif os.path.islink(path):
            return types[2]
        return types[3]

    @staticmethod
    def shadow_key(key):
        """ shadow the key
        """
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                         salt=b'', iterations=100000,
                         backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(key))

    @staticmethod
    def enc_bytes(pwd, ctx_bytes):
        """ encrypt python bytes with pwd by using cryptography package
        """
        shadowkey = DirList.shadow_key(pwd)
        return Fernet(shadowkey).encrypt(ctx_bytes)

    @staticmethod
    def dec_bytes(pwd, ctx_bytes):
        """ decrypt python bytes with pwd by using cryptography package
        """
        shadowkey = DirList.shadow_key(pwd)
        return Fernet(shadowkey).decrypt(ctx_bytes)

    def serial(self, pwd, storage_file):
        """ serialize the instance
        """
        # dump the object
        bytestream = pickle.dumps(self, self.protocol)
        # do some encryption
        enc_bytes = self.enc_bytes(bstr(pwd), bytestream)
        with open(storage_file, 'wb') as filebuf:
            filebuf.write(enc_bytes)

    @staticmethod
    def unserail(pwd, storage_file):
        """ unserialize the instance
        """
        with open(storage_file, 'rb') as filebuf:
            bytestream_ = filebuf.read()
            bytestream = DirList.dec_bytes(bstr(pwd), bytestream_)
            print(bytestream)
            return pickle.loads(bytestream)


if __name__ == "__main__":
    OBJ = DirList("/Users/edony/coding/toolkitem")
    OBJ.serial('123!QAZ', "./buf.bin")
    del OBJ
    OBJ = DirList.unserail('123!QAZ', "./buf.bin")
    print(OBJ.dirlist)
