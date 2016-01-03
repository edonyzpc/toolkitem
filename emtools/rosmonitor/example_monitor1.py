import os
import win32api
import win32con
import wmi
import time

def getSysInfo(wmiService = None):
    result = {}
    if wmiService == None:
        wmiService = wmi.WMI()
    # cpu
    for cpu in wmiService.Win32_Processor():
        timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
        result['cpuPercent'] = cpu.loadPercentage
    # memory
    cs = wmiService.Win32_ComputerSystem()
    os = wmiService.Win32_OperatingSystem()
    result['memTotal'] = int(int(cs[0].TotalPhysicalMemory)/1024/1024)
    result['memFree'] = int(int(os[0].FreePhysicalMemory)/1024)
    #disk
    result['diskTotal'] = 0
    result['diskFree'] = 0
    for disk in wmiService.Win32_LogicalDisk(DriveType=3):
        result['diskTotal'] += int(disk.Size)
        result['diskFree'] += int(disk.FreeSpace)
    result['diskTotal'] = int(result['diskTotal']/1024/1024)
    result['diskFree'] = int(result['diskFree']/1024/1024)
    return result

if __name__ == '__main__':
    wmiService = wmi.WMI()
    while True:
        print getSysInfo(wmiService)
        time.sleep(3)
