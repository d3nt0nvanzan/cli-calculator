import sys

def checker():    
    while True:
        try:
            math = int(input('Enter number for the type of Math problem please: '))
            if math > 5:
                print('Sorry, that is not a selection')
            elif math <= 5:
                return math
                
        except ValueError:
            print('Not an integer')
        

def mathAnswer(math, firstNumber, secondNumber):
    if math == 1:
        answer = firstNumber + secondNumber #Adding both number
    elif math == 2:
        answer = firstNumber - secondNumber #Subtracting both numbers
    elif math == 3:
        answer = firstNumber / secondNumber #Dividing both Numbers3
    elif math == 4:
        answer = firstNumber * secondNumber #Multiplying both Numbers
    elif math == 5:
        answer = firstNumber ** secondNumber #Raising to the power of X
    return answer

def equate(math):
    if math == 1:
        equation = 'plus'
    elif math == 2:
        equation = 'minus'
    elif math == 3:
        equation = 'divided by'
    elif math == 4:
        equation = 'times'
    elif math == 5:
        equation = 'to the power of'
    return equation