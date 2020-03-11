import random
from Sampling.DataLoader import DataLoader


class SampleRequestLargerThanDataset(Exception):
    pass


def srs(test_data, n):
    # get n random samples from test_data
    if n > len(test_data):
        raise SampleRequestLargerThanDataset
    samples = []
    for i in range(1, n+1):
        rand = random.randint(1, len(test_data)) - 1
        selected = test_data.pop(rand)
        samples.append(selected)
    return samples


class Sample(DataLoader):

    def __init__(self):
        pass

    def srs(self, n):
        return srs(self.test_data, n)

