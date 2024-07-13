import dialogue
from quiz import Quiz
from minigame import MiniGame
from tutorial import Tutorial
from dashboard import Dashboard
from player import Player

class Game:
    def __init__(self):
        self.game_state = ""
        self.is_game_started = False
        self.dialogue_manager = dialogue.DialogueManager()
        self.quiz = Quiz("AI Concepts Quiz", "Test your knowledge on AI concepts")
        self.minigame = MiniGame("AI Adventure", "A fun adventure game")
        self.tutorial = Tutorial("AI Basics Tutorial", "Learn the basics of AI")
        self.dashboard = Dashboard()
        self.player = Player()

        # Example content for quiz and tutorial
        self.quiz.add_question("What does AI stand for?", "Artificial Intelligence")
        self.quiz.add_question("Name a popular programming language for AI.", "Python")
        self.tutorial.add_step("Step 1: Understand what AI is.")
        self.tutorial.add_step("Step 2: Learn about different AI frameworks.")

    def start(self):
        self.is_game_started = True
        self.game_state = "start"

    def process_input(self, input_text):
        if not self.is_game_started:
            self.start()

        input_text = input_text.strip().lower()
        command, *args = input_text.split(" ")

        if command == "quit":
            self.game_state = "quit"
        elif command == "help":
            self.game_state = self.dialogue_manager.get_help_message()
        elif command == "start":
            self.game_state = self.dialogue_manager.process_response("start")
        elif command == "quiz":
            if "start" in args:
                self.game_state = "Starting quiz: " + self.quiz.get_next_question()
            elif "answer" in args:
                answer = " ".join(args[1:])
                self.game_state = self.quiz.check_answer(answer)
            elif "reset" in args:
                self.quiz.reset()
                self.game_state = "Quiz has been reset."
            elif "repeat" in args:
                self.game_state = self.quiz.get_next_question()
            else:
                self.game_state = self.dialogue_manager.process_response("quiz")
        elif command == "minigame":
            if "start" in args:
                self.game_state = self.minigame.start()
            elif "stop" in args:
                self.game_state = self.minigame.stop()
            else:
                self.game_state = self.minigame.get_status()
        elif command == "tutorial":
            if "start" in args:
                self.game_state = "Starting tutorial: " + self.tutorial.get_next_step()
            elif "next" in args:
                self.game_state = self.tutorial.get_next_step()
            elif "reset" in args:
                self.tutorial.reset()
                self.game_state = "Tutorial has been reset."
            else:
                self.game_state = self.dialogue_manager.process_response("tutorial")
        elif command == "dashboard":
            self.game_state = self.dashboard.display()
        elif command == "set":
            if "name" in args:
                name = " ".join(args[1:])
                self.player.set_name(name)
                self.game_state = f"Player name set to {name}."
            elif "character" in args:
                character = " ".join(args[1:])
                self.player.set_character(character)
                self.game_state = f"Player character set to {character}."
        elif command == "status":
            self.game_state = self.player.get_status()
        elif command == "commands":
            self.game_state = self.dialogue_manager.get_help_message()
        elif command == "progress":
            self.game_state = self.dashboard.display()
        elif command == "save":
            self.game_state = self.dialogue_manager.process_response("save")
        else:
            self.game_state = self.dialogue_manager.process_response(input_text)

    def get_output(self):
        if self.game_state == "quit":
            return "Game over. You quit the game."
        elif self.game_state == "help":
            return self.dialogue_manager.get_help_message()
        else:
            return self.game_state
