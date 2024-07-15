class Quiz:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.questions = []
        self.current_question_index = -1

    def add_question(self, question, options, answer):
        self.questions.append((question, options, answer))

    def get_next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            question, options, _ = self.questions[self.current_question_index]
            return question, options
        else:
            self.current_question_index = -1
            return "Quiz finished. You can reset the quiz to start over.", []

    def check_answer(self, selected_option):
        if self.current_question_index == -1:
            return "Start the quiz first by typing 'quiz start'."
        _, _, correct_answer = self.questions[self.current_question_index]
        if selected_option == correct_answer:
            return "Correct!"
        else:
            return f"Incorrect. The correct answer was: {correct_answer}"

    def reset(self):
        self.current_question_index = -1

def get_ai_quiz():
    quiz = Quiz("AI Concepts Quiz", "Test your knowledge on AI concepts")
    quiz.add_question("What does AI stand for?", ["Artificial Intelligence", "Automated Intelligence", "Autonomous Interface"], "Artificial Intelligence")
    quiz.add_question("Name a popular programming language for AI.", ["Java", "Python", "C++"], "Python")
    quiz.add_question("What is machine learning?", ["A subset of AI that focuses on building systems that learn from data.", "A way to write code.", "A type of hardware."], "A subset of AI that focuses on building systems that learn from data.")
    quiz.add_question("What is deep learning?", ["A type of AI that involves deep thinking.", "A subset of machine learning involving neural networks with many layers.", "A method for big data analysis."], "A subset of machine learning involving neural networks with many layers.")
    quiz.add_question("What is NLP?", ["A type of AI that processes natural languages.", "A field of AI that gives machines the ability to read, understand, and derive meaning from human languages.", "A programming language."], "A field of AI that gives machines the ability to read, understand, and derive meaning from human languages.")
    quiz.add_question("What is reinforcement learning?", ["A type of machine learning where agents learn by interacting with their environment and receiving rewards or penalties.", "A way to reinforce code reliability.", "A security measure."], "A type of machine learning where agents learn by interacting with their environment and receiving rewards or penalties.")
    return quiz
