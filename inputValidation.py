from decimal import Decimal
from colorama import Back
from messageAlerts import INVALID_NUMBER_MSG, NUMBER_TOO_LARGE_MSG, ZERO_DIVISION_ERROR_MSG
from mathAnswer import MathOperation

MAX_VALUE = 10**5

def get_valid_number(prompt: str, math_op=None) -> Decimal:
    while True:
        try:
            user_input = input(prompt)

            if any(c.isalpha() for c in user_input):
                print(Back.RED + INVALID_NUMBER_MSG)
                continue

            if ',' in user_input:
                print(Back.RED + "Commas are not allowed. Please use a period (.) for decimals.")
                continue
            
            if user_input.count('.') > 1:
                print(Back.RED + "Too many decimal points. Please enter a valid number.")
                continue
            
            number = Decimal(user_input)

            if abs(number) > MAX_VALUE:
                print(Back.RED + NUMBER_TOO_LARGE_MSG)
                continue

            if math_op == MathOperation.DIVIDE and number == 0:
                print(Back.RED + ZERO_DIVISION_ERROR_MSG)
                continue

            return number

        except ValueError:
            print(Back.RED + INVALID_NUMBER_MSG)
            continue
