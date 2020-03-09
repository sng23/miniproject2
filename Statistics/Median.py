#def mean(data):
 #   values = len(data)
  #  total = 0
   # for num in data:
    #    total = fn_addition(total, num)
     #   return fn_division(total, values)"""

from Calculator.Addition import fn_addition
from Calculator.Division import fn_division
from CsvReader import CsvReader


def median(data):
    data = []
    data.sort()
    values = len(data)
    total = 0
    for num in data:
        total = fn_addition(values, 1)
        return fn_division(total, 2)



