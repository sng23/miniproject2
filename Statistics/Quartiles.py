import numpy


def quartiles(data):
    x = numpy.quantile(data, .25)
    y = numpy.quantile(data, .50)
    z = numpy.quantile(data, .75)
    return [x, y, z]

    # x = len(data)
    # q1 = .25 * (x + 1)
    # q2 = median(data)
    # q3 = .75 * (x + 1)

    # return [q1, q2, q3]
