from Calculator.Calculator import Calculator
from Statistics.mean_Absolute_Deviation import mad
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from pprint import pprint


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mad(self, data):
        self.result = mad(data)
        return self.result

    def middle(self, data):
        self.result = median(data)
        return self.result

    def test_mode(self, data):
        self.result = mode(data)
        return self.result

