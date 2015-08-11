# PEER-REVIEW LIBRARY BOOST
1. Use boost.python to embed python into C++

2. Use boost.python to extend python with C++

P.S.

`g++ -o xx xx.cc -I/python/include/path -I/boost/include/path -l/path/lib_boost_python -l/path/libpythonx.x`

Linux:<br>

------

`g++ -fPIC -shared -o mo.so boostmodule.cc -Iboost/python -I/usr/include/python2.7 -lboost_python -lpython2.7`

Max:<br>

------
TODO(edony):add mac share lib compile command line
