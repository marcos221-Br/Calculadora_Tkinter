#Funções utilizadas na calculadora
def alterSignal(display): #Altera o sinal do número que está sendo mostrado no display
    try:
        number = float(display.replace(',','.'))
        if (number%1) == 0:
            number = int(number)
        return str(number*-1).replace('.',',')
    except ValueError:
        print('Sem números no display')
        return ''