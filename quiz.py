'''
AI Adventure Quest - Quiz File
'''
class Quiz:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description