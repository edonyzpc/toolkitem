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
 # Last modified: 2015-05-07 15:32
 # 
 # Filename: pycall.cpp
 # 
 # Description: All Rights Are Reserved                 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
// File pycall.cpp is the definition of class PyCall.
// PyCall class can call an attribute in the Python module.
// And PyCall class can directly run the Python script.

#include <iostream>
#include <string>
#include "pycall.h"
using namespace std;

// Protected PyCall class prototype, not used
void PyCall::PyRunFunc(string append_path,
                        const char *kfunc,
                        const char *kmodule,
                        PyObject **func_arg,
                        int num_arg) {
	PyObject *py_object_name, *py_object_module,
             *py_object_dict, *py_object_func,
             *py_object_args, *py_object_return_val,
             *py_object_import;
	Py_Initialize();
	if(!Py_IsInitialized()) {
		printf("ERROR: Python Initialize failed.\n");
		return;
	}

	string cmd_head = "sys.path.append('";
	string cmd_end = "')";
	string append_sys_path = cmd_head + append_path + cmd_end;
	const char * krunstr = append_sys_path.c_str();
	PyRun_SimpleString("import sys\n");
	PyRun_SimpleString("sys.path.append('./')\n");
	PyRun_SimpleString(krunstr);
	py_object_name = PyString_FromString(kmodule);
	py_object_module = PyImport_Import(py_object_name);

	if (!py_object_module) {
		printf("WARNING: can't find import module\n");
		return;
	}
	py_object_dict = PyModule_GetDict(py_object_module);
	if (!py_object_dict) {
		printf("ERROR: can't find __dict__ of imported module\n");
		return;
	}
	// 找出函数
	py_object_func = PyDict_GetItemString(py_object_dict, kfunc);
	if (!py_object_func || !PyCallable_Check(py_object_func)) {
		printf("ERROR: can't find attribute function\n");
		return;
	}
	// 参数进栈
	py_object_args = PyTuple_New(num_arg);

	// PyObject* Py_BuildValue(char *format, ...)
	// 把C++的变量转换成一个Python对象。当需要从
	// C++传递变量到Python时，就会使用这个函数。此函数
	// 有点类似C的printf，但格式不同。常用的格式有
	// s 表示字符串，
	// i 表示整型变量，
	// f 表示浮点数，
	// O 表示一个Python对象。

	for(int i = 0;i < num_arg; ++i)
		PyTuple_SetItem(py_object_args, i, *(func_arg+i));

	// 调用Python函数
	py_object_return_val = PyObject_CallObject(py_object_func, py_object_args);
	Py_Finalize();
}

// Initial the Python interpreter
int PyCall::PyInit() {
    //TODO(edony): make clear interpreter initialization with Py_Initialize()
	PyRun_SimpleString("import sys\n");
	PyRun_SimpleString("sys.path.append('./')\n");
	Py_Initialize();
	if(!Py_IsInitialized())
	{
		printf("ERROR: Python Initialize failed.\n");
		return -1;
	}
    else
        return 1;
}

// Add the path of module to be imported or the path of Python script needed module
void PyCall::AddPath(string path) {
	string cmd_head = "sys.path.append('";
	string cmd_end = "')";
	string append_sys_path = cmd_head + path + cmd_end;
	const char * krunstr = append_sys_path.c_str();
	PyRun_SimpleString(krunstr);
}

// Import the Python module.
// You can take the module name with PyObject type.
// And you can take the module name with string type.
// Note: string type parameter comes first and do not take both parameter.
PyObject* PyCall::PyImport(string module_name_str,
                            PyObject *module_name_py_object) {
    if (!module_name_str.empty() || module_name_py_object)
    {
        PyObject* py_string_module = PyString_FromString(module_name_str.c_str());
        PyObject* py_str_import_module = PyImport_Import(py_string_module);
	    if (!py_str_import_module) {
		    printf("WARNING: can't find import module\n");
	    } else {
            return py_str_import_module;
        }

	    PyObject* py_object_import_module = PyImport_Import(module_name_py_object);
	    if (!py_object_import_module) {
		    printf("WARNING: can't find import module\n");
		    return 0;
	    } else {
            return py_object_import_module;
        }
    } else {
        printf("error: only one parameter taken\n");
        return 0;
    }
}

// Call the imported module attributes(function).
PyObject* PyCall::Caller() {
    int flag_py_initial;
    flag_py_initial = this->PyInit();
    if(flag_py_initial != -1) {
        PyObject* module_import = this->PyImport(this->import_mod_,this->py_import_mod_);
    	PyObject* module_dict = PyModule_GetDict(module_import);
    	if (!module_dict) {
    		printf("ERROR: can't find __dict__ of imported module\n");
    		return 0;
    	}
    	// 找出函数
	    PyObject* func = PyDict_GetItemString(module_dict, this->func_.c_str());
	    if (!func || !PyCallable_Check(func)) {
    		printf("ERROR: can't find attribute function\n");
    		return 0;
    	}
    	// 参数进栈
        size_t num_arg;
        num_arg = this->py_argv_.size();
    	PyObject* func_args = PyTuple_New(num_arg);
    	// PyObject* Py_BuildValue(char *format, ...)
    	// 把C++的变量转换成一个Python对象。当需要从
    	// C++传递变量到Python时，就会使用这个函数。此函数
    	// 有点类似C的printf，但格式不同。常用的格式有
    	// s 表示字符串，
    	// i 表示整型变量，
    	// f 表示浮点数，
	    // O 表示一个Python对象。

	    for(int i = 0; i < num_arg; ++i)
		    PyTuple_SetItem(func_args, i, this->py_argv_[i]);

	    // 调用Python函数
        std::cout << func << std::endl;
	    //PyObject* py_object_return = PyObject_CallObject(func, func_args);
	    PyObject* py_object_return = PyObject_CallObject(func, func_args);
        std::cout << py_object_return << std::endl;
        //Py_Finalize();
        return py_object_return;
    }
}

// Directly run the imported Python module.
void PyCall::PyRunner() {
    int flag_py_initial;
    flag_py_initial = this->PyInit();
    if(flag_py_initial != -1) {
        printf("RUNNER\n");
	    PyRun_SimpleString("import sys");
	    PyRun_SimpleString("import subprocess");
        string tmp = "[sys.executable, "+this->file_name_+",";
        for(size_t i = 0;i < this->str_argv_.size(); ++i) {
            if(1 == str_argv_.size() - i)
                tmp += str_argv_[i] + "]";
            else
                tmp += str_argv_[i] + ",";
        }
        printf("%s\n",tmp.c_str());
        string cmd = "subprocess.call(" + tmp + ")";
        PyRun_SimpleString(cmd.c_str());
        //TODO(edony):try use `execfile()` instead of subprocess
        /*
         *Py_Initialize() do not have the sys.argv
         */
        //string tmp1 = "sys.argv = ["+this->filename+",";
        //for(size_t i=0;i<this->strargv.size();i++)
        //{
        //    if(1==strargv.size()-i)
        //        tmp1 += strargv[i] + "]";
        //    else
        //        tmp1 += strargv[i] + ",";
        //}
        //cout<<tmp1<<endl;
        //PyRun_SimpleString(tmp1.c_str());
        //string file = "execfile(";
        //file = file + this->filename + ")";
        //cout<<file.c_str()<<endl;
        //PyRun_SimpleString(file.c_str());
    }
    Py_Finalize();
}

