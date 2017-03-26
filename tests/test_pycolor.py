from __future__ import print_function
import sys
sys.path.append('./')
from colorprinter.pycolor import PyColor
from colorprinter.pycolor import cprint

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

    def test_disableformat(self):
        py_color = PyColor('ured')
        cprint(py_color.format, 'this is test')
        py_color.disable()
        cprint(py_color.format, 'this is disable')
        assert py_color.format is ''

    def test_colorstr(self):
        str1 = 'this is a test'
        py_color = PyColor('green')
        str2 = py_color.colorstr(str1)
        str3 = py_color.colorstr(str1, 'red')
        assert((str2 == '\033[0;32;40mthis is a test\033[0m') and
               (str3 == '\033[0;31;40mthis is a test\033[0m'))

#if __name__ == "__main__":
#    cprint('ugreen', 'hello edony')
#    printer('edony')
#    py_color = PyColor('green')
#    py_color.format = 'ucyan'
#    print(py_color.format)
#    cprint(py_color.format, 'this is test')
