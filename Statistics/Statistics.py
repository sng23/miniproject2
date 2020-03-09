from Calculator.Calculator import Calculator
from CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __int__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()


