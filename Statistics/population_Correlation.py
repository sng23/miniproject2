import numpy


def p_correlation(data, data2):
    return round(numpy.corrcoef(data, data2)[0, 1], 4)
