class Task():
    def __init__(self, title):
        self.title = title
        self.creation_date = "dd/mm/yyyy"
        self.description = "info"
        self.due_date = "dd/mm/yyyy"
        self.progress = 0
        self.last_update = "dd/mm/yyyy"
        
    def simple_string(self):
        return self.title
    
    def set_progress(self, start_progress):
        self.progess = start_progress
    
    def get_progress(self):
        return self.progress
    
    def detail_string(self):
        
        return " "*10 + str(self.title) + "\n" + \
        " "*5 + "last update " + str(self.last_update) + "\n" + \
        " "*5 + "progress: " + str(self.progress) + "\n" + \
        " "*5 + "created: " + str(self.creation_date) + "\n" + \
        " "*5 + "description: " + str(self.description) + "\n" + \
        " "*5 + "deadline: " + str(self.due_date) + "\n" 
        
    
