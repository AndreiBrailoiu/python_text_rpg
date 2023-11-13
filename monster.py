class Monster:
    def __init__(self, name, health, attack, defense, experience_reward, gold_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience_reward = experience_reward
        self.gold_reward = gold_reward  # Add the gold_reward attribute

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
