from CsvReader import CsvReader


class DataLoader:

    test_data = []

    def __init__(self):
        pass

    def load_data(self, filepath):
        test_data = CsvReader(filepath).data
        self.test_data = test_data
        return test_data

