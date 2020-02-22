import textwrap 

class TvListResultObject:
    
    def __init__(self, response):
        self.id = response['id']
        self.name = response['name']
        self.overview = response['overview']

    def get_table_row(self, index):
        wrapper = textwrap.TextWrapper(width=100)         
        return [index, self.name, "\n".join(wrapper.wrap(self.overview))]