#!/usr/bin/python

"""This is a IMA hash log checking tool.
# Jobs:
#   1. check if the hash value extend into PCR10 is correct
#   2. ensure the hash value of checked file being the same with the value record in IMA log
# Algorithm reference from https://sourceforge.net/p/linux-ima/wiki/Home/#ima-measurements
"""

from __future__ import print_function
import os
try:
    from commands import getstatusoutput
except ImportError:
    from subprocess import getstatusoutput
from multiprocessing import Process
from hashlib import sha256
import binascii


__version__ = '1.1'
__author__ = 'z00369817'

class PyColor(object):
    """Colorful print for terminal
    """
    def __init__(self):
        self.self_doc = r"""
        STYLE: \033['display model';'foreground';'background'm
        DETAILS:
        FOREGROUND        BACKGOUND       COLOR
        ---------------------------------------
        30                40              black
        31                41              red
        32                42              green
        33                43              yellow
        34                44              blue
        35                45              purple
        36                46              cyan
        37                47              white
        DISPLAY MODEL    DETAILS
        -------------------------
        0                default
        1                highlight
        4                underline
        5                flicker
        7                reverse
        8                non-visiable
        e.g:
        \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
        \033[0m         <!--set all into default-->
        """
        self.warningcolor = '\033[0;31m'
        self.tipcolor = '\033[0;32m'
        self.endcolor = '\033[0m'
        self._newcolor = ''
    @property
    def new(self):
        """
        Customized Python Print Color.
        """
        return self._newcolor
    @new.setter
    def new(self, color_str):
        """
        New Color.
        """
        self._newcolor = color_str
    def disable(self):
        """
        Disable the Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''


# IMA measurement log path
IMA_LOG = '/sys/kernel/security/ima/ascii_runtime_measurements'
# PCR id label for identify
PCR_LABL = ['PCR_0' + str(item) for item in range(10)]
PCR_LABL.append('PCR_10')
PCR_LABL = [item + ':' for item in PCR_LABL]
# color print for logging output
COLOR = PyColor()
COLOR.new = '\033[0;33m'

def init_tss():
    """
    Initialize the Trusted computing Software Stack.
    1. Run bash command `resourcemgr > /dev/null` in backgroud \
       to enable tpm2.0-tools running
    2. Run bash command `tpm2_listpcrs > PCRLIST` to write value of \
       PCR_00 ~ PCR_10 to file named PCRLIST
    """
    cmd_res = 'resourcemgr > /dev/null'
    cmd_ls = 'tpm2_listpcrs > PCRLIST'
    p_res = Process(target=os.system, args=(cmd_res,))
    p_res.daemon = True
    p_res.start()
    stat_ls, output_ls = getstatusoutput(cmd_ls)
    if stat_ls != 0:
        raise Exception('`tpm2_listpcrs > PCRLIST` failed\n')
    return output_ls


def get_pcrs():
    """
    Get PCRs value into diction like {'PCR_00:':'ffca0238xxxxxxxxxxxxxxxxxxxxxxxx',...}
    """
    fd_pcr = open('PCRLIST', 'r')
    lines = fd_pcr.readlines()
    fd_pcr.close()
    pcrs_str = [''.join([line for line in lines if \
               line.startswith(label)][1].rstrip().split()[1:]) \
               for label in PCR_LABL]
    pcrs = dict(zip(PCR_LABL, pcrs_str))
    return pcrs


def get_hashlog():
    """
    Get log buff of IMA Runtime Measurements which writed into \
    file name '/sys/kernel/security/ima/ascii_runtime_measurements'
    """
    try:
        fd_ima = open(IMA_LOG, 'r')
    except IOError:
        raise IOError('Fail to open {}'.format(IMA_LOG))
    log_buf = [(item.split()[1],
                item.split()[3],
                item.split()[4]+item.rstrip().split(item.split()[4])[1])
               for item in fd_ima.readlines()]
    fd_ima.close()
    return log_buf


def gen_filehash(filename):
    """
    Generate the value of file data.
    """
    sha256_val = sha256()
    try:
        file_buff = open(filename, 'rb')
        sha256_val.update(file_buff.read())
    except IOError as err:
        print(COLOR.new + '    [WARNING]:' + str(err) + ' (skip)')
    return sha256_val.hexdigest()


def gen_pcrhash(log_value, pcr_value):
    """
    PCR Extend:  value(PCR_10) = sha256(PCR_10_old + filehash_in_log)
    NOTE:        log_value and pcr_value are not string, so they cannot work as the input
                 parameter of sha256().
    Algorithm:   1. convert the input value into bit list
                 2. convert bit list into char list
                 3. concatenate the char list to string as the input parameter of sha256()
                 4. calculate the hexdigest of the input string
    """
    s_tmp = pcr_value + log_value
    hex_ls = [s_tmp[item*2:item*2+2] for item in range(64)]
    bin_ls = ['0'*(8 - len(bin(int(item, 16))[2:])) \
             + bin(int(item, 16))[2:] for item in hex_ls]
    return sha256(''.join([chr(int(item, 2)) for item in bin_ls])).hexdigest()


def gen_pcr10():
    """
    According to the template hash value, generate the value of PCR_10\
    which indicate the integrity.
    """
    logs = get_hashlog()
    pcr10 = '0' * 64
    for log in logs:
        pcr10 = gen_pcrhash(log[0], pcr10)
    return pcr10


def hex2str(hex_str):
    """
    Convert hexadecimal bunch into identical string.
    """
    hex_len = len(hex_str)
    if hex_len % 2 != 0:
        raise Exception("Wrong Hex string!")
    char_ls = [chr(int(ch, base=16)) for ch in \
              [hex_str[item*2:item*2+2] for item in range(hex_len/2)]]
    return ''.join(char_ls)


def str2hex(ch_str):
    """
    Convert string into identical hexadecimal bunch.
    """
    return binascii.b2a_hex(ch_str)


def ima_template_hash(filedata_hash, filename_hint):
    """
    According to file data hash value and file name, that should be fill in 256 bytes,\
    generate template hash value.
    """
    hint_hex_filename = str2hex(filename_hint)
    hint_hex_filename_len = len(hint_hex_filename)
    hint_hex = hint_hex_filename + ('0' * (512 - hint_hex_filename_len))
    sha_str = hex2str(filedata_hash + hint_hex)
    return sha256(sha_str).hexdigest()


def boot_aggregate_hash():
    """
    According to the value of PCR_00 ~ PCR_07, generate boot_aggregate value.
    """
    pcrs_dict = get_pcrs()
    pcrs = [pcrs_dict[label] for label in PCR_LABL]
    pcr_tmp = pcrs[0]
    for pcr_id in range(1, 8):
        pcr_tmp += pcrs[pcr_id]
    return sha256(hex2str(pcr_tmp)).hexdigest()


def printer(level):
    """Decorator with parameter for logging the info of execution method.
    """
    def wrapper(func):
        """Closure method
        """
        def inner(*args, **kwargs):
            """Addtional logging print
            """
            print('[{level}]: start {func}'\
                    .format(level=level, func=' '.join(func.__name__.split('_'))))
            return func(*args, **kwargs)
        return inner
    return wrapper


@printer('INFO')
def check_boot_aggregate(logged_bootaggregate_hash):
    """Check the coherence between boot aggregate value and related value recorded in IMA log.
    """
    boot_flag = 0
    ## boot_aggregate hash checking
    boot_hash = boot_aggregate_hash()
    if boot_hash != logged_bootaggregate_hash:
        boot_flag += 1
        raise Exception(COLOR.warningcolor + 'boot_aggregate hash not identical\n' +
                        'check boot aggregate. (failed)' + COLOR.endcolor)
    else:
        print(COLOR.tipcolor + '    boot_aggregate value check (passed).' + COLOR.endcolor)
    return boot_flag


@printer('INFO')
def check_filedata_hash(file_hint, filedata_logged_hash):
    """Check the coherence between file data hash value and related value recorded in IMA log.
    """
    file_flag = 0
    for idx, filename in enumerate(file_hint[1:]):
        hash_value = gen_filehash(filename)
        if hash_value != filedata_logged_hash[idx + 1]:
            file_flag += 1
            print(COLOR.new + \
                  '    [WARNING]:file hash value is not identical: \'{}\''\
                  .format(filename) + ' (skip)' + COLOR.endcolor)
        else:
            #print(color.tipcolor + '    {} (pass)'.format(filename) + color.endcolor)
            pass
    if file_flag == 0:
        print(COLOR.tipcolor + '    All file data hash value check. (passed)' + COLOR.endcolor)
    return file_flag


@printer('INFO')
def check_template_hash(template_logged_hash, filedata_logged_hash, file_hint):
    """Check the coherence between template hash value and related value recorded in IMA log.
    """
    temp_flag = 0
    for idx, template_hash in enumerate(template_logged_hash):
        hash_value = ima_template_hash(filedata_logged_hash[idx], file_hint[idx])
        if hash_value != template_hash:
            temp_flag += 1
            print(COLOR.new + \
                  '    [WARNING]:file value of tempalte hash is not identical: \'{}\''\
                  .format(file_hint[idx]) + ' (skip)' + COLOR.endcolor)
        else:
            #print(color.tipcolor + '    {} (pass)'.format(filename) + color.endcolor)
            pass
    if temp_flag == 0:
        print(COLOR.tipcolor + '    All file template hash value checked. (passed)' \
              + COLOR.endcolor)

    return temp_flag


@printer('INFO')
def check_pcr10_value(pcr10):
    """Check the coherence between Register value of PCR_10 and related value recorded in IMA log.
    """
    pcr_flag = 0

    if pcr10 != gen_pcr10():
        pcr_flag += 1
        raise Exception(COLOR.warningcolor + 'PCR10 not identical, and IMA log has been modified!\n' + 
                        'check pcr10 value. (failed)' + COLOR.endcolor)
    else:
        print("\033[0;36m    PCR_10: {}".format(pcr10) + COLOR.endcolor)
        print(COLOR.tipcolor +
              '    PCR_10 value in TPM Register is identical with IMA measurement. (passed)' +
              COLOR.endcolor)

    return pcr_flag


@printer('INFO')
def check_hash_alg(ima_log):
    """Check the IMA Measurement with sha256.
    """
    hash_alg_flag = 0
    filedata_hash_alg = sum([1 for item in ima_log if len(item[1]) == 64])
    template_hash_alg = sum([1 for item in ima_log if len(item[0]) == 64])
    if filedata_hash_alg == len(ima_log) and template_hash_alg == len(ima_log):
        print(COLOR.tipcolor +
              '    check IMA Measurement hash algorithm is sha256. (passed)' +
              COLOR.endcolor)
    else:
        hash_alg_flag += 1
        raise Exception(COLOR.warningcolor + 'check IMA Measurement hash algorithm is sha256. (failed)' +
	                COLOR.endcolor)


@printer('INFO')
def print_ima_integrity(flag):
    """Print IMA Intergrity Measurement checking info.
    """
    print(COLOR.tipcolor + '    IMA Integrity Measurement checked. (passed)')
    print('    In checking process, we get ' + COLOR.warningcolor +
          '{} '.format(flag) + COLOR.tipcolor +
          'filedata hash warning.' + COLOR.endcolor)


@printer('ERROR')
def print_check_log():
    """Print IMA Intergrity Measurement checking failed info.
    """
    print(COLOR.warningcolor + 'IMA Measurement checking failed.' + COLOR.endcolor)


def check_ima_measurement(ima_log, pcr10):
    """
    Check if the related value in system are identical with the record in IMA runtime log.
    """
    template_logged_hash = [item[0] for item in ima_log]
    filedata_logged_hash = [item[1] for item in ima_log]
    file_hint = [item[2] for item in ima_log]

    # check hash algorithm is sha256
    hash_alg_flag = check_hash_alg(ima_log)

    # check file data hash
    ## boot_aggregate hash checking
    boot_flag = check_boot_aggregate(filedata_logged_hash[0])
    ## IMA policy file data hash checking
    filedata_flag = check_filedata_hash(file_hint, filedata_logged_hash)
    ## check template_hash
    template_flag = check_template_hash(template_logged_hash,
                                        filedata_logged_hash,
                                        file_hint)
    ## check PCR_10 value
    pcr10_flag = check_pcr10_value(pcr10)
    ## check integrity of IMA measurement
    if hash_alg_flag > 0 or boot_flag > 0 or template_flag > 0 or pcr10_flag > 0:
        print_check_log()
        return False
    else:
        print_ima_integrity(filedata_flag)
        return True


def main():
    """Main workflow to do IMA Intergrity Measurement checking.
    """
    init_tss()
    pcr = get_pcrs()[PCR_LABL[10]]
    hashlog = get_hashlog()
    if check_ima_measurement(hashlog, pcr):
        print("[INFO]: result of IMA Measurement checking")
        print("    IMA Integrity Measurement \033[4;32mSucceeded" + COLOR.endcolor)
	return 0
    else:
        print("[ERROR]: IMA Measurement Result")
        print("    IMA Integrity Measurement \033[4;31m Failed" + COLOR.endcolor)
	return 127


if __name__ == "__main__":
    # run IMA Intergrity Measurement checking
    main()
