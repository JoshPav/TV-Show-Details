import requests 

API_KEY = "dff74ac126bbec75e5c44206cbad2ab6"
BASE_API_ENDPOINT = "https://api.themoviedb.org/3"

SEARCH_BY_NAME_ENDPOINT_PATH = "/search/tv"
GET_TV_SHOW_BY_ID_ENDPOINT_PATH = "/tv/{0}"

def search_for_shows_by_name(show_name):
    payload = {'api_key': API_KEY, 'query': show_name }
    return requests.get(url = BASE_API_ENDPOINT + SEARCH_BY_NAME_ENDPOINT_PATH, params = payload).json()

def get_tv_show_by_id(show_id):
    payload = {'api_key': API_KEY }
    return requests.get(url = BASE_API_ENDPOINT + GET_TV_SHOW_BY_ID_ENDPOINT_PATH.format(show_id), params = payload).json()
