import sys
if sys.version.startswith('3.4'):
    import tkinter
else:
    import Tkinter as tkinter

def frame(root, side):
    w = tkinter.Frame(root)
    w.pack(side=side, expand=tkinter.YES, fill=tkinter.BOTH)
    return w
def button(root, side, text, command=None):
    w = tkinter.Button(root, text=text, command=command)
    w.pack(side=side, expand=tkinter.YES, fill=tkinter.BOTH)
    return w
class Calculator(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calc1")
        display = tkinter.StringVar()
        tkinter.Entry(self, relief=tkinter.SUNKEN, textvariable=display).pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
        for key in ("123", "456", "789", "-0."):
            keyF = frame(self, tkinter.TOP)
            for char in key:
                button(keyF, tkinter.LEFT, char, lambda w=display, s='%s'%char: w.set(w.get()+s))
        opsF = frame(self, tkinter.TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, tkinter.LEFT, char)
                btn.bind('<ButtonRelease-1>',
                        lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, tkinter.LEFT, char,
                        lambda w=display, c=char: w.set(w.get()+' '+c+' '))
        clearF = frame(self, tkinter.BOTTOM)
        button(clearF, tkinter.LEFT, 'Clr', lambda w=display: w.set(''))
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except ValueError:
            display.set("ERROR")
if __name__ == '__main__':
    Calculator().mainloop()
