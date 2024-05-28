import sys

# FIXME: improve this name
def checker():    
    while True:
        try:
            # BUG: handle the negative numbers
            math = int(input('Enter number for the type of Math problem please: '))
            if math > 5:
                print('Sorry, that is not a selection')
            elif math <= 5:
                return math
                
        except ValueError:
            print('Not an integer')
        

def mathAnswer(math, firstNumber, secondNumber):
    # FIXME: look something called Enum that are a defined range of values with underlying int value.
    # https://docs.python.org/3/library/enum.html#module-enum
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
    # FIXME: stick to a switch case, it's prettier
    # FIXME: you could also use a map[key]value
    # FIXME: in other languages is called dictionary (C#) or maps (Go) or dynamic arrays (PHP)
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