
from numpy import absolute, asarray
from Statistics.Mean import mean


def mad(data):
    return mean(absolute(asarray(data) - mean(data)))