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
 # Last modified: 2015-05-07 15:19
 # 
 # Filename: pycall.h
 # 
 # Description: All Rights Are Reserved                 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
// File pycall.h declare the PyCall calss.
// PyCall is a python interpreter caller in C/C++ with help of Python C-API.

#ifndef _PYCALL_H_
#define _PYCALL_H_
#include <iostream>
#include <string>
#include <vector>
#include <python2.7/Python.h>
using namespace std;
class PyCall {
public:
	PyCall(string path, string func_name,
            string import_mod = "", PyObject* py_object_import_mod = NULL)
        :mod_path_(path),
        func_(func_name),
        import_mod_(import_mod) {
        this->py_import_mod_ = py_object_import_mod;
    };

    explicit PyCall(string fn):file_name_(fn){};

    virtual ~PyCall(){};

    inline void set_func_arg(vector<PyObject*> pa) {
        this->py_argv_.insert(this->py_argv_.end(),pa.begin(),pa.end());
    };

    inline void set_runner_arg(vector<string> sa){
        this->str_argv_.insert(this->str_argv_.end(),sa.begin(),sa.end());
    };

    PyObject* Caller();
    void PyRunner();

protected:
    int PyInit();
    void AddPath(string path);
    //int PyImport(string mod);
    PyObject* PyImport(string strmod="",PyObject* Pymod=NULL);
    void PyCaller(PyObject* mod,const char* func,vector<string> argstr,vector<PyObject*> argpy);
	void PyRunFunc(string apppath,const char* func,const char* module,PyObject**funcarg,int argnum);

private:
    string import_mod_;   //name of modules to import
    string mod_path_;     //path of modules to import
    PyObject* py_import_mod_;
    string func_;            //name of function to call in python
    string file_name_;       //file name of python scripts to run
    vector<PyObject*> py_argv_;  //parameter of fun whose type is PyObject
    vector<string> str_argv_;    //parameter of fun whose type is string

};
#endif
