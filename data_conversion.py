import csv

from models import Ward


def get_ward_data():
    # Returns a list of ward dicts
    ward_data = []
    with open('data/dc_percentage.csv') as dc_ward_raids:
        csv_reader = csv.reader(dc_ward_raids)
        next(csv_reader)

        ward_data.extend([Ward(row[0], row[1], row[2],
                         row[3], row[4], row[5],
                         row[6], row[7]) for row in csv_reader])
    return ward_data
