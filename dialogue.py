import random

class DialogueManager:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! Welcome to AI Adventure Quest. How can I assist you today?",
            "help": self.get_help_message(),
            "start": "Let's get started! You can begin by typing 'quiz start', 'minigame start', or 'tutorial start'. For more options, type 'help'.",
            "quit": "Thank you for playing AI Adventure Quest! Hope to see you again soon.",
            "quiz": "To start a quiz, type 'quiz start'. To answer a question, type 'answer <your answer>'.",
            "minigame": "To start the mini-game, type 'minigame start'. To stop the mini-game, type 'minigame stop'.",
            "tutorial": "To begin the tutorial, type 'tutorial start'. To move to the next step, type 'tutorial next'.",
            "dashboard": "You can view your progress on the dashboard. Type 'dashboard' to see your current progress and rewards.",
            "unrelated": [
                "I'm here to help with the game. Try typing 'help' to see what you can do.",
                "That doesn't seem related to the game. Maybe try 'start' to begin your adventure.",
                "I didn't quite get that. You can type 'help' for assistance.",
            ],
            "unknown": "I'm not sure how to respond to that. Type 'help' for a list of commands.",
            "progress": "You can view your progress on the dashboard by typing 'dashboard'.",
            "save": "Your progress is saved automatically. You can type 'quit' to exit the game at any time, and we'll save your progress for next time.",
            "repeat_question": "To repeat the current question, type 'repeat question'.",
            "reset_quiz": "To reset the quiz, type 'reset quiz'.",
            "reset_tutorial": "To reset the tutorial, type 'reset tutorial'.",
            "reset_game": "To reset the entire game, type 'reset game'.",
            "status": "To check the status of your game, type 'status'.",
            "list_commands": "To see a list of all commands, type 'commands'.",
            "user_name": "To set or change your user name, type 'set name <your name>'.",
            "character": "To choose or change your character, type 'set character <character name>'.",
            "error_handling": "If you encounter an error, try restarting the game or check the 'help' section for guidance."
        }
        self.unrelated_triggers = [
            "what", "how", "why", "where", "who", "which", "when", "does", "is", "are", "can", "do"
        ]

    def get_help_message(self):
        return (
            "Here are some commands you can use:\n"
            "- 'start': Begin your adventure.\n"
            "- 'quiz': Start a quiz or answer quiz questions.\n"
            "- 'minigame': Play the mini-game.\n"
            "- 'tutorial': Learn about AI with the tutorial.\n"
            "- 'dashboard': View your progress.\n"
            "- 'quit': Exit the game.\n"
            "- 'help': Show this help message.\n"
            "- 'commands': List all available commands.\n"
            "- 'set name <your name>': Set or change your user name.\n"
            "- 'set character <character name>': Choose or change your character.\n"
            "- 'status': Check the status of your game.\n"
            "- 'repeat question': Repeat the current question in a quiz.\n"
            "- 'reset quiz': Reset the current quiz.\n"
            "- 'reset tutorial': Reset the current tutorial.\n"
            "- 'reset game': Reset the entire game.\n"
            "- 'progress': View your current progress.\n"
            "- 'save': Information on saving your progress."
        )

    def process_response(self, input_text):
        input_text = input_text.lower().strip()

        if input_text in self.responses:
            return self.responses[input_text]
        elif any(trigger in input_text for trigger in self.unrelated_triggers):
            return self.get_random_unrelated_response()
        else:
            return self.responses["unknown"]

    def get_random_unrelated_response(self):
        return random.choice(self.responses["unrelated"])

    def add_response(self, command, response):
        self.responses[command] = response
