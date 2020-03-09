from Calculator.Addition import fn_addition
from Calculator.Division import fn_division


def mean(data):
    numValues = len(data)
    sum = 0
    for num in data:
        sum = fn_addition(sum, num)
        return fn_division(sum, numValues)
