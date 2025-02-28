# Cli Calculator

<!-- TODO: please stick to the Markdown syntax when you write .md files. Not addressed -->

## How to Run it

1. Ensure you have Python3 installed. You can download it here: <https://www.python.org/downloads/>
2. Run the program in the terminal using Python3: `python3 calculator.py`
    <!-- FIXME: this command is outdated. -->
3. Follow the on-screen prompts to select the type of math problem you would like to solve.

## HOW IT WORKS

When you run the program, it will display a menu with the following options:
   Please select the type of math problem you would like to run:  
   [+] Addition  
   [-] Subtraction  
   [/] Division  
   [*] Multiplication  
   [^] Power of X  
   [0] Exit Program  

* Enter the symbol corresponding to your choice
* If you choose '0' the program will exit
* If you choose any symbol other than the choices provided the program will exit
* If you choose a valid option you will be prompted to enter two numbers
* For the 'Power of X' the second number will be the exponent
The program will then display the result of the selected operation

---

## Example

Please select which type of math problem you would like to run:
[+] Addition
[-] Subtraction
[/] Division
[*] Multiplication
[^] Power of X
[0] Exit Program
Please select which type of math problem you would like to run: +
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
   * Open a terminal and navigate to the directory containing the program and `test_math.py`.
   * Run the tests using the following command:

   ```bash
   python3 -m unittest test_math.py

<!-- TODO work on this section -->
1. The outcome of the tests is:

    ```text
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.000s

    OK
    ```

2. Could you be a little bit more verbose? I have no idea about the tests I've run
3. Could you better explain the options we have to run the tests? What if I wanted to run a single test?
