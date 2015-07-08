#define BOOST_PYTHON_SOURCE
#include <boost/python.hpp>
#include <string>
#include <iostream>

using namespace std;
using namespace boost::python;

int main() {
    Py_Initialize();

    object i(10);
    i = 10*i;
    cout << extract<int>(i) << endl;
    boost::python::tuple t = boost::python::make_tuple("edony", "cc");
    cout << string(extract<string>(t[0])) << endl;
    cout << boost::python::len(t) << endl;
}
