import csv
import random
from CsvReader import CsvReader
from typing import overload


class SampleRequestLargerThanDataset(Exception):
    pass


class Sample:

    test_data = []

    def __init__(self):
        pass

    def load_data(self, filepath):
        test_data = CsvReader(filepath).data
        self.test_data = test_data
        return test_data

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

