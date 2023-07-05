from tkinter import *
from tkinter import font

class Main:
    def __init__(self,master):
        self.defaultFont = ('Verdana')

        self.containerDisplay = Frame(master)
        self.containerDisplay.pack(fill=X)
        self.containerNumpad = Frame(master, background='black')
        self.containerNumpad.pack(side=LEFT, fill='both')
        
        self.display = Entry(self.containerDisplay, justify='right', font=self.defaultFont)
        self.display.pack(fill=X)

init = Tk()
init.geometry('200x200')
Main(init)
init.mainloop()