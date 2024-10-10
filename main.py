# BUG: always checks the user input. If I enter 'abc' it crashes. You correctly managed the operation selection but you missed the operands sanity checks. When I messed with operands, you should keep selection and not ask again what operation would you like to perform. - Not addressed. To repro it: select Addition, then input "c" as first operand.
# [Q]: look better at how you can import stuff from other file with the Python mechanism - Not addressed synce Style is not used here. On my IDE is grayed out.
import sys
import colorama
from colorama import Fore, Back, Style
from getOperation import getOperationSelected
from messageAlerts import INVALID_NUMBER_MSG, NUMBER_TOO_LARGE_MSG, ZERO_DIVISION_ERROR_MSG
from mathAnswer import mathAnswer
from equate import equate
from decimal import Decimal, getcontext, Overflow

colorama.init(autoreset=True)

MAX_VALUE = 10**5

getcontext().prec = 10000

print('Welcome to the cli-calculator!')

#Asks users to select from the list to decide which program they would like to run
operations = []

try:

    while True:
        print(Fore.WHITE + Back.CYAN + 'Please select which type of math problem you would like to run')
        print(Fore.GREEN + Back.WHITE+  '[1] Addition\n[2] Subtraction\n[3] Division\n[4] Multiplication\n[5] Power of X\n[0] Exit Program')

        math = getOperationSelected() #assigns the result of the checker() from checkInput.py to the math variable
        if math == 0:
            print(Fore.GREEN + 'Goodbye!')
            print(Fore.GREEN + 'Operations performed: ')
            for operation in operations:
                print(operation)
            sys.exit()
        
        try:
            if math == 5:
                while True:
                    try:
                        firstNumber = Decimal(input('Enter the base number (MAX Number is 100000): '))
                        if abs(firstNumber) > MAX_VALUE:
                          print(Back.RED + NUMBER_TOO_LARGE_MSG)
                        else:
                            break
                    except ValueError:
                        print(Back.RED + INVALID_NUMBER_MSG)

                while True:
                    try:     
                        secondNumber = Decimal(input('Enter the exponent (MAX Number is 100000): '))
                        if abs(secondNumber) > MAX_VALUE:
                            print(Back.RED + NUMBER_TOO_LARGE_MSG)
                        else:
                            break
                    except ValueError:
                            print(Back.RED + INVALID_NUMBER_MSG)

            else:
                while True:
                    try:
                        firstNumber = Decimal(input('Enter first number (MAX Number is 100000): '))
                        if abs(firstNumber) > MAX_VALUE:
                            print(Back.RED + NUMBER_TOO_LARGE_MSG)
                        else:
                            break
                    except ValueError:
                        print(Back.RED + INVALID_NUMBER_MSG)

                while True:
                    try:
                        secondNumber = Decimal(input('Enter second number (MAX Number is 100000): '))
                        if abs(secondNumber) > MAX_VALUE:
                            print(Back.RED + NUMBER_TOO_LARGE_MSG)
                        else:
                            if math == 3 and secondNumber == 0:
                                print(Back.RED + ZERO_DIVISION_ERROR_MSG)
                            else:
                                break
                    except ValueError:
                        print(Back.RED + INVALID_NUMBER_MSG) 
                    
            answer = mathAnswer(math, firstNumber, secondNumber) #assigns the result of mathAnswer() from checkInput.py to answer
            equation = equate(math) #assigns the result of equate() to from checkInput.py to equation
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
        print(Fore.RED + operations)
    sys.exit(1)
