import csv
from collections import defaultdict

file_name = 'annual-enterprise-survey-2021-financial-year-provisional-csv.csv'


def count_keys(csv_file):
    key_count = defaultdict(int)
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            key = f"{row['Industry_code_NZSIOC']}#{row['Variable_code']}"
            key_count[key] += 1

    return {k: v for k, v in key_count.items() if v > 1}


result = count_keys(file_name)

for key, count in result.items():
    # print(f"{key}: {count}")
    print('')


class CountKeys:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.file = open(self.csv_file, mode='r')
        self.reader = csv.DictReader(self.file)
        self.key_count = defaultdict(int)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            row = next(self.reader)
            key = f"{row['Industry_code_NZSIOC']}#{row['Variable_code']}"
            self.key_count[key] += 1
            return {key: self.key_count[key]}
        except StopIteration:
            self.file.close()
            raise StopIteration


clas_result = CountKeys(file_name)

for result in clas_result:
    # print(result)
    print('')
