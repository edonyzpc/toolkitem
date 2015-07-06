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
 # Last modified:	2015-07-05 15:24
 #
 # Filename:		cpy.h
 #
 # Description: All Rights Are Reserved
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
/*
 * Class CPY is a well encapsulated interface for c++ call python function or run python script.
 */
#ifndef _CPY_H
#define _CPY_H
#include <iostream>
#include <string>
#include <vector>
#include <python2.7/Python.h>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

class CPY {
    public:
        // call python function
        CPY(string fname, string fmodel, vector<PyObject*> arg):
            func_name(fname),model_import(fmodel),args(arg) {};
        // run python script
        CPY(string script):script_name(script) {};
        void RunScript();
        void ImportModel(string mimport);
        PyObject *ImportModel();
        PyObject *RunFunc();

    protected:

    private:
        string func_name;
        string model_import;    // model_import can contain the path of to import model
        string script_name;
        vector<PyObject*> args;

};

#endif
