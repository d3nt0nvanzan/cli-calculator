#let user know that they need Python 3 to run program
print('Before continuing you must have Python 3 to run this program')
#Asks users to select from the list to decide which program they would like to run
print('Please select which type of math problem you would like to run')
print('[1] Addition\n[2] Subtraction\n[3] Division\n[4] Multiplication\n[5] Power of X')

#Takes the input from the user from the list provided
math = int(input('Enter number for the type of Math problem please: '))
firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number (if you selected 5 this will be the exponent): '))

#If they choose addition
if math == 1:
    answer = firstNumber + secondNumber #Adding both numbers
elif math == 2:
    answer = firstNumber - secondNumber #Subtracting both numbers
elif math == 3:
    answer = firstNumber / secondNumber #Dividing both Numbers
elif math == 4:
    answer = firstNumber * secondNumber #Multiplying both Numbers
elif math == 5:
    answer = firstNumber ** secondNumber #Rasing to the power of X
    

print(answer)
                    
