# Cli Calculator

<!-- TODO: please stick to the Markdown syntax when you write .md files. -->

## How to Run it

1. Ensure you have Python3 installed. You can download it here: <https://www.python.org/downloads/>
1. Run the program in the terminal using Python3: `python3 calculator.py`
1. Follow the on-screen prompts to select the type of math problem you would like to solve.

## HOW IT WORKS

When you run the program, it will display a menu with the following options:
   Please select the type of math problem you would like to run:  
   [1] Addition  
   [2] Subtraction  
   [3] Division  
   [4] Multiplication  
   [5] Power of X  
   [0] Exit Program  

  * Enter the number corresponding to your choice
  * If you choose '0' the program will exit
  * If you choose any number other than the choices provided the program will exit
  * If you choose a valid option (1-5), you will be prompted to enter two numbers
  * For the 'Power of X' the second number will be the exponent
The program will then display the result of the selected operation
---
## Example

Please select which type of math problem you would like to run:
[1] Addition
[2] Subtraction
[3] Division
[4] Multiplication
[5] Power of X
[0] Exit Program
Enter number for the type of Math problem please: 1
You selected ADDITION
Enter first number: 5
You entered: 5
Enter second number (if you selected 5 this will be the exponent): 3
You entered: 3
5 plus 3 equals 8


## How to Test the Program

If you'd like to test the functionality of the program, you can use the `test_math.py` file included in this repository.

1. **Ensure the Test File is in the Same Directory**: Make sure the `test_math.py` file is in the same directory as the other program files.

2. **Run the Tests**:
   - Open a terminal and navigate to the directory containing the program and `test_math.py`.
   - Run the tests using the following command:

   ```bash
   python3 -m unittest test_math.py
