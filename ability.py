class Ability:
    def __init__(self, name, type, value, cooldown):
        self.name = name
        self.type = type
        self.value = value
        self.cooldown = cooldown

    def is_usable(self):
        return self.cooldown == 0