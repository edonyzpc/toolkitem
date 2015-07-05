#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
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
 # Last modified: 2015-07-04 22:08
 #
 # Filename: appgui.py
 #
 # Description: All Rights Are Reserved
 #
"""
import sys
if sys.version.startswith('3.4'):
    import tkinter
else:
    import Tkinter as tkinter
from project_file_browser import GUI
import os

def app():
    print 1
    path = os.getcwd()
    print path
    print 2
    win = tkinter.Tk()
    print 3
    win.geometry("800x450")
    print 4
    win.title("File Manager")
    print 5
    gui = GUI(win)
    print 6
    win.mainloop()
    print 7
    return [path, gui.pc_file, gui.stl_file, gui.igs_file]

if __name__ == "__main__":
    #pc, stl, igs = app()
    #print(pc, stl, igs)
    tmp = app()
    os.chdir(tmp[0])
    f = open("./buf", "w")
    f.write(tmp[1]+"\n")
    f.write(tmp[2]+"\n")
    f.write(tmp[3]+"\n")
    f.close()

