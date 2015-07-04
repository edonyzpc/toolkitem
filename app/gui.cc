 /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
 # Last modified: 2015-07-04 22:04
 #
 # Filename: gui.cc
 #
 # Description: All Rights Are Reserved
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#include <iostream>
#include <fstream>
#include <string>
#include <python2.7/Python.h>
#include "pycall.h"

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main() {
	Py_Initialize();
	if (!Py_IsInitialized()) {
		printf("ERROR: Python Initialize failed.\n");
		return -1;
	}
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("import subprocess");
    //PyRun_SimpleString("sys.path.append('./emgui')");
    string tmp = "['python', './emgui/appgui.py']";
    string cmd = "subprocess.call(" + tmp + ")";
    PyRun_SimpleString(cmd.c_str());
    char line[256];
    ifstream file("buf", ios::binary|ios::in);
    vector<string> filelist;
    while (!file.eof()) {
        file.getline(line, 256, '\n');
        cout << line << endl;
        string tmp(line);
        filelist.push_back(tmp);
    }
    Py_Finalize();
    //PyRun_SimpleString("import appgui");
    //PyCall funcall(path,"app","appgui",NULL);
    //PyObject *result = NULL;
    //result = funcall.Caller();
    //PyObject *pc = PyTuple_GetItem(result, 1);
    //PyObject *stl = PyTuple_GetItem(result, 2);
    //PyObject *igs = PyTuple_GetItem(result, 3);
    //char *ps_c = PyString_AsString(pc);
    //char *stl_c = PyString_AsString(stl);
    //char *igs_c = PyString_AsString(igs);
    //cout << ps_c<< endl;
    //cout << stl_c<< endl;
    //cout << igs_c<<endl;
}
