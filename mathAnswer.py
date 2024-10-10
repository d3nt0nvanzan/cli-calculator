from enum import Enum
from decimal import Decimal, getcontext, Overflow

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