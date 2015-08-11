#include <boost/python.hpp>
#include "pyex.h"

using namespace boost::python;

BOOST_PYTHON_MODULE(pyex) {
    class_<pyex>("pyex", init<float,float>())
        .def("Max", &pyex::Max);
        //.def_readwrite("a", &pyex::a)
        //.def_readwrite("b", &pyex::b);
}
