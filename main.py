# TODO: need to work again on point 4 of the "requirements.md" file. You've to list all of the operations done in the session. 
# BUG: always checks the user input. If I enter 'abc' it crashes
#import sys library
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
                    
