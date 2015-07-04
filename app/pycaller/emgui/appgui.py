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

def app():
    win = tkinter.Tk()
    win.geometry("800x450")
    win.title("File Manager")
    gui = GUI(win)
    win.mainloop()
    print(gui.pc_file)
    return (gui.pc_file, gui.stl_file, gui.igs_file)

if __name__ == "__main__":
    #pc, stl, igs = app()
    #print(pc, stl, igs)
    tmp = app()
    print(type(tmp))

