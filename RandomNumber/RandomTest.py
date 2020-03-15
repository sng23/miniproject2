import unittest
import random
from random import randint
from RandomNumber.Random import noSeed, noSeed_Decimal, seed_Int, seed_Decimal
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


if __name__ == '__main__':
    unittest.main()
