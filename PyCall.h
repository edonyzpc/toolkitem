#pragma once
#include"Python.h"
#include <string>
using namespace std;
class PyCall
{
public:
	PyCall(void);
	~PyCall(void);
	void PyRunFunc(string apppath,const char* func,const char* module,PyObject**funcarg,int argnum);
protected:
    int PyInit();
    void addpath(string path);
    int PyImport(string mod);
    PyObject* PyImport(PyObject* Pymod);
    void PyCaller(PyObject* mod,const char* func,vector<string> argstr,vector<PyObject*>argpy);

private:
    vector<string> importmod;   //name of modules to import
    vector<string> pathmod;     //path of modules to import
    const char* fun;            //name of function to call in python
    Vector<PyObject*> argfunc;  //parameter of fun whose type is PyObject
    vector<string> kargfunc;    //parameter of fun whose type is string
};
