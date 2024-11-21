# TODO: this file must be deleted.
# FIXME: this file is called "checkInput" but it does more than that. Try to split further the content of this file.
# FIXME: get rid of magic strings around your code

# FIXME: some imports are marked as unused to me.
from enum import Enum
from decimal import Decimal, getcontext, Overflow

getcontext().prec = 10000

INVALID_SELECTION_MSG = 'Sorry, this is not a selection (please type something between 0 and 5)'
INVALID_INPUT_MSG = 'Invalid input. Please enter an integer.'
ZERO_DIVISION_ERROR_MSG = "Cannot divide by zero"
INVALID_NUMBER_MSG = 'Not a number. Please enter a number.'
NUMBER_TOO_LARGE_MSG = "Number is too large."

def getOperationSelected():
    while True:
        try:
            math = int(input('Enter number for the type of Math problem please: '))

            # FIXME: you're still using numbers (magic numbers) here.
            if math < 0 or math > 5:
                print(INVALID_SELECTION_MSG)
            else:
                return math
        except ValueError:
            print(INVALID_INPUT_MSG)
        
        

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
            raise ZeroDivisionError(ZERO_DIVISION_ERROR_MSG)
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