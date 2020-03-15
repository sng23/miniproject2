import unittest
import random
from random import randint
from RandomNumber.Random import noSeed, noSeed_Decimal
from RandomNumber import Random
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = noSeed()

    def test_instantiate_random(self):
        self.assertIsInstance(self.random, Random)

    def test_noSeed(self):
        self.assertLessEqual(noSeed(), 100)
        pprint(noSeed())

    def test_noSeed_Decimal(self):
        self.assertLessEqual(noSeed(), 100)
        pprint(noSeed_Decimal())


if __name__ == '__main__':
    unittest.main()
