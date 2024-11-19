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
            # TODO: report to the user which values he's allowed to enter.
            print(INVALID_INPUT_MSG)