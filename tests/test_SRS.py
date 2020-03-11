import unittest
from Sampling.SRS import SRS, SampleRequestLargerThanDataset
from CsvReader import CsvReader


class SRSTests(unittest.TestCase):

    def setUp(self):
        self.srs = SRS()
        self.data_path = 'data/patient.csv'

    def test_instantiate(self):
        self.assertIsInstance(self.srs, SRS)

    def test_srs(self):
        n = 7382
        self.srs.load_data(self.data_path)
        samples = self.srs.srs(n)
        self.assertEqual(n, len(samples))

        samples_sorted = sorted(samples, key=lambda i: i['id'])
        last = ""
        for row in samples_sorted:
            if row["id"] == last:
                self.fail('Duplicate row found in sample')
            last = row["id"]

    def test_srs_n_too_large(self):
        n = 7383
        try:
            self.srs.load_data(self.data_path)
            samples = self.srs.srs(n)
        except SampleRequestLargerThanDataset:
            pass
        else:
            self.fail("Did not catch SampleRequestLargerThanDataset.")


if __name__ == '__main__':
    unittest.main()
