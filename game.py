'''
AI Adventure Quest - Game File
'''
from player import Player
from quest import Quest
from tutorial import Tutorial
from minigame import MiniGame
from quiz import Quiz
from coding_challenge import CodingChallenge
from dashboard import Dashboard
class Game:
    def __init__(self):
        self.player = Player()
        self.quests = []
        self.tutorials = []
        self.minigames = []
        self.quizzes = []
        self.coding_challenges = []
        self.dashboard = Dashboard()
    def start(self):
        self.player.create_character()
        self.load_quests()
        self.load_tutorials()
        self.load_minigames()
        self.load_quizzes()
        self.load_coding_challenges()
        self.dashboard.display()
    def load_quests(self):
        # Load quests from a data source
        # For simplicity, let's assume we have a list of quests
        quest_data = [
            {"name": "Quest 1", "description": "Complete quest 1"},
            {"name": "Quest 2", "description": "Complete quest 2"},
            {"name": "Quest 3", "description": "Complete quest 3"}
        ]
        for data in quest_data:
            quest = Quest(data["name"], data["description"])
            self.quests.append(quest)
    def load_tutorials(self):
        # Load tutorials from a data source
        # For simplicity, let's assume we have a list of tutorials
        tutorial_data = [
            {"name": "Tutorial 1", "description": "Learn about AI agents"},
            {"name": "Tutorial 2", "description": "Learn about TensorFlow"},
            {"name": "Tutorial 3", "description": "Learn about NLTK"}
        ]
        for data in tutorial_data:
            tutorial = Tutorial(data["name"], data["description"])
            self.tutorials.append(tutorial)
    def load_minigames(self):
        # Load mini-games from a data source
        # For simplicity, let's assume we have a list of mini-games
        minigame_data = [
            {"name": "Mini-Game 1", "description": "Play a game related to AI"},
            {"name": "Mini-Game 2", "description": "Play a game using TensorFlow"},
            {"name": "Mini-Game 3", "description": "Play a game using NLTK"}
        ]
        for data in minigame_data:
            minigame = MiniGame(data["name"], data["description"])
            self.minigames.append(minigame)
    def load_quizzes(self):
        # Load quizzes from a data source
        # For simplicity, let's assume we have a list of quizzes
        quiz_data = [
            {"name": "Quiz 1", "description": "Test your knowledge about AI"},
            {"name": "Quiz 2", "description": "Test your knowledge about TensorFlow"},
            {"name": "Quiz 3", "description": "Test your knowledge about NLTK"}
        ]
        for data in quiz_data:
            quiz = Quiz(data["name"], data["description"])
            self.quizzes.append(quiz)
    def load_coding_challenges(self):
        # Load coding challenges from a data source
        # For simplicity, let's assume we have a list of coding challenges
        coding_challenge_data = [
            {"name": "Coding Challenge 1", "description": "Solve a coding challenge related to AI"},
            {"name": "Coding Challenge 2", "description": "Solve a coding challenge using TensorFlow"},
            {"name": "Coding Challenge 3", "description": "Solve a coding challenge using NLTK"}
        ]
        for data in coding_challenge_data:
            coding_challenge = CodingChallenge(data["name"], data["description"])
            self.coding_challenges.append(coding_challenge)