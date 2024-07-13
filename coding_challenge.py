# coding_challenge.py
class CodingChallenge:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

def get_ai_coding_challenges():
    return [
        CodingChallenge("Implement a basic neural network", "Create a simple neural network using TensorFlow or PyTorch"),
        CodingChallenge("Develop a decision tree algorithm", "Build a decision tree from scratch to classify data"),
        CodingChallenge("Implement a k-means clustering algorithm", "Write a k-means clustering algorithm to group data points")
    ]
