def equate(math):
    math_operations = {
        1: 'plus',
        2: 'minus',
        3: 'divided by',
        4: 'times',
        5: 'to the power of'
    }
    return math_operations.get(math, 'Invalid operation')