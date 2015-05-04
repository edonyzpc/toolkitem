 /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
 # ##########################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-04-13 22:03
 # 
 # Filename: test.cpp
 # 
 # Description: All Rights Are Reserved                 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#include <iostream>
#include <string>
#include <python2.7/Python.h>
#include "PyCall.h"
using namespace std;

int main()
{
	Py_Initialize();
	if(!Py_IsInitialized())
	{
		printf("ERROR: Python Initialize failed.\n");
		return -1;
	}
    string path = "/home/edony/code/github/toolkitem/pycaller";
    PyCall funcall(path,"main","pyproperty",NULL);
    string name = "edony";
    int age = 23;
    int _age = age;
    int i2c = age;
    int count = 0;
    while(i2c)
    {
        i2c /= 10;
        count++;
    }
    char* cage = new char[count+1];
    for(int i=0;i<count;i++)
    {
        cage[i] = _age%10 + '0';
        _age /= 10;
    }
    cage[count] = '\0';
    vector<PyObject*> arg;
    PyObject* tmp1 = Py_BuildValue("s",name.c_str());
    PyObject* tmp2 = Py_BuildValue("i",age);
    arg.push_back(tmp1);
    arg.push_back(tmp2);
    funcall.setFuncArg(arg);
    PyObject* t = funcall.caller();

	Py_Initialize();
	if(!Py_IsInitialized())
	{
		printf("ERROR: Python Initialize failed.\n");
		return -1;
	}
    string fn = "'pyproperty.py'";
    cout<<fn<<endl;
    vector<string> ast;
    ast.push_back("'eee'");
    ast.push_back("'ccc'");
    ast.push_back("'ddd'");
    cout<<ast[2]<<endl;
    PyCall strcall(fn);
    strcall.setRunnerArg(ast);
    strcall.PyRunner();
}
