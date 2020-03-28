import numpy


def sample(sample1, sample2):
    return round(numpy.corrcoef(sample1, sample2)[0, 1], 4)
