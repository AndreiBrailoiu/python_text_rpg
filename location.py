class Location:
    def __init__(self, name, description, interactions):
        self.name = name
        self.description = description
        self.interactions = interactions

    def get_interactions(self):
        interaction_str = "Options:\n"
        for option, action in self.interactions.items():
            interaction_str += f"{option}. {action}\n"
        return interaction_str