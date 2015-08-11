# Personal Ways to Extend Python With C/C++

* First.
    
    gcc/g++ compile the c/c++ source code into shared library. And this library can be an importable module by python.

* Second:

    boost::python extend the python module with c/c++ and the build the module with setup.py file help with distutil.Extension and distutil.core.
