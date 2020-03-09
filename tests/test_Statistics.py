import unittest
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

   # def test_mean(self):
    #    mean = self.statistics.mean(self.testData)
     #   self.assertEqual(mean, 38.95)



    if __name__ == '__main__':
     unittest.main()