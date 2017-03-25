from __future__ import print_function
from pycolor import PyColor
from pycolor import cprint

@PyColor('ured')
def printer(string):
    a = 1
    b = 2
    print(str((a + b)**4) + string)

class TestClass(object):
    def test_pycolor(self):
        printer('edony')

    def test_cprint(self):
        cprint('ugreen', 'hello edony')

    def test_setformat(self):
        py_color = PyColor('green')
        py_color.format = 'ucyan'
        cprint(py_color.format, 'this is test')

#if __name__ == "__main__":
#    cprint('ugreen', 'hello edony')
#    printer('edony')
#    py_color = PyColor('green')
#    py_color.format = 'ucyan'
#    print(py_color.format)
#    cprint(py_color.format, 'this is test')
