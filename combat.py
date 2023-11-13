import random

class Combat:
    @staticmethod
    def calculate_damage(attacker, defender):
        # Calculate damage based on attacker's attack and defender's defense
        damage = max(attacker.attack - defender.defense, 0)
        # Add some randomness to damage (between 80% and 120%)
        damage *= random.uniform(0.8, 1.2)
        return int(damage)