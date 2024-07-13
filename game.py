import dialogue
from quiz import Quiz
from minigame import MiniGame
from tutorial import Tutorial

class Game:
    def __init__(self):
        self.game_state = ""
        self.is_game_started = False
        self.dialogue_manager = dialogue.DialogueManager()
        self.quiz = Quiz("AI Concepts Quiz", "Test your knowledge on AI concepts")
        self.minigame = MiniGame("AI Adventure", "A fun adventure game")
        self.tutorial = Tutorial("AI Basics Tutorial", "Learn the basics of AI")

        # Example content for quiz and tutorial
        self.quiz.add_question("What does AI stand for?", "Artificial Intelligence")
        self.quiz.add_question("Name a popular programming language for AI.", "Python")
        self.tutorial.add_step("Step 1: Understand what AI is.")
        self.tutorial.add_step("Step 2: Learn about different AI frameworks.")

    def start(self):
        self.is_game_started = True

    def process_input(self, input_text):
        if not self.is_game_started:
            self.start()

        input_text = input_text.strip().lower()

        if input_text == "quit":
            self.game_state = "quit"
        elif input_text == "help":
            self.game_state = "help"
        elif input_text.startswith("quiz"):
            if "next" in input_text:
                self.game_state = self.quiz.get_next_question()
            else:
                self.game_state = "Starting quiz: " + self.quiz.get_next_question()
        elif input_text.startswith("answer"):
            _, answer = input_text.split(" ", 1)
            self.game_state = self.quiz.check_answer(answer)
        elif input_text.startswith("minigame"):
            if "start" in input_text:
                self.game_state = self.minigame.start()
            elif "stop" in input_text:
                self.game_state = self.minigame.stop()
            else:
                self.game_state = self.minigame.get_status()
        elif input_text.startswith("tutorial"):
            if "next" in input_text:
                self.game_state = self.tutorial.get_next_step()
            else:
                self.game_state = "Starting tutorial: " + self.tutorial.get_next_step()
        else:
            self.game_state = self.dialogue_manager.process_response(input_text)

    def get_output(self):
        if self.game_state == "quit":
            return "Game over. You quit the game."
        elif self.game_state == "help":
            return "Available commands: quiz, answer <your answer>, minigame start/stop, tutorial, help, quit"
        else:
            return self.game_state
