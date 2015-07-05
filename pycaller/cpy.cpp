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
 # Last modified: 2015-07-05 15:42
 #
 # Filename: cpy.cpp
 #
 # Description: All Rights Are Reserved
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#include <cstdio>
#include <iostream>
#include <string>
#include <python2.7/Python.h>
#include "cpy.h"

using std::cout;
using std::cin;
using std::endl;
using std::string;

void CPY::ImportModel(string import_model) {
    PyRun_SimpleString("import sys");
    string model = import_model.substr(import_model.rfind('/') + 1);
    cout << model << endl;
    model = model.substr(0, model.find('.'));
    cout << model << endl;
    string path = import_model.substr(0, import_model.rfind('/'));
    string path_cmd("sys.path.append('");
    path_cmd += path;
    path_cmd += "')";
    PyRun_SimpleString(path_cmd.c_str());
    string import_cmd("import ");
    import_cmd += model;
    PyRun_SimpleString(import_cmd.c_str());

}

PyObject *CPY::ImportModel() {
    PyRun_SimpleString("import sys");
    string model = this->model_import.substr(this->model_import.rfind('/') + 1);
    model = model.substr(0, model.find('.'));
    string path = this->model_import.substr(0, this->model_import.rfind('/'));
    string path_cmd("sys.path.append('");
    path_cmd += path;
    path_cmd += "')";
    PyRun_SimpleString(path_cmd.c_str());
    return PyImport_ImportModuleNoBlock(model.c_str());

}

void CPY::RunScript() {
    if (!this->model_import.empty()) {
        ImportModel(this->model_import);
    }
    if (!this->script_name.empty()) {
        ImportModel(this->script_name);
    }
    PyRun_SimpleString("import subprocess");
    string tmp("[\'python\', ");
    tmp += "\'";
    tmp += this->script_name;
    tmp += "\']";
    string cmd = "subprocess.call(" + tmp + ")";
    PyRun_SimpleString(cmd.c_str());

}

PyObject *CPY::RunFunc() {
    PyObject *model = NULL;
    model = ImportModel();
    if (!model) {
        cout << "Can't import model\n";
        return 0;
    }
    PyObject *dict = NULL;
	dict = PyModule_GetDict(model);
	if (!dict) {
		printf("ERROR: can't find __dict__ of imported module\n");
		return 0;
	}
	// 找出函数
    PyObject *func = NULL;
	func = PyDict_GetItemString(dict, this->func_name.c_str());
	if (!func || !PyCallable_Check(func)) {
		printf("ERROR: can't find attribute function\n");
		return 0;
	}
	// 参数进栈
    if (this->args.size() == 0) {
	    PyObject *arg_tuple = NULL;
	    // 调用Python函数
        PyObject *rev;
	    rev = PyObject_CallObject(func, arg_tuple);
        return rev;
    }
    else {
	    PyObject *arg_tuple = PyTuple_New(this->args.size());
        // PyObject* Py_BuildValue(char *format, ...)
	    // 把C++的变量转换成一个Python对象。当需要从
	    // C++传递变量到Python时，就会使用这个函数。此函数
	    // 有点类似C的printf，但格式不同。常用的格式有
	    // s 表示字符串，
	    // i 表示整型变量，
	    // f 表示浮点数，
	    // O 表示一个Python对象。
	    for(int i = 0;i < this->args.size(); ++i)
		    PyTuple_SetItem(arg_tuple, i, this->args[i]);
	    // 调用Python函数
        PyObject *rev;
	    rev = PyObject_CallObject(func, arg_tuple);
        return rev;
    }

}
