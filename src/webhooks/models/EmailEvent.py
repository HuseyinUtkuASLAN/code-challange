import json
import string


class EmailEvent:
    def __init__(self):
        self.Id : string = None
        self.Type : string = None
        self.Text : string = None
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)