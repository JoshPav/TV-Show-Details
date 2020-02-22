import textwrap 

class TvListResultObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.overview = response['overview']
        self.poster_path = response['poster_path']
        self.popularity = response['popularity']
        self.backdrop_path = response['backdrop_path']
        self.vote_average = response['vote_average']
        self.first_air_date = response['first_air_date']
        self.origin_country = response['origin_country']
        self.genre_ids = response['genre_ids']
        self.original_language = response['original_language']
        self.vote_count = response['vote_count']
        self.original_name = response['original_name']

    def get_table_row(self, index):
        wrapper = textwrap.TextWrapper(width=100)         
        return [index, self.name, "\n".join(wrapper.wrap(self.overview))]