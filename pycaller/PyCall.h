#ifndef _PYCALL_H_
#define _PYCALL_H_
#include <python2.7/Python.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
class PyCall
{
public:
	PyCall(string path,string f,string imod="",PyObject* pyim=NULL):pathmod(path),func(f),importmod(imod)
    {
        this->pyimportmod = pyim;
    };
    PyCall(string fn):filename(fn){cout<<"string\n";};
    inline void setFuncArg(vector<PyObject*> pa)
    {
        this->pyargv.insert(this->pyargv.end(),pa.begin(),pa.end());
    };
    inline void setRunnerArg(vector<string> sa)
    {this->strargv.insert(this->strargv.end(),sa.begin(),sa.end());};
    //virtual ~PyCall();
    PyObject* caller();
    void PyRunner();
protected:
    int PyInit();
    void addpath(string path);
    int PyImport(string mod);
    PyObject* PyImport(string strmod="",PyObject* Pymod=NULL);
    void PyCaller(PyObject* mod,const char* func,vector<string> argstr,vector<PyObject*> argpy);
	void PyRunFunc(string apppath,const char* func,const char* module,PyObject**funcarg,int argnum);
private:
    string importmod;   //name of modules to import
    string pathmod;     //path of modules to import
    PyObject* pyimportmod;
    string func;            //name of function to call in python
    string filename;       //file name of python scripts to run
    vector<PyObject*> pyargv;  //parameter of fun whose type is PyObject
    vector<string> strargv;    //parameter of fun whose type is string
};
#endif
