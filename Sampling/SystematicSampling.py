import random
from typing import overload

from Sampling.DataLoader import DataLoader


class SampleRequestLargerThanDataset(Exception):
    pass


def ss(test_data, n, k, start):
    # get n systematic samples from test_data
    if n > len(test_data):
        raise SampleRequestLargerThanDataset
    samples = []
    i_next = rand = random.randint(1, len(test_data)) - 1
    for i in range(1, n+1):
        selected = test_data.pop(i_next)
        samples.append(selected)
        i_next = i_next+k-1
        if i_next != 0 and i_next > len(test_data) - 1:
            i_next = (len(test_data)-1) % i_next
    return samples


class SystematicSampling(DataLoader):

    def __init__(self):
        pass

    def ss(self, n, k=None):
        start = random.randint(1, len(self.test_data)) - 1
        if not k:
            k = random.randint(1, len(self.test_data))
        return ss(self.test_data, n, k, start)
