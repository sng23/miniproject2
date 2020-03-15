from Statistics.Mean import mean
from numpy import absolute, asarray


def var(data):
    x = (absolute(asarray(data) - mean(data)))
    y = x **2
    z = mean(y)
    return round(z, 13)
# variance is the square of mean deviation
