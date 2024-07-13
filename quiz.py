class Quiz:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.questions = []
        self.current_question_index = 0
        self.score = 0

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index][0]
            self.current_question_index += 1
            return question
        else:
            return "Quiz completed. Your score: {}".format(self.score)

    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question_index - 1][1]
        if answer.lower() == correct_answer.lower():
            self.score += 1
            return "Correct!"
        else:
            return "Wrong! The correct answer was: {}".format(correct_answer)

    def reset(self):
        self.current_question_index = 0
        self.score = 0
