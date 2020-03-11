
from Statistics.Mean import mean


def median(data):
    data.sort()
    if len(data) % 2 != 0:
        center = int((len(data) - 1) / 2)
        return data[center]
    elif len(data) % 2 == 0:
        center1 = int(len(data) / 2)
        center2 = int(len(data) / 2) - 1
        return int(mean([data[center1], data[center2]]))
