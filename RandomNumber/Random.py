import random
from random import randint, seed


# Generates a number without seed in Integer
def noSeed():
    return random.randint(0, 100)


# Generates a number without seed in Decimal
def noSeed_Decimal():
    return random.uniform(0, 100)


# Generates a number with seed in Integer
def seed_Int():
    seed(53)
    return random.randint(0, 100)


# Generates a number with seed in Decimal
def seed_Decimal():
    seed(12)
    return random.uniform(0, 10)


# Generate a list of N random numbers with a seed
def seed_Numbers():
    seed(3)
    for _ in range(10):
        value = randint(0, 10)
        print(value)
