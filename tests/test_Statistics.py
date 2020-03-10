import unittest
from Statistics.Statistics import Statistics


from Statistics.Statistics import mean
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # seed(5)
        # self.testData = randint(0, 10, 20)
        self.statistics = Statistics()
        self.data = (1, 2, 3, 4)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):

        self.assertEqual(self.statistics.mean(self.data), 2.5)

    def test_mad(self):
        self.assertEqual(self.statistics.mad(self.data), 1)

    if __name__ == '__main__':
        unittest.main()
