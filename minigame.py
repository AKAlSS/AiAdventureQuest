class MiniGame:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_active = False

    def start(self):
        self.is_active = True
        return "Mini-game started: {}".format(self.name)

    def stop(self):
        self.is_active = False
        return "Mini-game stopped: {}".format(self.name)

    def get_status(self):
        return "Mini-game '{}' is currently {}".format(self.name, "active" if self.is_active else "inactive")
