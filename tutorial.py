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
