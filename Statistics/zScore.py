from Statistics.Mean import mean
from Calculator.Subtraction import fn_subtraction
from Statistics.standard_Deviation import standard
from Calculator.Division import fn_division
import scipy.stats as stats


# closed form, return z given a sample and a datapoint from the sample
# z = (x - mean) / stdev; x is for raw score
def z(data, x):
    b = standard(data)
    c = mean(data)
    d = fn_subtraction(x, c)
    return round(fn_division(d, b), 5)


# open form, return z given the normal distribution and confidence interval
def z_given_confidence(p):
    z_score = round(stats.norm.ppf(1-(1-p)/2), 3)
    return z_score

