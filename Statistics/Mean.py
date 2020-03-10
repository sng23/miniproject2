from Calculator.Addition import fn_addition
from Calculator.Division import fn_division
from pprint import pprint


def mean(data):
    values = len(data)
    total = 0

    for i in data:
        total = sum(data)
        return fn_division(total, values)
