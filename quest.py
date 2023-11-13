class Quest:
    def __init__(self, name, description, experience_reward, gold_reward, objectives):
        self.name = name
        self.description = description
        self.experience_reward = experience_reward
        self.gold_reward = gold_reward
        self.objectives = objectives
        self.required_progress = len(objectives)
        self.is_completed = False
