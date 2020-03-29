import csv


class ZeroDataException(Exception):
    pass


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
            if len(self.data) == 0:
                raise ZeroDataException("Datafile is zero length")
        pass
