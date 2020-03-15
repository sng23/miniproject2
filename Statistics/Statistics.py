from Calculator.Calculator import Calculator
from Statistics.mean_Absolute_Deviation import mad
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.standard_Deviation import standard
from Statistics.Variance import var
from Statistics.Skewness import skewness
from Statistics.zScore import z
from Statistics.Quartiles import quartiles
from Statistics.population_Correlation import p_correlation
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

    def test_stdev(self, data):
        self.result = standard(data)
        return self.result

    def test_variance(self, data):
        self.result = var(data)
        return self.result

    def test_z(self, data):
        self.result = z(data)
        return self.result

    def test_skew(self, data):
        self.result = skewness(data)
        return self.result

    def test_quartiles(self, data):
        self.result = quartiles(data)
        return self.result

    def test_p_correlation(self, data, data2):
        self.result = p_correlation(data, data2)
        return self.result
