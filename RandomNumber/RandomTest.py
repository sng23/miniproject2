import unittest
import random
from random import seed
from random import randint
from RandomNumber.Random import noSeed, noSeed_Decimal, seed_Int, seed_Decimal, seed_Numbers, seed_Numbers_Decimal, \
    number_list, seed_number_list, seedNo_number_list, list_with_seed

from RandomNumber import Random
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = noSeed()

    def test_noSeed(self):
        self.assertGreaterEqual(noSeed(), 0)
        self.assertLessEqual(noSeed(), 100)
        pprint("number without seed in Integer")
        pprint(noSeed())


    def test_noSeed_Decimal(self):
        self.assertGreaterEqual(noSeed_Decimal(), 0)
        self.assertLessEqual(noSeed_Decimal(), 100)
        pprint("number without seed in Decimal")
        pprint(noSeed_Decimal())

    def test_seed_Int(self):
        self.assertGreaterEqual(seed_Int(), 0)
        self.assertLessEqual(seed_Int(), 100)
        pprint("number with seed in Integer")
        pprint(seed_Int())

    def test_seed_Decimal(self):
        self.assertGreaterEqual(seed_Decimal(), 0)
        self.assertLessEqual(seed_Decimal(), 100)
        pprint(" number with seed in Decimal")
        pprint(seed_Decimal())

    def test_seed_Number_Int(self):
        self.assertIs(seed_Numbers(), seed_Numbers())
        pprint("list of N random numbers with a seed - Integer")
        pprint(seed_Numbers())

    def test_seed_Number_Decimal(self):
        self.assertIs(seed_Numbers_Decimal(), seed_Numbers_Decimal())
        pprint("list of N random numbers with a seed - Decimal")
        pprint(seed_Numbers_Decimal())

    def test_Number_list(self):
        self.assertGreaterEqual(number_list(), 0)
        pprint("random item from a list")
        pprint(number_list())

    def test_seed_list(self):
        self.assertIs(seed_number_list(), seed_number_list())
        pprint("seed and randomly.select the same value from a list")
        pprint(seed_number_list())

    def test_NOSeed_list(self):
        self.assertIs(seedNo_number_list(), seedNo_number_list())
        pprint("N number of items from a list without a seed")
        pprint(seedNo_number_list())

    def test_numberList(self):
        self.assertIs(list_with_seed(), list_with_seed())
        pprint(" N number of items from a list with a seed")
        pprint(list_with_seed())


if __name__ == '__main__':
    unittest.main()
