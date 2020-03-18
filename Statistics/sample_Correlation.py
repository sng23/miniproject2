import numpy
import random
from RandomNumber.Random import seed_number_list
from RandomNumber.Random import seed_Int
from RandomNumber.Random import seed_Numbers
from RandomNumber.Random import list_with_seed
from Statistics.standard_Deviation import standard

from pprint import pprint


def sample(sample1, data):
    return round(numpy.corrcoef(sample1, data)[0, 1], 4)

