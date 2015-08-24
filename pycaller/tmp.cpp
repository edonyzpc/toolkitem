#include <iostream>
#include <string>
#include <vector>
#include <python2.7/Python.h>
#include "cpy.h"
using namespace std;

int main() {
    string name;
    cin >> name;
    cout << name.substr(name.rfind('/')+1) <<endl;
    cout << name.substr(0, name.rfind('/')) <<endl;

    string script("/home/edony/code/github/toolkitem/emgui/gui.py");
    Py_Initialize();
    CPY test(script);
    test.RunScript();

    string func_name("main");
    string func_model("pyproperty");
    string import_model("/home/edony/code/github/toolkitem/pycaller/pyproperty.py");
    vector<PyObject*> arg;
    PyObject *str = NULL;
    str = PyString_FromString("edony");
    arg.push_back(str);
    long a = 12;
    PyObject *age = NULL;
    age = PyInt_FromLong(a);
    arg.push_back(age);
    CPY fun(func_name, import_model, arg);
    PyObject *result = fun.RunFunc();
    char *res = NULL;
    cout << "results: " << PyInt_AsLong(result);
    cout << res << endl;
    string func_name1("__gui__");
    string import_model1("/home/edony/code/github/toolkitem/pycaller/pyproperty.py");
    vector<PyObject*> arg1;
    CPY fun1(func_name1, import_model1, arg1);
    PyObject *result1 = fun1.RunFunc();
    Py_Finalize();

}
