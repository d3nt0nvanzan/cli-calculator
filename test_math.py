import unittest
from mathAnswer import calculate, MathOperation
from equate import equate
from decimal import Decimal, getcontext

class TestCalculator(unittest.TestCase):

    def setUp(self):
        getcontext().prec = 10000
    
    def test_addition(self):
        result = calculate(MathOperation.ADD, Decimal('10'), Decimal('5'))
        self.assertEqual(result, Decimal('15'))
    
    def test_subtraction(self):
        result = calculate(MathOperation.SUBTRACT, Decimal('10'), Decimal('5'))
        self.assertEqual(result, Decimal('5'))
    
    def test_multiplication(self):
        result = calculate(MathOperation.MULTIPLY, Decimal('10'), Decimal('5'))
        self.assertEqual(result, Decimal('50'))
    
    def test_division(self):
        result = calculate(MathOperation.DIVIDE, Decimal('10'), Decimal('2'))
        self.assertEqual(result, Decimal('5'))
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(MathOperation.DIVIDE, Decimal('10'), Decimal('0'))

    def test_exponentiation(self):
        result = calculate(MathOperation.EXPONENTIATE, Decimal('2'), Decimal('3'))
        self.assertEqual(result, Decimal('8'))

    def test_equate(self):
        result = equate('+')
        self.assertEqual(result, 'plus')

        result = equate('-')
        self.assertEqual(result, 'minus')

        result = equate('*')
        self.assertEqual(result, 'times')

        result = equate('/')
        self.assertEqual(result, 'divided by')

        result = equate('^')
        self.assertEqual(result, 'to the power of')

        result = equate('invalid')
        self.assertEqual(result, 'Invalid operation')

if __name__ == '__main__':
    unittest.main()
