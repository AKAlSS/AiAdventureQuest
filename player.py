# player.py
class Player:
    def __init__(self):
        self.name = "Player"
        self.character = "Default Character"

    def set_name(self, name):
        self.name = name

    def set_character(self, character):
        self.character = character

    def get_status(self):
        return f"Player Name: {self.name}, Character: {self.character}"
