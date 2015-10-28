import csv

class Ward(object):
    pass


def get_ward_data():
    # Returns a list of ward dicts
    with open('data/dc_percentage.csv') as dc_ward_raids:

        csv_reader = csv.reader(dc_ward_raids)

        for row in csv_reader:
            print row

    return
