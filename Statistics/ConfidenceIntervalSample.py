from Statistics.mean_Absolute_Deviation import mean
from Statistics.MarginOfError import margin_of_error


# me = z (s/ sqrt(n))
def confidence_interval_sample(data, x):
    me = margin_of_error(data, x, 1)
    x_bar = mean(data)
    return x_bar - me, x_bar + me
