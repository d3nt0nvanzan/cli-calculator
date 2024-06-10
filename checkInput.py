from enum import Enum

# FIXME: improve this name
def selectionCheck():    
    while True:
        try:
            # BUG: handle the negative numbers
            math = int(input('Enter number for the type of Math problem please: '))

            if math < 0 or math > 5:
                print('Sorry, this is not a selection')
            else:
                return math
        except ValueError:
            print('Invalid input. Please enter an integer.')
        
        

def mathAnswer(math, firstNumber, secondNumber):
    class MathOperation(Enum):
        ADD = 1
        SUBTRACT = 2
        DIVIDE = 3
        MULTIPLY = 4
        EXPONENTIATE = 5


    # FIXME: look something called Enum that are a defined range of values with underlying int value.
    # https://docs.python.org/3/library/enum.html#module-enum
    math_operation = MathOperation(math)
    
    if math_operation == MathOperation.ADD:
        answer = firstNumber + secondNumber 
    elif math_operation == MathOperation.SUBTRACT:
        answer = firstNumber - secondNumber 
    elif math_operation == MathOperation.DIVIDE:
        if secondNumber == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        answer = firstNumber / secondNumber 
    elif math_operation == MathOperation.MULTIPLY:
        answer = firstNumber * secondNumber
    elif math_operation == MathOperation.EXPONENTIATE:
        answer = firstNumber ** secondNumber 
    return answer  
            

def equate(math):
    # FIXME: stick to a switch case, it's prettier
    # FIXME: you could also use a map[key]value
    # FIXME: in other languages is called dictionary (C#) or maps (Go) or dynamic arrays (PHP)
    math_operations = {
        1: 'plus',
        2: 'minus',
        3: 'divided by',
        4: 'times',
        5: 'to the power of'
    }
    return math_operations.get(math, 'Invalid operation')