import random
import string



def calculate(a, b , operator):
    mapping_dict = {
        'add': '+',
        'mul': '*',
        'div': '/',
        'min': '-'}
    result = '{}{}{}'.format(a, mapping_dict[operator], b)
    return eval(result)

def transfer_strings(strings, type):
    mapping_dict = {
        'upper': 'upper()',
        'lower': 'lower()'
    }
    result = "'{}'.{}".format(strings, mapping_dict[type])
    return eval(result)

def random_string():
    strings = ''.join(random.sample(string.ascii_letters, 8))
    return strings

