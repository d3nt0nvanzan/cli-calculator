# BUG: always checks the user input. If I enter 'abc' it crashes. You correctly managed the operation selection but you missed the operands sanity checks.
# BUG: divide by 0 is not allowed.
# FIXME: everytime that you've done an operation, presents the user with the menu otherwise he doesn't know what operations to do
# FIXME: set a maximum value on number that you can manage. This choice is up to you as long as you've done proper researches.
# TODO: in case the application crashes I'd like to get the operations done so far (also the wrong one)
# [Q]: look better at how you can import stuff from other file with the Python mechanism
import sys
from checkInput import (checker, mathAnswer, equate) #imports checker function from checkInput.py
print('Welcome to the cli-calculator!')

#Asks users to select from the list to decide which program they would like to run
print('Please select which type of math problem you would like to run')
print('[1] Addition\n[2] Subtraction\n[3] Division\n[4] Multiplication\n[5] Power of X\n[0] Exit Program')
operations = []
while True:
    math = checker() #assigns the result of the checker() from checkInput.py to the math variable

    if math == 0:
        print('Goodbye!')
        print('Operations performed: ')
        for operation in operations:
            print(operation)
        sys.exit()

    if math == 5:
        firstNumber = int(input('Enter the base number: '))
        secondNumber = int(input('Enter the exponent: '))
    else:
        firstNumber = int(input('Enter first number: '))
        secondNumber = int(input('Enter second number: '))

    answer = mathAnswer(math, firstNumber, secondNumber) #assigns the result of mathAnswer() from checkInput.py to answer
    equation = equate(math) #assigns the result of equate() to from checkInput.py to equation
    operation = f'{firstNumber} {equation} {secondNumber} equals {answer}'
    operations.append(operation)

    print(operation)
                    
