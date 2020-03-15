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


# Generate a list of N random numbers with a seed - Integer
def seed_Numbers():
    seed(3)
    for _ in range(10):
        value = randint(0, 10)
        print(value)


# Generate a list of N random numbers with a seed - Decimal
def seed_Numbers_Decimal():
    seed(0.6)
    for _ in range(10):
        value = random.uniform(0, 10)
        print(value)


# Select a random item from a list
def number_list():
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return random.choice(value)


# Set a seed and randomly.select the same value from a list
def seed_number_list():
    seed(9)
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return random.choice(value)


# Select N number of items from a list without a seed
def seedNo_number_list():
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for value in range(20):
        value = random.randint(1, 20)
        print(value)


# select N number of items from a list with a seed
def list_with_seed():
    value = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    seed(4)
    for value in range(30):
        value = random.randint(11, 20)
        print(value)
