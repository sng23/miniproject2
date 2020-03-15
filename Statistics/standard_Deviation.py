from numpy import std


def standard(data, ddof=0):
    v = std(data, ddof=ddof)
    return round(v, 3)
