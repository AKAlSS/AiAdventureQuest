'''
AI Adventure Quest - Player File
'''
class Player:
    def __init__(self):
        self.name = ""
        self.character = ""
    def create_character(self):
        self.name = input("Enter your name: ")
        self.character = input("Choose your character: ")
    def get_name(self):
        return self.name
    def get_character(self):
        return self.character