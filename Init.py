#Tela calculadora
from tkinter import *
import Functions as fc
import ctypes

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
        self.display = Entry(self.containerDisplay, justify='right', font=self.defaultFontDisplay,state='readonly')
        self.display.pack(fill=X)

        #Grade de botões
        buttonWidth = 4
        self.buttonClear = Button(self.containerNumpad, text='C', width=buttonWidth, font=self.defaultFontNumpad, command=self.clear)
        self.buttonClear.grid(row=1,column=3)

        self.number7 = Button(self.containerNumpad, text='7', width=buttonWidth, font=self.defaultFontNumpad)
        self.number7['command'] = lambda command='7':self.insertNumbers(number=command)
        self.number7.grid(row=3,column=1)

        self.number8 = Button(self.containerNumpad, text='8', width=buttonWidth, font=self.defaultFontNumpad)
        self.number8['command'] = lambda command='8':self.insertNumbers(number=command)
        self.number8.grid(row=3,column=2)

        self.number9 = Button(self.containerNumpad, text='9', width=buttonWidth, font=self.defaultFontNumpad)
        self.number9['command'] = lambda command='9':self.insertNumbers(number=command)
        self.number9.grid(row=3,column=3)

        self.number4 = Button(self.containerNumpad, text='4', width=buttonWidth, font=self.defaultFontNumpad)
        self.number4['command'] = lambda command='4':self.insertNumbers(number=command)
        self.number4.grid(row=4,column=1)

        self.number5 = Button(self.containerNumpad, text='5', width=buttonWidth, font=self.defaultFontNumpad)
        self.number5['command'] = lambda command='5':self.insertNumbers(number=command)
        self.number5.grid(row=4,column=2)

        self.number6 = Button(self.containerNumpad, text='6', width=buttonWidth, font=self.defaultFontNumpad)
        self.number6['command'] = lambda command='6':self.insertNumbers(number=command)
        self.number6.grid(row=4,column=3)

        self.number1 = Button(self.containerNumpad, text='1', width=buttonWidth, font=self.defaultFontNumpad)
        self.number1['command'] = lambda command='1':self.insertNumbers(number=command)
        self.number1.grid(row=5,column=1)

        self.number2 = Button(self.containerNumpad, text='2', width=buttonWidth, font=self.defaultFontNumpad)
        self.number2['command'] = lambda command='2':self.insertNumbers(number=command)
        self.number2.grid(row=5,column=2)

        self.number3 = Button(self.containerNumpad, text='3', width=buttonWidth, font=self.defaultFontNumpad)
        self.number3['command'] = lambda command='3':self.insertNumbers(number=command)
        self.number3.grid(row=5,column=3)

        self.number0 = Button(self.containerNumpad, text='0', width=buttonWidth, font=self.defaultFontNumpad)
        self.number0['command'] = lambda command='0':self.insertNumbers(number=command)
        self.number0.grid(row=6,column=2)

        self.signal = Button(self.containerNumpad, text='+/-', width=buttonWidth, font=self.defaultFontNumpad, command=self.alterSignal)
        self.signal.grid(row=6,column=1)

        self.comma = Button(self.containerNumpad, text=',', width=buttonWidth, font=self.defaultFontNumpad, command=self.numberOfComma)
        self.comma.grid(row=6,column=3)

        self.buttonResult = Button(self.containerNumpad, text='=', width=buttonWidth, font=self.defaultFontNumpad, command=self.result)
        self.buttonResult.grid(row=6,column=4)

        self.sum = Button(self.containerNumpad, text='+', width=buttonWidth, font=self.defaultFontNumpad)
        self.sum['command'] = lambda command='+':self.operator(operator=command)
        self.sum.grid(row=5,column=4)

        self.mult = Button(self.containerNumpad, text='*', width=buttonWidth, font=self.defaultFontNumpad)
        self.mult['command'] = lambda command='*':self.operator(operator=command)
        self.mult.grid(row=3,column=4)

        self.minus = Button(self.containerNumpad, text='-', width=buttonWidth, font=self.defaultFontNumpad)
        self.minus['command'] = lambda command='-':self.operator(operator=command)
        self.minus.grid(row=4,column=4)

        self.div = Button(self.containerNumpad, text='/', width=buttonWidth, font=self.defaultFontNumpad)
        self.div['command'] = lambda command='/':self.operator(operator=command)
        self.div.grid(row=2,column=4)

        self.sqrt = Button(self.containerNumpad, text='√x', width=buttonWidth, font=self.defaultFontNumpad)
        self.sqrt['command'] = lambda command='√x':self.uniqueOperation(operator=command)
        self.sqrt.grid(row=2,column=3)

        self.pow = Button(self.containerNumpad, text='x²', width=buttonWidth, font=self.defaultFontNumpad)
        self.pow['command'] = lambda command='x²':self.uniqueOperation(operator=command)
        self.pow.grid(row=2,column=2)

        self.frac = Button(self.containerNumpad, text='1/x', width=buttonWidth, font=self.defaultFontNumpad)
        self.frac['command'] = lambda command='1/x':self.uniqueOperation(operator=command)
        self.frac.grid(row=2,column=1)

        self.clearDisplay = Button(self.containerNumpad, text='CE', width=buttonWidth, font=self.defaultFontNumpad)
        self.clearDisplay['command'] = lambda command='CE':self.display.delete(0,END)
        self.clearDisplay.grid(row=1,column=2)

        self.erase = Button(self.containerNumpad, text='\u21E6', width=buttonWidth, font=self.defaultFontNumpad, command=self.removeLastCharacter)
        self.erase.grid(row=1,column=4)

        self.percent = Button(self.containerNumpad, text='%', width=buttonWidth, font=self.defaultFontNumpad)
        self.percent['command'] = lambda command='%':self.uniqueOperation(operator=command)
        self.percent.grid(row=1,column=1)

        #Funções do teclado
        self.number0.bind_all('<KeyPress-0>',self.insertNumbers)
        self.number1.bind_all('<KeyPress-1>',self.insertNumbers)
        self.number2.bind_all('<KeyPress-2>',self.insertNumbers)
        self.number3.bind_all('<KeyPress-3>',self.insertNumbers)
        self.number4.bind_all('<KeyPress-4>',self.insertNumbers)
        self.number5.bind_all('<KeyPress-5>',self.insertNumbers)
        self.number6.bind_all('<KeyPress-6>',self.insertNumbers)
        self.number7.bind_all('<KeyPress-7>',self.insertNumbers)
        self.number8.bind_all('<KeyPress-8>',self.insertNumbers)
        self.number9.bind_all('<KeyPress-9>',self.insertNumbers)

        self.buttonClear.bind_all('<Delete>',self.clear)
        self.signal.bind_all('<F9>',self.alterSignal)
        self.comma.bind_all('<KeyPress-,>',self.numberOfComma)
        self.buttonResult.bind_all('<Return>',self.result)
        self.buttonResult.bind_all('<KeyPress-=>',self.result)
        self.erase.bind_all('<BackSpace>',self.removeLastCharacter)

        self.sum.bind_all('<KeyPress-+>',self.operator)
        self.minus.bind_all('<KeyPress-->',self.operator)
        self.mult.bind_all('<KeyPress-*>',self.operator)
        self.div.bind_all('<KeyPress-/>',self.operator)

        self.sqrt.bind_all('<KeyPress-r>',self.uniqueOperation)
        self.frac.bind_all('<KeyPress-f>',self.uniqueOperation)
        self.pow.bind_all('<KeyPress-e>',self.uniqueOperation)
        self.percent.bind_all('<KeyPress-p>',self.uniqueOperation)

    def alterSignal(self,event=None): #Altera o sinal do número
        self.display['state'] = 'normal'
        number = self.display.get()
        self.display.delete(0,END)
        self.display.insert(INSERT,fc.alterSignal(number))
        self.display['state'] = 'readonly'
    
    def operator(self,event=None,operator:str=''): #Seleciona o operador que vai ser utilizado na conta
        display = self.display.get()
        self.display['state'] = 'normal'
        self.display.delete(0,END)
        self.display.insert(INSERT,fc.operation(display,event,operator))
        self.display['state'] = 'readonly'
    
    def clear(self,event=None): #Limpa o display e as variáveis
        self.display['state'] = 'normal'
        self.display.delete(0,END)
        fc.clear()
        self.display['state'] = 'readonly'

    def numberOfComma(self,event=None): #Limita o número de virgulas que pode ter no número
        self.display['state'] = 'normal'
        self.display.insert(INSERT,fc.commaFinder(self.display.get()))
        self.display['state'] = 'readonly'
    
    def result(self,event=None): #Mostra o resultado da conta
        self.display['state'] = 'normal'
        display = self.display.get()
        self.display.delete(0,END)
        self.display.insert(INSERT,fc.result(display))
        self.display['state'] = 'readonly'
    
    def uniqueOperation(self,event=None,operator:str=''): #Mostra resultado para contas com apenas um número
        self.display['state'] = 'normal'
        display = self.display.get()
        self.display.delete(0,END)
        self.display.insert(INSERT,fc.uniqueOperation(display,event,operator))
        self.display['state'] = 'readonly'
    
    def insertNumbers(self,event=None,number:str=''): #Realiza verificações antes de inserir números
        self.display['state'] = 'normal'
        display = self.display.get()
        self.display.delete(0,END)
        self.display.insert(INSERT,fc.insertVerification(display,event,number))
        self.display['state'] = 'readonly'
    
    def removeLastCharacter(self,event=None): #Remove o ultimo número do display
        self.display['state'] = 'normal'
        display = self.display.get()
        self.display.delete(0,END)
        self.display.insert(INSERT,fc.eraser(display))
        self.display['state'] = 'readonly'

init = Tk() #Atribui os comandos do iniciador do tkinter a init
init.geometry('310x385') #Tamanho da janela
init.resizable(False,False) #Não deixa o usuário alterar o tamanho da janela
init.title('Calculadora') #Titulo do programa
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Calculator') #Seta o icone da TaskBar como o mesmo da aplicação
init.iconphoto(True,PhotoImage(file=r'Images\icon.ico')) #Seta o icone da aplicação
Main(init) #Seta a classe inicial
init.mainloop() #Inicia o programa