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

    def serialize(self):
        result = {
            "name": self.name,
            "pop": self.pop,
            "black_pop": self.black_pop,
            "black_per_capita": self.black_per_capita,
            "percent_searches": self.percent_searches,
            "total_searches": self.total_searches,
            "searches_per_capita": self.searches_per_capita,
            "home_search_ratio": self.home_search_ratio
        }

        return result

    def __repr__(self):
        return u'<Ward {}>'.format(self.name)
