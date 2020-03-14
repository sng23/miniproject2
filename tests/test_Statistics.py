import unittest
from Statistics.Statistics import Statistics

from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # seed(5)
        # self.testData = randint(0, 10, 20)
        self.statistics = Statistics()
        self.data = [2, 1, 3, 3, 4, 5]
        self.raw_score = 25

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):

        self.assertEqual(self.statistics.mean(self.data), 3)

    def test_mad(self):
        self.assertEqual(self.statistics.mad(self.data), 1)

    def test_middle(self):
        self.assertEqual(self.statistics.middle(self.data), 3)

    def test_mode(self):
        self.assertEqual(self.statistics.test_mode(self.data), 3)

    def test_stdev(self):
        self.assertEqual(self.statistics.test_stdev(self.data), 1.291)

    def test_var(self):
        self.assertEqual(self.statistics.test_variance(self.data), 1.6666666666667)

    def test_z(self):
        self.assertEqual(self.statistics.test_z(self.data), 17.04105)

    def test_skew(self):
        self.assertEqual(self.statistics.test_skew(self.data), 0)

    def test_quartiles(self):
        self.assertEqual(self.statistics.test_quartiles(self.data), [2.25, 3, 3.75])
    if __name__ == '__main__':
        unittest.main()
