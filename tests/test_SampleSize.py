import unittest
from Sampling.SampleSize import SampleSize


class SampleSizeTests(unittest.TestCase):

    def setUp(self):
        self.sample_size = SampleSize()

    def test_instantiate(self):
        self.assertIsInstance(self.sample_size, SampleSize)

    def test_cochran_large(self):
        self.assertEqual(self.sample_size.cochran_large(0.50, 0.05, 0.95), 384)

    def test_cochran_small(self):
        self.assertEqual(self.sample_size.cochran_small(385, 2000), 323)

    def test_cochran(self):
        self.assertEqual(self.sample_size.cochran(2000, 0.50, 0.05, 0.95), 384)

    def test_find_n_size_unknown_sigma(self):
        self.assertEqual(self.sample_size.find_n_size_unknown_sigma(0.95, 0.06, 0.41), 1033)

    def test_find_n_size_given_sigma(self):
        self.assertEqual(self.sample_size.find_n_size_given_sigma(0.99, 2.9, 0.5), 223)


if __name__ == '__main__':
    unittest.main()
