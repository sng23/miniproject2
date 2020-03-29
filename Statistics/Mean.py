from Calculator.Addition import fn_addition
from Calculator.Division import fn_division


def mean(data):
    values = len(data)
    total = 0

    for i in data:
        total = fn_addition(total, i)
    return fn_division(total, values)


