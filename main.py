import sys
import colorama
from colorama import Fore, Back
from getOperation import getOperationSelected
from messageAlerts import INVALID_NUMBER_MSG, NUMBER_TOO_LARGE_MSG, ZERO_DIVISION_ERROR_MSG
from mathAnswer import calculate, MathOperation
from equate import equate
from logo import logo
from decimal import Decimal, getcontext, Overflow

colorama.init(autoreset=True)
MAX_VALUE = 10**5
getcontext().prec = 10000

print(logo)
print('Welcome to the cli-calculator!')

operations = []  # To track performed operations

try:
    
    while True:
        print(Fore.WHITE + Back.CYAN + 'Please select which type of math problem you would like to run')
        print(Fore.GREEN + Back.WHITE + '[+] Addition\n[-] Subtraction\n[/] Division\n[*] Multiplication\n[^] Power of X\n[0] Exit Program')

        math = getOperationSelected()
        if math == "0":
            print(Fore.GREEN + 'Goodbye!')
            print(Fore.GREEN + 'Operations performed: ')
            for operation in operations:
                print(operation)
            sys.exit()

        while True:
            try:
                # FIXME: this could be a function because it's repeated with the 'second number' code                
                # FIXME: if I type '2,2' as first number, it crashes. You can handle that by either prompting the user again or converting the "," to a "."
                user_input = input('Enter first number (MAX Number is 100000): ')
                if any(c.isalpha() for c in user_input):  # Check for alphabetic characters
                    print(Back.RED + INVALID_NUMBER_MSG)
                    continue
                firstNumber = Decimal(user_input)  # Convert only after alpha check
                if abs(firstNumber) > MAX_VALUE:
                    print(Back.RED + NUMBER_TOO_LARGE_MSG)
                    continue
                break  # Valid input, exit loop
            except ValueError:
                print(Back.RED + INVALID_NUMBER_MSG)
                continue

        while True:
            try:
                user_input = input('Enter second number (MAX Number is 100000): ')
                if any(c.isalpha() for c in user_input):
                    print(Back.RED + INVALID_NUMBER_MSG)
                    continue
                secondNumber = Decimal(user_input)
                if abs(secondNumber) > MAX_VALUE:
                    print(Back.RED + NUMBER_TOO_LARGE_MSG)
                elif math == MathOperation.DIVIDE and secondNumber == 0:
                    print(Back.RED + ZERO_DIVISION_ERROR_MSG)
                    continue
                break
            except ValueError:
                print(Back.RED + INVALID_NUMBER_MSG)
                continue

        try:
            answer = calculate(math, firstNumber, secondNumber)
            equation = equate(math)
            operation = Fore.GREEN + f'{firstNumber} {equation} {secondNumber} equals {answer}'
        except (ValueError, NameError) as e:
            operation = Back.RED + f"Invalid input: {e}"
        except ZeroDivisionError as e:
            operation = Back.RED + f"Error: {e}"
        except Overflow as e:
            operation = Back.RED + f"Numerical result out of range: {e}"

        operations.append(operation)
        print(operation)

except KeyboardInterrupt:
    print(Back.RED + "\nProcess interrupted by user.")
    print(Fore.GREEN + 'Operations performed before interruption: ')
    for operation in operations:
        print(operation)
    sys.exit(0)

except Exception as e:
    print(Back.RED + f"An error occurred: {e}")
    print(Back.RED + "Operations performed before the crash:")
    for operation in operations:
        print(Fore.RED + operation)
    sys.exit(1)
