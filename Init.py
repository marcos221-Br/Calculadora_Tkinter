from tkinter import *

class Main: #Classe inicial
    def __init__(self,master):
        #Fontes utilizadas
        self.defaultFontDisplay = ('Verdana', init.winfo_width()*30)
        self.defaultFontNumpad = ('Verdana', init.winfo_width()*20)

        #Containeres
        self.containerDisplay = Frame(master)
        self.containerDisplay.pack(fill=X)
        self.containerNumpad = Frame(master)
        self.containerNumpad.pack(side=LEFT, fill='both')

        #Tela em que aparecerá a conta e resultado
        self.display = Entry(self.containerDisplay, justify='right', font=self.defaultFontDisplay, )
        self.display.pack(fill=X)

        #Grade de botões
        buttonWidth = 4
        self.clear = Button(self.containerNumpad, text='C', width=buttonWidth, font=self.defaultFontNumpad)
        self.clear['command'] = lambda command='clear':self.display.delete(0,END)
        self.clear.grid(row=1,column=3)

        self.number7 = Button(self.containerNumpad, text='7', width=buttonWidth, font=self.defaultFontNumpad)
        self.number7['command'] = lambda command='7':self.display.insert(INSERT,command)
        self.number7.grid(row=2,column=1)

        self.number8 = Button(self.containerNumpad, text='8', width=buttonWidth, font=self.defaultFontNumpad)
        self.number8['command'] = lambda command='8':self.display.insert(INSERT,command)
        self.number8.grid(row=2,column=2)

        self.number9 = Button(self.containerNumpad, text='9', width=buttonWidth, font=self.defaultFontNumpad)
        self.number9['command'] = lambda command='9':self.display.insert(INSERT,command)
        self.number9.grid(row=2,column=3)

        self.number4 = Button(self.containerNumpad, text='4', width=buttonWidth, font=self.defaultFontNumpad)
        self.number4['command'] = lambda command='4':self.display.insert(INSERT,command)
        self.number4.grid(row=3,column=1)

        self.number5 = Button(self.containerNumpad, text='5', width=buttonWidth, font=self.defaultFontNumpad)
        self.number5['command'] = lambda command='5':self.display.insert(INSERT,command)
        self.number5.grid(row=3,column=2)

        self.number6 = Button(self.containerNumpad, text='6', width=buttonWidth, font=self.defaultFontNumpad)
        self.number6['command'] = lambda command='6':self.display.insert(INSERT,command)
        self.number6.grid(row=3,column=3)

        self.number1 = Button(self.containerNumpad, text='1', width=buttonWidth, font=self.defaultFontNumpad)
        self.number1['command'] = lambda command='1':self.display.insert(INSERT,command)
        self.number1.grid(row=4,column=1)

        self.number2 = Button(self.containerNumpad, text='2', width=buttonWidth, font=self.defaultFontNumpad)
        self.number2['command'] = lambda command='2':self.display.insert(INSERT,command)
        self.number2.grid(row=4,column=2)

        self.number3 = Button(self.containerNumpad, text='3', width=buttonWidth, font=self.defaultFontNumpad)
        self.number3['command'] = lambda command='3':self.display.insert(INSERT,command)
        self.number3.grid(row=4,column=3)
        
        self.signal = Button(self.containerNumpad, text='+/-', width=buttonWidth, font=self.defaultFontNumpad, command=self.alterSignal)
        self.signal.grid(row=5,column=1)

        self.number0 = Button(self.containerNumpad, text='0', width=buttonWidth, font=self.defaultFontNumpad)
        self.number0['command'] = lambda command='0':self.display.insert(INSERT,command)
        self.number0.grid(row=5,column=2)

        self.comma = Button(self.containerNumpad, text=',', width=buttonWidth, font=self.defaultFontNumpad, command=self.numberOfComma)
        self.comma.grid(row=5,column=3)

        self.result = Button(self.containerNumpad, text='=', width=buttonWidth, font=self.defaultFontNumpad, command=self.countResult)
        self.result.grid(row=5,column=4)
    
    def alterSignal(self):
        number = float(self.display.get().replace(',','.'))
        if (number%1) == 0:
            number = int(number)
        self.display.delete(0,END)
        if number>0:
            self.display.insert(INSERT,'-')
            self.display.insert(INSERT,'{}'.format(number).replace('.',','))
        else:
            number *= -1
            self.display.insert(INSERT,'{}'.format(number).replace('.',','))

    def numberOfComma(self):
        if self.display.get() == '':
            return
        if self.display.get().find(',') == -1:
            self.display.insert(INSERT,',')
    
    def countResult(self):
        count = ['','','']
        operadores = {'+':lambda num1, num2: num1 + num2,
                      '-':lambda num1, num2: num1 - num2,
                      '*':lambda num1, num2: num1 * num2,
                      '/':lambda num1, num2: num1 / num2}
        j = 0
        for i in self.display.get():
            if ((i == '+') or (i == '-') or (i == '*') or (i == '/')) and (count[0] != '') and (count[1] == ''):
                j += 1
                count[j] = i
                j += 1
            else:
                count[j] = count[j] + i
        self.display.delete(0,END)
        result = operadores[count[1]](float(count[0]),float(count[2]))
        self.display.insert(INSERT,'{}'.format(result))

init = Tk()
init.geometry('310x400')
init.resizable(False,False)
Main(init)
init.mainloop()