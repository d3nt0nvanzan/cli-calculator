# FIXME: evaluate if we can separate functions over multiple files.
# FIXME: this file is called "checkInput" but it does more than that. Try to split further the content of this file.
# FIXME: get rid of magic strings around your code

# FIXME: some imports are marked as unused to me.
from enum import Enum
from decimal import Decimal, getcontext, Overflow
from messageAlerts import INVALID_SELECTION_MSG, INVALID_INPUT_MSG, INVALID_NUMBER_MSG
getcontext().prec = 10000


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