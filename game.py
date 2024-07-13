# game.py
import dialogue
from quiz import get_ai_quiz
from minigame import MiniGame
from tutorial import get_ai_tutorial
from dashboard import Dashboard
from database import Database
from player import Player
from coding_challenge import get_ai_coding_challenges
from quest import Quest
from knowledge_base import KnowledgeBase

class Game:
    def __init__(self):
        self.game_state = ""
        self.is_game_started = False
        self.dialogue_manager = dialogue.DialogueManager()
        self.quiz = get_ai_quiz()
        self.minigame = MiniGame("AI Adventure", "A fun adventure game")
        self.tutorial = get_ai_tutorial()
        self.dashboard = Dashboard()
        self.player = Player()
        self.coding_challenges = get_ai_coding_challenges()
        self.current_coding_challenge = None
        self.quest = Quest("AI Quest", "Complete various tasks to progress in the game")
        self.knowledge_base = KnowledgeBase()

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
        elif command == "codingchallenge":
            if "start" in args:
                self.current_coding_challenge = self.coding_challenges[0]  # Example to pick the first challenge
                self.game_state = f"Starting Coding Challenge: {self.current_coding_challenge.get_name()}"
            elif "complete" in args and self.current_coding_challenge:
                self.game_state = f"Coding Challenge Completed: {self.current_coding_challenge.get_name()}"
                self.current_coding_challenge = None
            else:
                self.game_state = f"Coding Challenge: {self.current_coding_challenge.get_description() if self.current_coding_challenge else 'No active challenge'}"
        elif command == "quest":
            if "start" in args:
                self.game_state = f"Starting Quest: {self.quest.get_name()}"
            elif "complete" in args:
                self.game_state = f"Quest Completed: {self.quest.get_name()}"
            else:
                self.game_state = f"Quest: {self.quest.get_description()}"
        elif command == "knowledge":
            if args:
                topic = " ".join(args)
                self.game_state = self.knowledge_base.get_topic_info(topic)
            else:
                self.game_state = "Available topics: " + ", ".join(self.knowledge_base.topics.keys())
        else:
            self.game_state = self.dialogue_manager.process_response(input_text)

    def get_output(self):
        if self.game_state == "quit":
            return "Game over. You quit the game."
        elif self.game_state == "help":
            return self.dialogue_manager.get_help_message()
        else:
            return self.game_state

# Main function to run the game
def main():
    import tkinter as tk

    class GameGUI:
        def __init__(self, master):
            self.master = master
            self.master.title("AI Adventure Quest")
            self.create_widgets()
            self.database = Database()
            self.game = Game()
            self.load_game_state()

        def create_widgets(self):
            self.input_text = tk.Entry(self.master)
            self.input_text.pack()
            self.submit_button = tk.Button(self.master, text="Submit", command=self.process_input)
            self.submit_button.pack()
            self.output_text = tk.Text(self.master)
            self.output_text.pack()

        def load_game_state(self):
            game_state = self.database.load_game_state()
            if game_state:
                self.game.game_state = game_state

        def save_game_state(self):
            game_state = self.game.game_state
            self.database.save_game_state(game_state)

        def process_input(self):
            input_text = self.input_text.get()
            self.game.process_input(input_text)
            self.save_game_state()
            self.update_gui()

        def update_gui(self):
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, self.game.get_output())

    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

