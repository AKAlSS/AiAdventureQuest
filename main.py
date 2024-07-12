# main.py
import tkinter as tk
from game import Game
from database import Database

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

def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
