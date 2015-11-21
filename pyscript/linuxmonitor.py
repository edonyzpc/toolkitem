#!/usr/bin/env Python
#from __future__ import print_function
from collections import OrderedDict
import sys
import time
 
def CPUinfo():
    ''' Return the information in /proc/CPUinfo
    as a dictionary in the following format:
    CPU_info['proc0']={...}
    CPU_info['proc1']={...}
    '''
    CPUinfo=OrderedDict()
    procinfo=OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                CPUinfo['proc%s' % nprocs] = procinfo
                nprocs=nprocs+1
                # Reset
                procinfo=OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
 
    return CPUinfo

def load_stat(avg): 
    fbuf = open("/proc/loadavg", 'r')
    con = fbuf.read()
    avg['lavg_1']=con.split()[0] 
    avg['lavg_5']=con.split()[1] 
    avg['lavg_15']=con.split()[2] 
    avg['nr']=con.split()[3] 
    avg['last_pid']=con.split()[4] 
    fbuf.close()
    #return loadavg 

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()
 
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo


if __name__=='__main__':
    #print(meminfo())
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))

    CPUinfo = CPUinfo()
    for processor in CPUinfo.keys():
        print(CPUinfo[processor]['model name'])

    loadavg = {}
    load_stat(loadavg)
    
    if len(sys.argv) > 1:
	    INTERFACE = sys.argv[1]
    else:
	    INTERFACE = 'eth0'
    STATS = []
    print 'Interface:' + INTERFACE
 
    def rx():
        ifstat = open('/proc/net/dev').readlines()
        for interface in  ifstat:
            if INTERFACE in interface:
	        stat = float(interface.split()[1])
	        STATS[0:] = [stat]

    def tx():
        ifstat = open('/proc/net/dev').readlines()
        for interface in  ifstat:
            if INTERFACE in interface:
                stat = float(interface.split()[9])
	        STATS[1:] = [stat]
 
    print 'In            Out'
    rx()
    tx()
 
    while True:
        time.sleep(1)
        rxstat_o = list(STATS)
        rx()
        tx()
        RX = float(STATS[0])
        RX_O = rxstat_o[0]
        TX = float(STATS[1])
        TX_O = rxstat_o[1]
        RX_RATE = round((RX - RX_O)/1024/1024,3)
        TX_RATE = round((TX - TX_O)/1024/1024,3)
        print RX_RATE ,'MB		',TX_RATE ,'MB'

