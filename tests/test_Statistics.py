import unittest
from Statistics.Statistics import Statistics

from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # seed(5)
        # self.testData = randint(0, 10, 20)
        self.statistics = Statistics()
        self.data = [2, 1, 3, 3, 4, 5]
        self.data2 = [1, 5, 6, 9, 11, 3]

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
        self.assertEqual(self.statistics.test_z(self.data, 25), 17.04105)

    def test_z_given_p(self):
        self.assertEqual(self.statistics.z_given_p(0.80), 1.282)
        self.assertEqual(self.statistics.z_given_p(0.85), 1.440)
        self.assertEqual(self.statistics.z_given_p(0.90), 1.645)
        self.assertEqual(self.statistics.z_given_p(0.95), 1.960)
        self.assertEqual(self.statistics.z_given_p(0.99), 2.576)
        self.assertEqual(self.statistics.z_given_p(0.995), 2.807)
        self.assertEqual(self.statistics.z_given_p(0.999), 3.291)
        self.assertRaises(KeyError, self.statistics.z_given_p(0.875))

    def test_skew(self):
        self.assertEqual(self.statistics.test_skew(self.data), 0)

    def test_quartiles(self):
        self.assertEqual(self.statistics.test_quartiles(self.data), [2.25, 3, 3.75])

    def test_pCon(self):
        self.assertEqual(self.statistics.test_p_correlation(self.data, self.data2), 0.2287)

    def test_margin_of_error(self):
        self.assertEqual(self.statistics.margin_of_error(self.data, 0.95), 1.033)

    def test_confidence_interval_sample(self):
        self.assertEqual(self.statistics.confidence_interval_sample(self.data, 0.95), (1.869, 4.131))

    if __name__ == '__main__':
        unittest.main()
