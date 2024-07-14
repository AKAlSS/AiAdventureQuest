class Quiz:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.questions = []
        self.current_question_index = -1

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def get_next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index][0]
        else:
            self.current_question_index = -1
            return "Quiz finished. You can reset the quiz to start over."

    def check_answer(self, answer):
        if self.current_question_index == -1:
            return "Start the quiz first by typing 'quiz start'."
        correct_answer = self.questions[self.current_question_index][1]
        if answer.lower() == correct_answer.lower():
            return "Correct!"
        else:
            return f"Incorrect. The correct answer was: {correct_answer}"

    def reset(self):
        self.current_question_index = -1

def get_ai_quiz():
    quiz = Quiz("AI Concepts Quiz", "Test your knowledge on AI concepts")
    quiz.add_question("What does AI stand for?", "Artificial Intelligence")
    quiz.add_question("Name a popular programming language for AI.", "Python")
    quiz.add_question("What is machine learning?", "A subset of AI that focuses on building systems that learn from data.")
    quiz.add_question("What is deep learning?", "A subset of machine learning involving neural networks with many layers.")
    quiz.add_question("What is NLP?", "A field of AI that gives machines the ability to read, understand, and derive meaning from human languages.")
    quiz.add_question("What is reinforcement learning?", "A type of machine learning where agents learn by interacting with their environment and receiving rewards or penalties.")
    return quiz
