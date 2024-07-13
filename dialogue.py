import random

class DialogueManager:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! Welcome to AI Adventure Quest. How can I assist you today?",
            "help": self.get_help_message(),
            "start": "Let's get started! You can begin by typing 'quiz', 'minigame', or 'tutorial'. For more options, type 'help'.",
            "quit": "Thank you for playing AI Adventure Quest! Hope to see you again soon.",
            "quiz": "To start a quiz, type 'quiz start'. To answer a question, type 'answer <your answer>'.",
            "minigame": "To start the mini-game, type 'minigame start'. To stop the mini-game, type 'minigame stop'.",
            "tutorial": "To begin the tutorial, type 'tutorial start'. To move to the next step, type 'tutorial next'.",
            "unknown": "I'm not sure how to respond to that. Type 'help' for a list of commands.",
            "unrelated": [
                "I'm here to help with the game. Try typing 'help' to see what you can do.",
                "That doesn't seem related to the game. Maybe try 'start' to begin your adventure.",
                "I didn't quite get that. You can type 'help' for assistance.",
            ]
        }

    def get_help_message(self):
        return (
            "Here are some commands you can use:\n"
            "- 'start': Begin your adventure.\n"
            "- 'quiz': Start a quiz or answer quiz questions.\n"
            "- 'minigame': Play the mini-game.\n"
            "- 'tutorial': Learn about AI with the tutorial.\n"
            "- 'quit': Exit the game.\n"
            "- 'help': Show this help message."
        )

    def process_response(self, input_text):
        input_text = input_text.lower().strip()
        if input_text in self.responses:
            return self.responses[input_text]
        else:
            return self.get_random_unrelated_response()

    def get_random_unrelated_response(self):
        return random.choice(self.responses["unrelated"])

    def add_response(self, command, response):
        self.responses[command] = response
