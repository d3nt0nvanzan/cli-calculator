from decimal import getcontext
from messageAlerts import INVALID_SELECTION_MSG, INVALID_INPUT_MSG
getcontext().prec = 10000

operations = {"+", "-", "*", "/", "^", "0"}

def getOperationSelected():
    
    while True:
        try:
            math = input('Enter symbol for the type of Math problem please: ')

            if math not in operations:
                print(INVALID_SELECTION_MSG)
            else:
                return math
        except ValueError:
            print(INVALID_INPUT_MSG)