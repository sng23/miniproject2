from Calculator.Calculator import Calculator

from Statistics.Mean import Mean
from pprint import pprint


class Statistics(Calculator):

    def mean(self, data):
        self.result = Mean.mean(data)
        return self.result



