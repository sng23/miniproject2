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
