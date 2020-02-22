
class TvShowDetailsObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.overview = response['overview']  
        self.number_of_episodes = response['number_of_episodes']
        self.number_of_seasons = response['number_of_seasons']
        self.original_language = response['original_language']
        self.original_name = response['original_name']
        self.popularity = response['popularity']
        self.poster_path = response['poster_path']
        self.status = response['status']
        self.type = response['type']
        self.vote_average = response['vote_average']
        self.vote_count = response['vote_count']       
        self.backdrop_path = response['backdrop_path']       
        self.first_air_date = response['first_air_date']       
        self.homepage = response['homepage']       
        self.in_production = response['in_production']   
        self.languages = response['languages']
        self.origin_countrys = response['origin_country']
        self.last_episode_to_air = LastEpisodeToAirObject(response['last_episode_to_air'])
        self.networks = self.parse_networks(response['networks'])
        self.seasons = self.parse_seasons(response['seasons'])
        self.genres = self.parse_genres(response['genres'])
        self.episode_run_time = response['episode_run_time']
        self.created_by = self.parse_created_by(response['created_by'])
        self.production_companies = self.parse_production_companies(response['production_companies'])

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
    
    def parse_production_companies(self, production_companies_response):
        production_companies = []
        for production_company_response in production_companies_response:
            production_companies.append(ProductionCompanyObject(production_company_response))
        return production_companies
    
    def parse_created_by(self, created_by_response):
        created_by = []
        for created_by_response in created_by_response:
            created_by.append(GenreObject(created_by_response))
        return created_by
    
class LastEpisodeToAirObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.overview = response['overview']
        self.episode_number = response['episode_number']
        self.production_code = response['production_code']
        self.season_number = response['season_number']
        self.show_id = response['show_id']
        self.still_path = response['still_path']
        self.vote_average = response['vote_average']
        self.vote_count = response['vote_count']

class GenreObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']

class CreatedByObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.credit_id = response['credit_id']
        self.gender = response['gender']
        self.profile_path = response['profile_path']
        
class NetworkObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.logo_path = response['logo_path']
        self.origin_country = response['origin_country']
        
class SeasonObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.season_number = response['season_number']
        self.overview = response['overview']
        self.poster_path = response['poster_path']
        self.episode_count = response['episode_count']
        self.air_date = response['air_date']
        
class ProductionCompanyObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.origin_country = response['origin_country']
        self.logo_path = response['logo_path']