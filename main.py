import tkinter as tk
from tkinter import scrolledtext
from knowledge_base import KnowledgeBase
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
        self.knowledge_base = KnowledgeBase()
        self.quiz = get_ai_quiz()
        self.current_quiz = None
        self.selected_option = tk.StringVar()
        self.game_state = {'current_content': ''}
        self.load_game_state()
        logging.info("Game started")
        self.show_instructions()

    def create_widgets(self):
        self.welcome_text = tk.Label(self.master, text="Welcome to AI Adventure Quest!\nLearn about AI agents and test your knowledge.\nUse the buttons below to navigate.")
        self.welcome_text.pack()

        self.input_text = tk.Entry(self.master)
        self.input_text.pack()
        self.submit_button = tk.Button(self.master, text="Submit", command=self.process_input)
        self.submit_button.pack()

        self.output_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.output_text.pack(expand=True, fill='both')

        self.lesson_button = tk.Button(self.master, text="View Lessons", command=self.display_lessons)
        self.lesson_button.pack()
        self.quiz_button = tk.Button(self.master, text="Take Quiz", command=self.start_quiz)
        self.quiz_button.pack()
        self.feedback_button = tk.Button(self.master, text="View Feedback", command=self.display_feedback)
        self.feedback_button.pack()

        self.option_buttons = []

    def load_game_state(self):
        game_state = self.database.load_game_state()
        if game_state:
            self.game_state = game_state
            logging.info("Game state loaded")
        else:
            self.game_state = {'current_content': ''}

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
        self.output_text.insert(tk.END, self.game_state.get('current_content', ''))

    def handle_command(self, command):
        if command.startswith('lesson '):
            topic = command.split(' ', 1)[1]
            lesson_content = self.knowledge_base.get_topic_info(topic)
            self.game_state['current_content'] = lesson_content + "\n\n" + self.get_instructions()
        elif command == 'quiz start':
            self.start_quiz()
        elif command == 'reset':
            self.reset_quiz()
        else:
            self.game_state['current_content'] = "Command not recognized. Please use 'lesson [topic]', 'quiz start', or 'reset'."

    def show_instructions(self):
        self.game_state['current_content'] = self.get_instructions()
        self.update_gui()

    def get_instructions(self):
        return (
            "Welcome to AI Adventure Quest!\n\n"
            "Available commands:\n"
            "- 'lesson [topic]': View a lesson on a specific topic.\n"
            "- 'quiz start': Start the quiz.\n"
            "- 'reset': Reset the current quiz.\n\n"
            "Topics available:\n"
            "- AI Agents\n"
            "- AI Frameworks\n"
            "- Agentic Workflows\n"
            "- Agentic Automation\n"
            "- AI Concepts"
        )

    def display_lessons(self):
        lesson_topics = list(self.knowledge_base.topics.keys())
        self.game_state['current_content'] = "Available lessons:\n" + "\n".join(lesson_topics) + "\n\n" + self.get_instructions()
        self.update_gui()

    def start_quiz(self):
        self.current_quiz = get_ai_quiz()
        self.show_next_question()

    def show_next_question(self):
        question, options = self.current_quiz.get_next_question()
        if not options:
            self.game_state['current_content'] = question + "\n\n" + self.get_instructions()
        else:
            self.game_state['current_content'] = question
            self.update_gui()
            self.display_options(options)

    def display_options(self, options):
        for btn in self.option_buttons:
            btn.destroy()
        self.option_buttons = []
        self.selected_option.set(None)
        for option in options:
            btn = tk.Radiobutton(self.master, text=option, variable=self.selected_option, value=option)
            btn.pack(anchor=tk.W)
            self.option_buttons.append(btn)
        self.submit_answer_button = tk.Button(self.master, text="Submit Answer", command=self.submit_answer)
        self.submit_answer_button.pack()
        self.option_buttons.append(self.submit_answer_button)

    def submit_answer(self):
        selected_answer = self.selected_option.get()
        if selected_answer:
            feedback = self.current_quiz.check_answer(selected_answer)
            question, options = self.current_quiz.get_next_question()
            self.game_state['current_content'] = feedback + "\n\n" + question
            self.update_gui()
            if options:
                self.display_options(options)
            else:
                self.game_state['current_content'] += "\n\nQuiz finished. You can reset the quiz to start over."
                self.update_gui()
        else:
            self.game_state['current_content'] = "Please select an answer."
            self.update_gui()

    def reset_quiz(self):
        self.current_quiz.reset()
        self.game_state['current_content'] = "Quiz has been reset.\n\n" + self.get_instructions()
        self.update_gui()

    def display_feedback(self):
        self.game_state['current_content'] = "Displaying feedback (to be implemented)" + "\n\n" + self.get_instructions()
        self.update_gui()

def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
