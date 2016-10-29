#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wmi 
import os 
import sys 
import platform 
import time 

def sys_version():  
    c = wmi.WMI () 
    #获取操作系统版本 
    for sys in c.Win32_OperatingSystem(): 
        print "Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber 
        print  sys.OSArchitecture.encode("UTF8")#系统是32位还是64位的 
        print sys.NumberOfProcesses #当前系统运行的进程总数

def cpu_mem(): 
    c = wmi.WMI ()        
    #CPU类型和内存 
    for processor in c.Win32_Processor(): 
        #print "Processor ID: %s" % processor.DeviceID 
        print "Process Name: %s" % processor.Name.strip() 
    for Memory in c.Win32_PhysicalMemory(): 
        print "Memory Capacity: %.fMB" %(int(Memory.Capacity)/1048576) 

def cpu_use(): 
    #5s取一次CPU的使用率 
    c = wmi.WMI() 
    while True: 
        for cpu in c.Win32_Processor(): 
             timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime()) 
             print '%s | Utilization: %s: %d %%' % (timestamp, cpu.DeviceID, cpu.LoadPercentage) 
             time.sleep(5)     

def disk(): 
    c = wmi.WMI ()    
    #获取硬盘分区 
    for physical_disk in c.Win32_DiskDrive (): 
        for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
            for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
                print physical_disk.Caption.encode("UTF8"), partition.Caption.encode("UTF8"), logical_disk.Caption 

    #获取硬盘使用百分情况 
    for disk in c.Win32_LogicalDisk (DriveType=3): 
        print disk.Caption, "%0.2f%% free" % (100.0 * long (disk.FreeSpace) / long (disk.Size)) 

def network(): 
    c = wmi.WMI ()     
    #获取MAC和IP地址 
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1): 
        print "MAC: %s" % interface.MACAddress 
    for ip_address in interface.IPAddress: 
        print "ip_add: %s" % ip_address 
    print 

    #获取自启动程序的位置 
    for s in c.Win32_StartupCommand (): 
        print "[%s] %s <%s>" % (s.Location.encode("UTF8"), s.Caption.encode("UTF8"), s.Command.encode("UTF8"))  

     
    #获取当前运行的进程 
    for process in c.Win32_Process (): 
        print process.ProcessId, process.Name 

def main(): 
    sys_version() 
    #cpu_mem() 
    #disk() 
    #network() 
    #cpu_use() 

if __name__ == '__main__': 
    main() 
    print platform.system() 
    print platform.release() 
    print platform.version() 
    print platform.platform() 
    print platform.machine() 
