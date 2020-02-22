from models.TvListResultObject import TvListResultObject
from tabulate import tabulate
import ApiGateway
from models.TvShowDetailsObject import TvShowDetailsObject

def print_result_object_table(rows):
    table_headers = [" ","Name", "Overview"]
    print(tabulate(rows, headers=table_headers, tablefmt="grid", numalign="center", stralign="center"))

def get_tv_id_from_show_name(name, interactive_mode = False):
        
    results = ApiGateway.search_for_shows_by_name(name)['results']
    result_objects = extract_objects_from_results(results)
    
    if interactive_mode:
        print_result_object_table(get_tabular_rows_from_result_objects(result_objects))
        index = get_index_of_choice("Please enter the series that matches: ", len(result_objects))
    else:
        index = 0
        
    return result_objects[index].id
    
def extract_objects_from_results(results):
    result_objects = []
    for result in results:
        result_objects.append(TvListResultObject(result))        
    return result_objects

def get_tabular_rows_from_result_objects(result_objects):
    table = []
    for index, result_object in enumerate(result_objects):
        table.append(result_object.get_table_row(index+1))    
    return table
        
def get_index_of_choice(question, max_index):
    choice = 0
    choices = list(map(str, range(1, max_index+1)))
    while choice not in choices:
        choice = input(question).strip()
    return int(choice) - 1
    
       
show_id = get_tv_id_from_show_name("Silicon Valley")

response = ApiGateway.get_tv_show_by_id(show_id)

obj = TvShowDetailsObject(response)

print("hello")