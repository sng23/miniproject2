from Calculator.Calculator import Calculator
from Sampling.DataLoader import DataLoader
from Statistics import Statistics


def cochran_small(n_0, N):
    calc = Calculator()
    return round(calc.divide(n_0, 1 + calc.divide(n_0 - 1, N)), 0)


def cochran_large(proportion, me, confidence):
    calc = Calculator()
    z = Statistics.z_given_confidence(confidence)
    z_2 = calc.square(z)
    e_2 = calc.square(me)
    n_0 = calc.divide(calc.multiply(calc.multiply(z_2, proportion), 1-proportion), e_2)
    return round(n_0, 0)


# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/find-sample-size/
# https://www.tarleton.edu/academicassessment/documents/Samplesize.pdf
class SampleSize(DataLoader):

    def __init__(self):
        self.calc = Calculator()
        pass

    def cochran_small(self, n_0, N):
        return cochran_small(n_0, N)

    def cochran_large(self, proportion, marginerror, confidence):
        return cochran_large(proportion, marginerror, confidence)

    def cochran(self, N, proportion, marginerror, confidence):
        n_0 = cochran_large(proportion, marginerror, confidence)
        if N >= 500:
            return n_0
        else:
            return cochran_small(n_0, N)

    def find_n_size_unknown_sigma(self, confidence_p, interval_width, n_pct_of_N ):
        z = Statistics.z_given_confidence(confidence_p)
        E = self.calc.divide(interval_width, 2)
        p_hat = n_pct_of_N
        q_hat = 1 - p_hat
        pq = self.calc.multiply(p_hat, q_hat)
        result = self.calc.multiply(self.calc.square(self.calc.divide(z, E)), pq)
        return round(result, 0)

    def find_n_size_given_sigma(self, confidence_p, sigma, me):
        z = Statistics.z_given_confidence(confidence_p)
        zsig = self.calc.multiply(z, sigma)
        result = self.calc.square(self.calc.divide(zsig, me))
        return round(result, 0)
