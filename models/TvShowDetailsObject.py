class TvShowDetailsObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.overview = response['overview']  
        self.number_of_seasons = response['number_of_seasons']
        self.networks = self.parse_networks(response['networks'])
        self.seasons = self.parse_seasons(response['seasons'])
        self.genres = self.parse_genres(response['genres'])

    def parse_networks(self, networks_response):
        networks = []
        for network_response in networks_response:
            networks.append(NetworkObject(network_response))
        return networks
    
    def parse_seasons(self, seasons_response):
        seasons = []
        for season_response in seasons_response:
            seasons.append(SeasonObject(season_response))
        return seasons
    
    def parse_genres(self, genres_response):
        genres = []
        for genre_response in genres_response:
            genres.append(GenreObject(genre_response))
        return genres
            
class GenreObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']       
class NetworkObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']        
class SeasonObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.season_number = response['season_number']
        self.overview = response['overview']
        self.episode_count = response['episode_count']
        self.air_date = response['air_date']