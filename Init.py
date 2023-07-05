from tkinter import *

class Main:
    def __init__(self,master):
        self.containerDisplay = Frame(master, background='RED')
        self.containerDisplay.pack(fill=X)
        self.defaultFont = ('Verdana',13)

        self.display = Entry(self.containerDisplay, justify='right', font=self.defaultFont)
        self.display.pack()

init = Tk()
init.geometry('200x200')
Main(init)
init.mainloop()