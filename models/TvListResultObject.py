import textwrap 

class TvListResultObject:
    
    def __init__(self, id, name, overview):
        self.id = id
        self.name = name
        self.overview = overview
        
    def get_table_row(self, index):
        wrapper = textwrap.TextWrapper(width=100) 
        
        s = "\n"
        
        return [index, self.name, s.join(wrapper.wrap(self.overview))]        
    