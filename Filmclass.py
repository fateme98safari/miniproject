from mediaclass import Media
class Film(Media):
    def __init__(self,year):
        super().__init__()
        self.year_of_film_production=year
