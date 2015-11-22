#coding:utf-8
#-------------
#Author:Hu
#Data:20150520
#-------------

from __future__ import division
import re
import time
from optparse import OptionParser


def getbandwidth(eth='eth0',intevel=1):
    a=open('/proc/net/dev')
    data=a.read()
    patten=eth + '.*'
    if  not re.search(patten,data):
        print "The ETHname not have"
        exit(1)
    Rev_old=re.search(patten,data).group().replace(':',' ').split()[1]
    Send_old=re.search(patten,data).group().replace(':',' ').split()[9]
    a.close()

    while True:
        #print intevel
        time.sleep(int(intevel))
        a=open('/proc/net/dev')
        data=a.read()
        Rev=re.search(patten,data).group().replace(':',' ').split()[1]
        Send=re.search(patten,data).group().replace(':',' ').split()[9]
        diff_Rev=int(Rev)-int(Rev_old)
        diff_Sen=int(Send)-int(Send_old)
        diff_M=diff_Rev*8/1024/1024/int(intevel)
        diff_S=diff_Sen*8/1024/1024/int(intevel)
        print time.strftime("%Y%m%d %H:%M:%S") + '   The Recevie is  %6.2f Mbps(byte is %d)' % (diff_M,diff_Rev) + '   The Send is  %6.2f Mbps(byte is %d)' % (diff_S,diff_Sen)
        Rev_old=Rev
        Send_old=Send
        a.close()
if __name__=='__main__':
    
    import sys
    usage='''%prog [-i ethname] [-t interveltime]
           Example:%prog -i eth0 -t 1'''
    parser=OptionParser(usage=usage,version='2.0_20150602')

    parser.add_option('-i','--interface',dest='interface',default='eth0',help='Wann to interface')
    parser.add_option('-t','--time',dest='intevel',type='int',default='1',help='The intevel time')
    (options,args)=parser.parse_args()
    print "The interafce is %s and the intevel time is %d" % (options.interface,options.intevel)
    getbandwidth(options.interface,options.intevel)
