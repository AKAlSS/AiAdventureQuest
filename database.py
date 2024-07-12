'''
AI Adventure Quest Database
'''
class Database:
    def __init__(self):
        # Initialize the database
        pass
    def save_game_state(self, game_state):
        # Save the game state to the database
        with open("game_state.txt", "w") as file:
            file.write(game_state)
    def load_game_state(self):
        # Load the game state from the database
        try:
            with open("game_state.txt", "r") as file:
                game_state = file.read()
            return game_state
        except FileNotFoundError:
            return None