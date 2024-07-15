import tkinter as tk
from lessons import Lessons
from quiz import get_ai_quiz, Quiz
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
        self.output_text.insert(tk.END, self.get_output())

    def handle_command(self, command):
        if isinstance(self.game_state, str):
            self.game_state = {'current_content': self.game_state}
        
        if command.startswith('lesson '):
            topic = command.split(' ', 1)[1]
            lesson_content = self.lessons.get_lesson(topic)
            self.game_state['current_content'] = lesson_content
        elif command == 'lessons':
            self.display_lessons()
        elif command == 'quiz':
            self.start_quiz()
        elif command.startswith('answer '):
            if self.current_quiz:
                answer = command.split(' ', 1)[1]
                self.game_state['current_content'] = self.current_quiz.check_answer(answer)
        elif command == 'next':
            if self.current_quiz:
                question, options = self.current_quiz.get_next_question()
                self.game_state['current_content'] = question
                self.display_options(options)
        elif command == 'reset':
            if self.current_quiz:
                self.current_quiz.reset()
                self.game_state['current_content'] = "Quiz has been reset."
        elif command == 'feedback':
            self.display_feedback()
        elif command == 'dashboard':
            self.game_state['current_content'] = "Displaying dashboard (to be implemented)"
        else:
            self.game_state['current_content'] = "Command not recognized. Please type 'lessons' to view lessons or 'quiz' to take a quiz."

    def get_output(self):
        return self.game_state.get('current_content', '')

    def display_lessons(self):
        lesson_topics = list(self.lessons.knowledge_base.topics.keys())
        lessons_str = "Available lessons:\n" + "\n".join(lesson_topics)
        lessons_str += "\n\nType 'lesson <topic>' to view a lesson (e.g., 'lesson AI Agents')."
        self.game_state['current_content'] = lessons_str
        self.update_gui()

    def start_quiz(self):
        self.current_quiz = self.quiz
        question, options = self.current_quiz.get_next_question()
        self.game_state['current_content'] = question
        self.display_options(options)
        self.update_gui()

    def display_options(self, options):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Radiobutton) or isinstance(widget, tk.Button) and widget.cget('text') == "Submit Answer":
                widget.destroy()

        for option in options:
            tk.Radiobutton(self.master, text=option, variable=self.selected_option, value=option).pack()

        tk.Button(self.master, text="Submit Answer", command=self.submit_answer).pack()

    def submit_answer(self):
        answer = self.selected_option.get()
        result = self.current_quiz.check_answer(answer)
        self.game_state['current_content'] = result
        self.update_gui()

    def display_feedback(self):
        self.game_state['current_content'] = "Displaying feedback (to be implemented)"
        self.update_gui()

    def show_instructions(self):
        instructions = "Welcome to AI Adventure Quest!\n\n" \
                       "Instructions:\n" \
                       "- Use the buttons below to view lessons or take quizzes.\n" \
                       "- You can also type commands in the input field and click 'Submit'.\n" \
                       "Available commands:\n" \
                       "  - 'lessons': View available lessons.\n" \
                       "  - 'lesson <topic>': View a specific lesson (e.g., 'lesson AI Agents').\n" \
                       "  - 'quiz': Start a quiz.\n" \
                       "  - 'answer <your_answer>': Submit an answer for the quiz.\n" \
                       "  - 'next': Move to the next question in the quiz.\n" \
                       "  - 'reset': Reset the current quiz.\n" \
                       "  - 'feedback': View feedback (to be implemented).\n"
        self.game_state['current_content'] = instructions
        self.update_gui()

def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
