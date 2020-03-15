import unittest
from Sampling.DataLoader import DataLoader


class DataLoaderTests(unittest.TestCase):

    def setUp(self):
        self.data_loader = DataLoader()
        self.data_path = 'data/Unit Test Addition.csv'

    def test_instantiate(self):
        self.assertIsInstance(self.data_loader, DataLoader)

    def test_load_data(self):
        test_data = self.data_loader.load_data(self.data_path)
        self.assertEqual(test_data, self.data_loader.test_data)