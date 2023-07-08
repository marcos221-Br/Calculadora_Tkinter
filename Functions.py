#Funções utilizadas na calculadora
count = [None,None]
counterOperation = 0
counterDiv = 0

def alterSignal(display:str): #Altera o sinal do número que está sendo mostrado no display
    try:
        number = float(display.replace(',','.'))
        if (number%1) == 0:
            number = int(number)
        return str(number*-1).replace('.',',')
    except ValueError:
        print('Sem números no display')
        return ''

def operation(display:str,operator:str): #Seta a operação que vai ser feita
    try:
        global counterOperation, count, counterDiv
        counterDiv = 0
        if count[0] == None:
            count[0] = float(display.replace(',','.'))
            count[1] = operator
            return ''
        elif counterOperation == 1:
            count[0] = float(display.replace(',','.'))
            count[1] = operator
            counterOperation = 0
            return ''
        else:
            return result(display)
    except ValueError:
        print('Sem números no display')
        return ''

def result(display:str): #Mostra o resultado da conta
    try:
        global counterOperation, count
        if count[0] == None:
            return display
        result = operators[count[1]](count[0],float(display.replace(',','.')))
        if (counterOperation == 0):
            count[0] = float(display.replace(',','.'))
        counterOperation = 1
        if (result%1) == 0:
            return str(int(result))
        return str(round(result,13))
    except ValueError:
        print('Sem números no display')
        return ''
    except TypeError:
        if result == ZeroDivisionError:
            return 'Impossível dividir por 0'

def clear(): #Limpa todos os dados armazenados
    global count, counterOperation, counterDiv
    count = [None,None]
    counterOperation = 0
    counterDiv = 0

def minus(number1:float,number2:float): #Altera a forma de conta dependendo se o número é positivo ou negativo
    if number1 >= 0:
        return (number1 - number2)*-1
    return number1 - number2

def div(number1:float,number2:float): #Altera a forma da conta dependendo se é a primeira conta de divisão ou a segunda
    try:
        global counterDiv
        if counterDiv == 0:
            counterDiv = 1
            return number1 / number2
        return number2 / number1
    except ZeroDivisionError:
        return ZeroDivisionError

operators = {'+':lambda number1, number2:number1 + number2,
             '-':lambda number1, number2:minus(number1,number2),
             '*':lambda number1, number2:number1 * number2,
             '/':lambda number1, number2:div(number1,number2)}