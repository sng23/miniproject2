import unittest
from Calculator import Calculator
from CsvReader import CsvReader, ZeroDataException


class CsvReaderTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_csvreader(self):
        self.csv_reader = CsvReader('data/Unit Test CsvReader.txt')
        self.assertIsInstance(self.csv_reader, CsvReader)
        self.assertEqual(self.csv_reader.data.__len__(), 2)

    def test_zerolength(self):
        try:
            test_data = CsvReader('data/Unit Test Zero Length Datafile.csv').data
        except ZeroDataException:
            pass
        else:
            self.fail("Did not catch ZeroDataException.")

    def test_add(self):
        test_data = CsvReader('data/Unit Test Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)

    def test_subtract(self):
        test_data = CsvReader('data/Unit Test Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), result)

    def test_multiply(self):
        test_data = CsvReader('data/Unit Test Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)

    def test_division(self):
        test_data = CsvReader('data/Unit Test Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(round(self.calculator.divide(row['Value 2'], row['Value 1']), 9), result)

    def test_square(self):
        test_data = CsvReader('data/Unit Test Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)

    def test_squareroot(self):
        test_data = CsvReader('data/Unit Test Square Root.csv').data
        for row in test_data:
            data = row['Result']
            result = float(data)
            if "." in data:
                sigfigs = len(data.split('.')[1])
                self.assertEqual(round(self.calculator.squareroot(row['Value 1']), sigfigs), result)
            else:
                self.assertEqual(self.calculator.squareroot(row['Value 1']), result)


if __name__ == '__main__':
    unittest.main()
