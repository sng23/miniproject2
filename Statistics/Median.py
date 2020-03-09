

from Calculator.Addition import fn_addition
from Calculator.Division import fn_division


def median(data):
    data = []
    data.sort()
    total = 0
    for num in data:
        total = fn_addition(data, 1)
        return fn_division(total, 2)

#median formula (n+1)/2
