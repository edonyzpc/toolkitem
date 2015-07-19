import sys
if sys.version.startswith("2.7."):
    import Tkinter as tkinter 
elif sys.version.startswith("3.4."):
    import tkinter
from PIL import Image
from PIL import ImageTk


class GIFWin(tkinter.Label):
    def __init__(self, master, filename):
        self.im = Image.open(filename)
        self.master = master
        self.seq = []
        try:
            while 1:
                self.seq.append(self.im.copy())
                self.im.seek(len(self.seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = self.im.info['duration']
        except KeyError:
            self.delay = 100
        self.first = self.seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(self.first)]
        tkinter.Label.__init__(self, self.master, image=self.frames[0])

        temp = self.seq[0]
        for image in self.seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))
        self.idx = 0
        self.cancel = self.after(self.delay, self.Play)
        #self.button = tkinter.Button(self.master, text='stop', command=Stop)

    def Play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.Play)        

    def Stop(self):
        self.after_cancel(self.cancel)

def GUI(filename):
    root = tkinter.Tk()
    root.title("GIF Viewer")
    anim = GIFWin(root, filename)
    anim.grid(row=0, columnspan=3, sticky=tkinter.N)
    fram = tkinter.LabelFrame(root, text="info")
    fram.grid(column=0, columnspan=2, rowspan=2, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    labtext_1 = tkinter.Label(fram, text="File: ")
    labtext_1.grid(row=1, column=0, sticky=tkinter.W)
    labtext_11 = tkinter.Label(fram,text=anim.im.filename)
    labtext_11.grid(row=1, column=1, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    labtext_2 = tkinter.Label(fram,text="GIF Delay: ")
    labtext_2.grid(row=2, column=0, sticky=tkinter.W)
    labtext_22 = tkinter.Label(fram,text=anim.im.info["duration"])
    labtext_22.grid(row=2, column=1, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    button = tkinter.Button(root, text="stop", command=anim.Stop)
    button.grid(row=1, column=2, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    button_q = tkinter.Button(root, text="quit", command=root.destroy)
    button_q.grid(row=2, column=2, sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    root.mainloop()

if __name__ == "__main__":
    GUI(sys.argv[1])
