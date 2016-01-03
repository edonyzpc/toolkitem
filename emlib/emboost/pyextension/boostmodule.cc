int Max(int i, int j) {
    return (i > j)?i:j;
}

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

using namespace boost::python;

BOOST_PYTHON_MODULE(bm) {
    def("Max", Max);
}
