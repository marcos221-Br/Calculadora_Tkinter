from tkinter import *

class Main:
    def __init__(self,master):
        self.containerBack = Label(master, background='RED', text='Vermelho')
        self.containerBack.pack(fill=X)

init = Tk()
init.geometry('200x200')
Main(init)
init.mainloop()