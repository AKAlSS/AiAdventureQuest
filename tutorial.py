# tutorial.py
class Tutorial:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.steps = []
        self.current_step_index = -1

    def add_step(self, step):
        self.steps.append(step)

    def get_next_step(self):
        self.current_step_index += 1
        if self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        else:
            self.current_step_index = -1
            return "Tutorial finished. You can reset the tutorial to start over."

    def reset(self):
        self.current_step_index = -1

def get_ai_tutorial():
    tutorial = Tutorial("AI Basics Tutorial", "Learn the basics of AI")
    tutorial.add_step("Step 1: Understand what AI is.")
    tutorial.add_step("Step 2: Learn about different AI frameworks like TensorFlow and PyTorch.")
    tutorial.add_step("Step 3: Implement a basic machine learning model.")
    return tutorial
