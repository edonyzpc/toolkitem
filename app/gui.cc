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
#include "cpy.h"

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ifstream;

void gui() {
	Py_Initialize();
	if (!Py_IsInitialized()) {
		printf("ERROR: Python Initialize failed.\n");
		return;
	}
    string func_name("app");
    string model("./emgui/appgui.py");
    vector<PyObject*> args;
    CPY fun(func_name, model, args);
    PyObject *result = NULL;
    result = fun.RunFunc();
    PyObject *list = NULL;
    Py_ssize_t len = PyList_Size(result);
    for (Py_ssize_t i=0; i < len; ++i) {
        list = PyList_GetItem(result, i);
        char *str_tmp = NULL;
        str_tmp = PyString_AsString(list);
        cout << str_tmp << endl;
    }
    Py_Finalize();
}
int main() {
	Py_Initialize();
	if (!Py_IsInitialized()) {
		printf("ERROR: Python Initialize failed.\n");
		return -1;
	}
    string func_name("app");
    string model("./emgui/appgui.py");
    vector<PyObject*> args;
    CPY fun(func_name, model, args);
    PyObject *result = NULL;
    result = fun.RunFunc();
    PyObject *list = NULL;
    Py_ssize_t len = PyList_Size(result);
    for (Py_ssize_t i=0; i < len; ++i) {
        list = PyList_GetItem(result, i);
        char *str_tmp = NULL;
        str_tmp = PyString_AsString(list);
        cout << i << str_tmp << endl;
    }
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("import subprocess");
    PyRun_SimpleString("sys.path.append('/Users/edony/coding/toolkitem/app/emgui')");
    string tmp = "['python', '/Users/edony/coding/toolkitem/app/emgui/appgui.py']";
    string cmd = "subprocess.call(" + tmp + ")";
    PyRun_SimpleString(cmd.c_str());
    char line[256];
    std::ifstream file("buf", std::ios::binary|std::ios::in);
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
