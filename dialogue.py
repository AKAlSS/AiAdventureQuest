# dialogue.py
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
            "save": "Your progress is saved."
        }

    def get_help_message(self):
        return (
            "Here are some commands you can use:\n"
            " - 'start': Begin the adventure\n"
            " - 'quiz start': Start the quiz\n"
            " - 'quiz answer <your answer>': Answer a quiz question\n"
            " - 'minigame start': Start the mini-game\n"
            " - 'minigame stop': Stop the mini-game\n"
            " - 'tutorial start': Start the tutorial\n"
            " - 'tutorial next': Move to the next step of the tutorial\n"
            " - 'dashboard': View your progress\n"
            " - 'set name <your name>': Set your player name\n"
            " - 'set character <character name>': Set your character\n"
            " - 'status': View your player status\n"
            " - 'commands': View available commands\n"
            " - 'progress': View your progress\n"
            " - 'save': Save your progress\n"
            " - 'quit': Quit the game\n"
        )

    def process_response(self, input_text):
        if input_text in self.responses:
            return self.responses[input_text]
        else:
            return random.choice(self.responses["unrelated"])

