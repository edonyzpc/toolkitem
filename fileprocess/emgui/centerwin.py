import Tkinter as tkinter
from PIL import Image

class CenterWin(tkinter.Frame):
    def __init__(self, parent_win):
        tkinter.Frame.__init__(self, parent_win, background='white')
        self.parent_win = parent_win
        self.parent_win.title("center window")
        self.InitUI()
        self.pack(fill=tkinter.BOTH, expand=1)

    def InitUI(self):
        width = 290
        height = 150

        sw = self.parent_win.winfo_screenwidth()    # the screen width
        sh = self.parent_win.winfo_screenheight()   # the screen height

        x = (sw - width)/2
        y = (sh - height)/2
        self.parent_win.geometry("%dx%d+%d+%d"%(width, height, x, y))
        button = tkinter.Button(self, text="quit",command=self.quit)
        button.place(x=width/2,y=height/2)
        label = tkinter.Label(self, text="label text")
        label.pack()
        frame = tkinter.Frame(self, relief=tkinter.RAISED, borderwidth=1)
        frame.pack(after=label, side=tkinter.BOTTOM, fill=tkinter.X, expand=1)

if __name__ == "__main__":
    root = tkinter.Tk()
    app = CenterWin(root)
    app.mainloop()
