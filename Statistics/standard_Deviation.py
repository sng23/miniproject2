from numpy import std


def standard(data):
    v = std(data)
    return round(v, 3)