#include <boost/noncopyable.hpp>
#include <boost/python.hpp>
#include <iostream>

using namespace std;
using namespace boost;

class pyinit: boost::noncopyable {
    public:
        pyinit(int initsigs = 1) {
            assert(initsigs == 0 || initsigs == 1);
            Py_InitializeEx(initsigs);
        }
        ~pyinit(){};

        bool isInitialized() {
            return Py_IsInitialized();
        }
        const char* version() {
            return Py_GetVersion();
        }
};

int main() {
    pyinit pinit;

    boost::python::list l;
    l.append("edony");
    l.append(12);

    cout << boost::python::len(l) << endl;
}
//#cat test.cpp 
//#include <boost/lexical_cast.hpp>
//#include <iostream>
//
//int main()
//{
//    using boost::lexical_cast;
//    int a= lexical_cast<int>("123456");
//    double b = lexical_cast<double>("123.456");
//    std::cout << a << std::endl;
//    std::cout << b << std::endl;
//    return 0;
//}
