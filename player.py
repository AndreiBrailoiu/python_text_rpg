from ability import Ability
from character_class import CharacterClass

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.defense = 5
        self.gold = 0
        self.inventory = []
        self.abilities = []
        self.quests = []
        self.defeated_monsters = {}
        self.collected_items = {}
        self.experience = 0

    def is_alive(self):
        return self.health > 0

    def gain_gold(self, amount):
        self.gold += amount

    def battle_monster(self, monster):
        if monster.is_alive():
            monster_name = monster.name
            if monster_name in self.defeated_monsters:
                self.defeated_monsters[monster_name] += 1
            else:
                self.defeated_monsters[monster_name] = 1

    def collect_item(self, item):
        item_name = item.name
        if item_name in self.collected_items:
            self.collected_items[item_name] += 1
        else:
            self.collected_items[item_name] = 1

    def gain_item(self, item):
        self.inventory.append(item)
        
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
            
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def use_item(self, item_name, value):
        for item in self.inventory:
            if item.name == item_name:
                if item_name == "Health Potion":
                    self.heal(value)  # You can define the heal method to restore the player's health
                # Handle other item effects here
                self.inventory.remove(item)
                return
        print(f"You don't have a {item_name} in your inventory.")

    def gain_experience(self, experience):
        self.experience += experience
        while self.experience >= self.get_experience_threshold():
            self.level_up()

    def get_experience_threshold(self):
        thresholds = [100, 200, 400, 800, 1600]
        if self.level < len(thresholds):
            return thresholds[self.level]
        return thresholds[-1]

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        self.defense += 2
        if self.level == 2:
            self.learn_new_ability("Power Strike", "attack", 25, 4)

        for ability in self.character_class.abilities:
            if self.level >= ability.level_required:
                self.learn_new_ability(ability.name, ability.type, ability.value, ability.cooldown)

    def learn_new_ability(self, name, type, value, cooldown):
        new_ability = Ability(name, type, value, cooldown)

        if self.character_class.name == "Warrior":
            if name in warrior_abilities:
                warrior_ability = warrior_abilities[name]
                if len(self.abilities) < 3:
                    self.abilities.append(Ability(warrior_ability.name, warrior_ability.type, warrior_ability.value, warrior_ability.cooldown))
        elif self.character_class.name == "Mage":
            if name in mage_abilities:
                mage_ability = mage_abilities[name]
                if len(self.abilities) < 3:
                    self.abilities.append(Ability(mage_ability.name, mage_ability.type, mage_ability.value, mage_ability.cooldown))
        elif self.character_class.name == "Rogue":
            if name in rogue_abilities:
                rogue_ability = rogue_abilities[name]
                if len(self.abilities) < 3:
                    self.abilities.append(Ability(rogue_ability.name, rogue_ability.type, rogue_ability.value, rogue_ability.cooldown))

# Define the warrior, mage, and rogue abilities as you have them in your code
warrior_abilities = {
    "Slash": Ability("Slash", "attack", 20, 3),
    "Rage": Ability("Rage", "attack", 40, 5),
    "Cleave": Ability("Cleave", "attack", 30, 4),
}

mage_abilities = {
    "Fireball": Ability("Fireball", "attack", 30, 4),
    "Heal": Ability("Heal", "health", 40, 5),
    "Freeze": Ability("Freeze", "debuff", "Freeze the target", 5),
}

rogue_abilities = {
    "Backstab": Ability("Backstab", "attack", 25, 3),
    "Stealth": Ability("Stealth", "utility", "Become invisible", 5),
    "Poison Dart": Ability("Poison Dart", "attack", 20, 3),
}
