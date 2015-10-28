import csv


class Ward(object):
    def __init__(self, name, pop, black_pop,
                 black_per_capita, percent_searches,
                 total_searches, searches_per_capita,
                 home_search_ratio):
        self.name = name
        self.pop = pop
        self.black_pop = black_pop
        self.black_per_capita = black_per_capita
        self.percent_searches = percent_searches
        self.total_searches = total_searches
        self.searches_per_capita = searches_per_capita
        self.home_search_ratio = home_search_ratio

    def __repr__(self):
        return u'<Ward {}>'.format(self.name)


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
