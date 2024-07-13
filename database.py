# database.py
import json
import os

class Database:
    def __init__(self, filepath='game_state.json'):
        self.filepath = filepath

    def load_game_state(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return None

    def save_game_state(self, game_state):
        with open(self.filepath, 'w') as file:
            json.dump(game_state, file)
