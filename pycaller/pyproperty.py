#!/usr/bin/env python
# -*- coding: utf-8 -*-
 #        .---.         .-----------  
 #       /     \  __  /    ------    
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_            
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->   
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    / 
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /) 
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`  
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'    
 # ######################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified:	2015-05-03 20:56
 # 
 # Filename:		pyproperty.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    
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
    
    e.g：
    \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
    \033[0m         <!--set all into default-->
    '''
    WARNING = '\033[0;37;41m'
    ENDC = '\033[0m'
    def disable(self):
        self.ENDC = ''
        self.WARNING = ''
 
#import numpy as np
#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
 
class protest(object):
    def __init__(self,name,age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,n):
        print('change...')
        if '@' not in n:
            raise ValueError('Invalid Value.')
        self._name = n

    @name.deleter
    def name(self):
        del sel._name
        
def main(n,a):
    tmp = protest(n,a)
    print(tmp.age)
    print(tmp.name)
    print(tmp._name)
    tmp.name = 'Murphy' #property
    tmp.age = 33 #bad idea to change member data
    print(tmp.age)
    print(tmp.name)
    print(tmp._name)
    tmp._name = 'cc' #to change member data
    tmp.age = 12 #to change member data
    print(tmp.age)
    print(tmp.name)
    print(tmp._name)

class Person(object):
    def __init__(self, name):
        self._name = name
        self.age = 10
    @property
    def name(self): # name = property(name)
        '''name property docs'''
        print('fetch...')
        return self._name
    @name.setter
    def name(self, value): # name = name.setter(name)
        print('change...')
        if self.age > 40:
            raise ValueError("not enough")
        else:
            self._name = value
    @name.deleter
    def name(self): # name = name.deleter(name)
        print('remove...')
        del self._name
if __name__ == '__main__':
    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob.name) # Runs name getter (name 1)
    bob.name = 'Robert Smith' # Runs name setter (name 2)
    print(bob.name)
    del bob.name # Runs name deleter (name 3)
    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.name)
    print(Person.name.__doc__) # Or help(Person.name)
    tmp = protest('edony',34)
    print(tmp.age)
    print(tmp._name)
    tmp._name = 'Murphy' #property
    tmp.age = 33 #bad idea to change member data
    print(tmp.age)
    print(tmp._name)
    tmp._name = 'cc' #to change member data
    tmp.age = 12 #to change member data
    print(tmp.age)
    print(tmp._name)
    import sys
    print(sys.argv)
