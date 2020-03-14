
from scipy import stats
from Statistics.Mean import mean
from Calculator.Subtraction import fn_subtraction
from numpy import std
from Statistics.standard_Deviation import standard
from Calculator.Division import fn_division


#z = (x - mean) / stdev; x is for raw score
def z(data):
    x = 25
    b = standard(data)
    c = mean(data)
    d = fn_subtraction(x, c)
    return round(fn_division(d, b), 5)

