from Calculator.Calculator import Calculator
from Statistics.mean_Absolute_Deviation import mad
from Statistics.Mean import mean
from pprint import pprint


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mad(self, data):
        self.result = mad(data)
        return self.result



