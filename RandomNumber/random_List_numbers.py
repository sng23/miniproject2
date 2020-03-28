from numpy.random import seed
from numpy.random import randint


def random_L0f_number(seedNum, min, max, number):
    seed(seedNum)
    Lof = []
    N = 1
    while N < number + 1:
        Lof.append(randint(min, max))
        N += 1
    return Lof

#lof = list of numbers



