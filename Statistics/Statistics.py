from Calculator.Calculator import Calculator
from Statistics.mean_Absolute_Deviation import mad
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.standard_Deviation import standard
from Statistics.Variance import var
from Statistics.Skewness import skewness
from Statistics.zScore import z, z_given_p
from Statistics.Quartiles import quartiles
from Statistics.population_Correlation import p_correlation
from Statistics.MarginOfError import margin_of_error
from Statistics.ConfidenceIntervalSample import confidence_interval_sample
from Statistics.sample_Correlation import sample


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

    def test_z(self, data, x):
        self.result = z(data, x)
        return self.result

    def z_given_p(self, p):
        self.result = z_given_p(p)
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

    def margin_of_error(self, data, p):
        self.result = margin_of_error(data, p)
        return self.result

    def confidence_interval_sample(self, data, x):
        self.result = confidence_interval_sample(data, x)
        return self.result

    def test_sample(self, data, data2):
        self.result = sample(data, data2)
        return self.result
