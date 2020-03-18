import unittest
from Sampling.Cochran import Cochran


class CochranTests(unittest.TestCase):

    def setUp(self):
        self.cochran = Cochran()

    def test_instantiate(self):
        self.assertIsInstance(self.cochran, Cochran)

    def test_cochran_large(self):
        self.assertEqual(self.cochran.cochran_large(0.50, 0.05, 0.95), 384)

    def test_cochran_small(self):
        self.assertEqual(self.cochran.cochran_small(385, 2000), 323)

    def test_cochran(self):
        self.assertEqual(self.cochran.cochran(2000, 0.50, 0.05, 0.95), 384)


if __name__ == '__main__':
    unittest.main()
