import requests 
from models.TvListResultObject import TvListResultObject
from tabulate import tabulate


API_KEY="dff74ac126bbec75e5c44206cbad2ab6"
BASE_API_ENDPOINT="https://api.themoviedb.org/3"


# Seach for tv series to get the correct id



def get_tv_id_from_show_name(name):
    ENDPOINT_PATH = "/search/tv"
    
    payload = {'api_key':API_KEY, 
                'query': name} 
    
    r = requests.get(url = BASE_API_ENDPOINT + ENDPOINT_PATH, params = payload) 
    
    data = r.json()
    
    results = data['results']
    result_objects = []
    table = []
    for index, result in enumerate(results):
        obj = TvListResultObject(result['id'], result['name'], result['overview'])
        result_objects.append(obj)
        table.append(obj.get_table_row(index+1))
    
    table_headers = [" ","Name", "Overview"]
    print(tabulate(table, headers=table_headers, tablefmt="grid", numalign="center"))
    
    print(get_choice("Please enter the corresponding choice: ", len(result_objects)))

        
def get_choice(question, max_index):
    choice = 0
    choices = list(map(str, range(1, max_index+1)))
    while choice not in choices:
        choice = input(question).strip()
    return choice
    
    
#show_name = input("Enter the name of the TV Series to find: ")
    
get_tv_id_from_show_name("Silicon Valley")