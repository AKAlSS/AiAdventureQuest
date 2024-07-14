import tkinter as tk
from lessons import Lessons
from quiz import get_ai_quiz
from database import Database
import logging

logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Adventure Quest")
        self.create_widgets()
        self.database = Database()
        self.lessons = Lessons()
        self.quiz = get_ai_quiz()
        self.current_quiz = None
        self.load_game_state()
        logging.info("Game started")

    def create_widgets(self):
        self.input_text = tk.Entry(self.master)
        self.input_text.pack()
        self.submit_button = tk.Button(self.master, text="Submit", command=self.process_input)
        self.submit_button.pack()
        self.output_text = tk.Text(self.master)
        self.output_text.pack()

        self.lesson_button = tk.Button(self.master, text="View Lessons", command=self.display_lessons)
        self.lesson_button.pack()
        self.quiz_button = tk.Button(self.master, text="Take Quiz", command=self.start_quiz)
        self.quiz_button.pack()
        self.feedback_button = tk.Button(self.master, text="View Feedback", command=self.display_feedback)
        self.feedback_button.pack()

    def load_game_state(self):
        game_state = self.database.load_game_state()
        if game_state:
            self.game_state = game_state
            logging.info("Game state loaded")
        else:
            self.game_state = {}

    def save_game_state(self):
        self.database.save_game_state(self.game_state)
        logging.info("Game state saved")

    def process_input(self):
        input_text = self.input_text.get()
        logging.info(f"User input: {input_text}")
        self.handle_command(input_text)
        self.save_game_state()
        self.update_gui()
        logging.info(f"Game state: {self.game_state}")

    def update_gui(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, self.get_output())

    def handle_command(self, command):
        if command.startswith('lesson '):
            topic = command.split(' ', 1)[1]
            self.game_state['current_content'] = self.lessons.get_lesson(topic)
        elif command.startswith('quiz '):
            self.current_quiz = self.quiz
            self.game_state['current_content'] = self.current_quiz.get_next_question()
        elif command.startswith('answer '):
            if self.current_quiz:
                answer = command.split(' ', 1)[1]
                self.game_state['current_content'] = self.current_quiz.check_answer(answer)
        elif command == 'next':
            if self.current_quiz:
                self.game_state['current_content'] = self.current_quiz.get_next_question()
        elif command == 'reset':
            if self.current_quiz:
                self.current_quiz.reset()
                self.game_state['current_content'] = "Quiz has been reset."
        elif command == 'feedback':
            self.display_feedback()
        elif command == 'dashboard':
            self.game_state['current_content'] = "Displaying dashboard (to be implemented)"
        else:
            self.game_state['current_content'] = "Command not recognized."

    def get_output(self):
        return self.game_state.get('current_content', '')

    def display_lessons(self):
        lesson_topics = list(self.lessons.knowledge_base.topics.keys())
        self.game_state['current_content'] = "Available lessons:\n" + "\n".join(lesson_topics)
        self.update_gui()

    def start_quiz(self):
        self.current_quiz = self.quiz
        self.game_state['current_content'] = self.current_quiz.get_next_question()
        self.update_gui()

    def display_feedback(self):
        # Implement feedback logic here
        self.game_state['current_content'] = "Displaying feedback (to be implemented)"
        self.update_gui()

def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
