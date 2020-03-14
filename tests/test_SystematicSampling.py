import unittest
from Sampling.SystematicSampling import SystematicSampling, SampleRequestLargerThanDataset
from CsvReader import CsvReader


class SystematicSamplingTests(unittest.TestCase):

    def setUp(self):
        self.ss = SystematicSampling()
        self.data_path = 'data/patient 10 records.csv'

    def test_instantiate(self):
        self.assertIsInstance(self.ss, SystematicSampling)

    def test_ss_unique(self):
        n = 7
        self.ss.load_data(self.data_path)
        samples = self.ss.ss(n)

        samples_sorted = sorted(samples, key=lambda i: i['id'])
        last = ""
        for row in samples_sorted:
            if row["id"] == last:
                self.fail('Duplicate row found in sample')
            last = row["id"]

    def test_ss_n(self):
        n = 10
        self.ss.load_data(self.data_path)
        samples = self.ss.ss(n)
        self.assertEqual(n, len(samples))

    def test_ss_n_too_large(self):
        n = 11
        try:
            self.ss.load_data(self.data_path)
            samples = self.ss.ss(n)
        except SampleRequestLargerThanDataset:
            pass
        else:
            self.fail("Did not catch SampleRequestLargerThanDataset.")


if __name__ == '__main__':
    unittest.main()
