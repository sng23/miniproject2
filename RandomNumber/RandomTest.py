import unittest
import random
from random import seed
from random import randint
from RandomNumber.Random import noSeed, noSeed_Decimal, seed_Int, seed_Decimal, seed_Numbers, seed_Numbers_Decimal, \
    number_list
from RandomNumber import Random
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = noSeed()

    def test_instantiate_random(self):
        self.assertIsInstance(self.random, Random)

    def test_noSeed(self):
        self.assertGreaterEqual(noSeed(), 0)
        self.assertLessEqual(noSeed(), 100)
        pprint(noSeed())

    def test_noSeed_Decimal(self):
        self.assertGreaterEqual(noSeed_Decimal(), 0)
        self.assertLessEqual(noSeed_Decimal(), 100)
        pprint(noSeed_Decimal())

    def test_seed_Int(self):
        self.assertGreaterEqual(seed_Int(), 0)
        self.assertLessEqual(seed_Int(), 100)
        print(seed_Int())

    def test_seed_Decimal(self):
        self.assertGreaterEqual(seed_Decimal(), 0)
        self.assertLessEqual(seed_Decimal(), 100)
        print(seed_Decimal())

    def test_seed_Number_Int(self):
        self.assertIs(seed_Numbers(), None)
        print(seed_Numbers())

    def test_seed_Number_Decimal(self):
        self.assertIs(seed_Numbers_Decimal(), None)
        print(seed_Numbers_Decimal())

    def test_Number_list(self):
        self.assertGreaterEqual(number_list(), 0)
        print(number_list())


if __name__ == '__main__':
    unittest.main()
