class Tutorial:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.steps = []
        self.current_step_index = 0

    def add_step(self, step):
        self.steps.append(step)

    def get_next_step(self):
        if self.current_step_index < len(self.steps):
            step = self.steps[self.current_step_index]
            self.current_step_index += 1
            return step
        else:
            return "Tutorial completed: {}".format(self.name)

    def reset(self):
        self.current_step_index = 0
