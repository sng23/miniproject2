from Statistics.Mean import mean
from Calculator.Subtraction import fn_subtraction
from Statistics.standard_Deviation import standard
from Calculator.Division import fn_division


class POutOfRangeException(Exception):
    pass


# closed form, return z given a sample and a datapoint from the sample
# z = (x - mean) / stdev; x is for raw score
def z(data, x):
    b = standard(data)
    c = mean(data)
    d = fn_subtraction(x, c)
    return round(fn_division(d, b), 5)


# open form, return z given the normal distribution and confidence p
def z_given_p(p):
    if not 0.0 <= p <= 1.0:
        raise POutOfRangeException

    switch = {
        0.05: -1.645,
        0.1: 0.125,
        0.2: 0.26,
        0.3: 0.385,
        0.4: 0.525,
        0.5: 0.675,
        0.6: 0.84,
        0.7: 1.02,
        0.8: 1.282,
        0.9: 1.645,
        0.95: 1.960,
        0.99: 2.576,
        0.995: 2.807,
        0.999: 3.291
    }

    try:
        z_score = switch[p]
    except KeyError:
        z_score = switch.get(round(p, 1))

    return z_score
