# FIXME: evaluate if we can separate functions over multiple files.
# FIXME: get rid of magic strings around your code

from enum import Enum

def getOperationSelected():
    while True:
        try:
            math = int(input('Enter number for the type of Math problem please: '))

            if math < 0 or math > 5:
                print('Sorry, this is not a selection (please type something between 0 and 5)')
            else:
                return math
        except ValueError:
            print('Invalid input. Please enter an integer.')
        
        

def mathAnswer(math, firstNumber, secondNumber):
    class MathOperation(Enum):
        # BUG: start from zero
        ADD = 1
        SUBTRACT = 2
        DIVIDE = 3
        MULTIPLY = 4
        EXPONENTIATE = 5


    math_operation = MathOperation(math)
    
    # FIXME: change the branches with returns. Use the switch construct
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
    math_operations = {
        1: 'plus',
        2: 'minus',
        3: 'divided by',
        4: 'times',
        5: 'to the power of'
    }
    return math_operations.get(math, 'Invalid operation')