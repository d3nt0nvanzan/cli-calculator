from messageAlerts import ZERO_DIVISION_ERROR_MSG, INVALID_NUMBER_MSG

# Class to represent math operations
class MathOperation:
    ADD = "+"
    SUBTRACT = "-"
    DIVIDE = "/"
    MULTIPLY = "*"
    EXPONENTIATE = "^"

# Function to perform the selected math operation
def calculate(math_operation, firstNumber, secondNumber):
    match math_operation:
        case MathOperation.ADD:
            return firstNumber + secondNumber
        case MathOperation.SUBTRACT:
            return firstNumber - secondNumber
        case MathOperation.MULTIPLY:
            return firstNumber * secondNumber
        case MathOperation.DIVIDE:
            if secondNumber == 0:
                raise ZeroDivisionError(ZERO_DIVISION_ERROR_MSG)
            return firstNumber / secondNumber
        case MathOperation.EXPONENTIATE:
            return firstNumber ** secondNumber
        case _:
            raise ValueError(INVALID_NUMBER_MSG)
        
    # FIXME: change the branches with returns. Use the switch construct
    # if math_operation == MathOperation.ADD:
    #     answer = firstNumber + secondNumber 
    # elif math_operation == MathOperation.SUBTRACT:
    #     answer = firstNumber - secondNumber 
    # elif math_operation == MathOperation.DIVIDE:
    #     if secondNumber == 0:
    #         raise ZeroDivisionError(ZERO_DIVISION_ERROR_MSG)
    #     answer = firstNumber / secondNumber 
    # elif math_operation == MathOperation.MULTIPLY:
    #     answer = firstNumber * secondNumber
    # elif math_operation == MathOperation.EXPONENTIATE:
    #     answer = firstNumber ** secondNumber 
    # return answer 