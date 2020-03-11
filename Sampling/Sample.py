import random
from typing import overload
from Sampling.DataLoader import DataLoader


class SampleRequestLargerThanDataset(Exception):
    pass


class Sample(DataLoader):

    def __init__(self):
        pass

    @overload
    def srs(self, n):
        return self.srs(self.test_data, n)

    def srs(self, test_data, n):
        # get n random samples from test_data
        list_copy = self.test_data
        if n > len(list_copy):
            raise SampleRequestLargerThanDataset
        samples = []
        for i in range(1, n+1):
            rand = random.randint(1, len(list_copy)) - 1
            selected = list_copy.pop(rand)
            samples.append(selected)
        return samples

