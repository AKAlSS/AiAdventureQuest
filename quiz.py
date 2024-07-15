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

    def check_answer(self, answer):
        if self.current_question_index == -1:
            return "Start the quiz first by typing 'quiz start'."
        _, _, correct_answer = self.questions[self.current_question_index]
        if answer.lower() == correct_answer.lower():
            return "Correct!"
        else:
            return f"Incorrect. The correct answer was: {correct_answer}"

    def reset(self):
        self.current_question_index = -1

def get_ai_quiz():
    quiz = Quiz("AI Concepts Quiz", "Test your knowledge on AI concepts")
    quiz.add_question(
        "What does AI stand for?",
        ["Artificial Intelligence", "Automated Intelligence", "Applied Intelligence", "Augmented Intelligence"],
        "Artificial Intelligence"
    )
    quiz.add_question(
        "Name a popular programming language for AI.",
        ["Python", "Java", "C++", "Ruby"],
        "Python"
    )
    quiz.add_question(
        "What is machine learning?",
        ["A subset of AI that focuses on building systems that learn from data.",
         "A method for hardcoding intelligent behavior.",
         "A type of hardware for running AI models.",
         "A programming language used exclusively for AI."],
        "A subset of AI that focuses on building systems that learn from data."
    )
    return quiz
