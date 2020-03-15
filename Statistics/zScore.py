
from scipy import stats
from Statistics.Mean import mean
from Calculator.Subtraction import fn_subtraction
from numpy import std
from Statistics.standard_Deviation import standard
from Calculator.Division import fn_division


# z = (x - mean) / stdev; x is for raw score
def z(data, x):
    b = standard(data)
    c = mean(data)
    d = fn_subtraction(x, c)
    return round(fn_division(d, b), 5)


def z_given_p(p):
    switch = {
        0.80: 1.282,
        0.85: 1.440,
        0.90: 1.645,
        0.95: 1.960,
        0.99: 2.576,
        0.995: 2.807,
        0.999: 3.291
    }
    return switch.get(p)
