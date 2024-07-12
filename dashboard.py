'''
AI Adventure Quest - Dashboard File
'''
class Dashboard:
    def __init__(self):
        self.progress = 0
        self.rewards = []
    def display(self):
        print("Progress: {}%".format(self.progress))
        print("Rewards: {}".format(", ".join(self.rewards)))
    def update_progress(self, increment):
        self.progress += increment
    def add_reward(self, reward):
        self.rewards.append(reward)