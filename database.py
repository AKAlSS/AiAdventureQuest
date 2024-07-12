# database.py
import json
import os

class Database:
    def __init__(self, filename="game_state.json"):
        self.filename = filename

    def load_game_state(self):
        # Load game state logic here
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return ""

    def save_game_state(self, game_state):
        # Save game state logic here
        with open(self.filename, 'w') as file:
            json.dump(game_state, file)
