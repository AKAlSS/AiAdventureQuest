# game.py
import dialogue

class Game:
    def __init__(self):
        # Initialize game state and variables
        self.game_state = ""
        self.is_game_started = False
        self.dialogue_manager = dialogue.DialogueManager()

    def start(self):
        # Start the game
        self.is_game_started = True

    def process_input(self, input_text):
        # Process user input
        if not self.is_game_started:
            self.start()
        # Implement game logic based on user input
        if input_text.strip() == "quit":
            self.game_state = "quit"
        elif input_text.strip() == "help":
            self.game_state = "help"
        else:
            self.game_state = self.dialogue_manager.process_response(input_text)

    def get_output(self):
        # Get the game output to display
        if self.game_state == "quit":
            return "Game over. You quit the game."
        elif self.game_state == "help":
            return "This is the help message."
        else:
            return self.game_state
