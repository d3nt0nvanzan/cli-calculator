def equate(math):
    math_operations = {
        '+': 'plus',
        '-': 'minus',
        '/': 'divided by',
        '*': 'times',
        '^': 'to the power of'
    }
    return math_operations.get(math, 'Invalid operation')