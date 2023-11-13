from player import Player
from quest import Quest
from character_class import CharacterClass
from location import Location
from monster import Monster
from random_events import RandomEvents
from ability import Ability
from item import Item
from saveload import SaveLoad
from combat import Combat
from ascii_art import ASCIIArt

import random

class GameManager:
    def __init__(self):
        self.player = None
        self.current_location = None
        self.game_world = {}
        self.monsters = []
        self.quests = []
        self.items = [Item("Health Potion", "Restores 20 health points"),
                      Item("Strength Elixir", "Increases attack by 10 for a limited time")]

    def run_game(self):
        self.initialize_game()
        self.setup_game_world()

        while True:
            self.display_location()
            choice = input("Enter your choice: ")

            if choice in self.current_location.interactions:
                action = self.current_location.interactions[choice]
                if action == "Explore":
                    self.explore()
                    self.check_level_up()
                elif action == "Visit the shop":
                    self.visit_shop()
                elif action == "Check your stats":
                    self.check_stats()
                elif action == "Abilities":
                    self.display_abilities()
                elif action == "View quests":
                    self.view_quests()
                elif action == "Interact with a friendly character":
                    self.interact_with_character()
                elif action == "Move to another location":
                    self.move_to_location()
                elif action == "Craft items":
                    self.craft_items()
                elif action == "Dice Game":
                    self.play_dice_game()
                elif action == "Save":
                    self.save_game()
                elif action == "Load":
                    self.load_game()
                elif action == "Quit":
                    print("Goodbye! Thanks for playing.")
                    break
                elif action.startswith("Complete Quest: "):
                    quest_name = action.replace("Complete Quest: ", "")
                    quest = self.get_quest_by_name(quest_name)
                    if quest:
                        self.complete_quest(quest)
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid choice. Please try again.")

    def initialize_game(self):
        player_name = input("Enter your character's name: ")
        print("Select your character class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        class_choice = input("Enter the number of your choice: ")

        if class_choice == "1":
            self.player = Player(player_name, warrior_class)
        elif class_choice == "2":
            self.player = Player(player_name, mage_class)
        elif class_choice == "3":
            self.player = Player(player_name, rogue_class)

        print(f"Welcome, {self.player.name} the {self.player.character_class.name}!")

    def setup_game_world(self):
        self.game_world = {
            "Village": Location("Village", "You are in a peaceful village.", {"1": "Explore", "2": "Visit the shop", "3": "Check your stats", "4": "Abilities", "5": "View quests", "6": "Interact with a friendly character", "7": "Move to another location", "8": "Craft items", "9": "Play dice game", "0": "Quit"}),
            "Forest": Location("Forest", "You are in a dark forest.", {"1": "Explore", "2": "Return to Village", "3": "Search for herbs", "4": "Fight a wild beast"}),
            "Mountains": Location("Mountains", "You've entered the treacherous mountain range.", {"1": "Climb higher", "2": "Return to Village", "3": "Mine for resources"}),
            "Castle": Location("Castle", "A grand castle stands before you.", {"1": "Enter the castle", "2": "Return to Village"}),
        }
        self.current_location = self.game_world["Village"]

        self.generate_monsters()
        self.generate_quests()

    def generate_monsters(self):
        self.monsters.append(Monster("Goblin", 25, 10, 5, 50, 20))
        self.monsters.append(Monster("Orc", 40, 15, 10, 75, 30))
        self.monsters.append(Monster("Dragon", 100, 30, 20, 150, 100))

    def generate_quests(self):
        self.quests.append(Quest("Defeat the Goblin", "Defeat 3 Goblins in the Forest", 50, 10, {"Goblin": 3}))
        self.quests.append(Quest("Retrieve the Lost Sword", "Find and return the lost sword to the Castle", 100, 20, {"Castle": 1}))
        self.quests.append(Quest("Collect Herbs", "Gather 5 healing herbs in the Forest", 30, 5, {"Forest Herbs": 5}))

    def display_location(self):
        if self.current_location.name in ["Village", "Forest", "Mountains", "Castle"]:
            print(getattr(ASCIIArt, self.current_location.name.lower())())
        print(self.current_location.description)
        print(self.current_location.get_interactions())
        
    def check_level_up(self):
        while self.player.experience >= self.player.get_experience_threshold():
            self.player.level_up()

    def explore(self):
        print("You venture into the unknown.")
        RandomEvents.explore_event(self.player)

        if random.random() < 0.3:
            self.battle_monster()
        else:
            print("You didn't encounter any monsters this time.")

    def battle_monster(self):
        monster = random.choice(self.monsters)
        monster_name = monster.name
        if monster_name in ["Goblin", "Orc", "Dragon"]:
            print(getattr(ASCIIArt, monster_name.lower())())
        else:
            print(f"A {monster_name} is approaching!")
        print(f"You engage in battle with a {monster.name}!")
        while self.player.is_alive() and monster.is_alive():
            self.player_attack(monster)

            if monster.is_alive():
                self.monster_attack(monster)

        if self.player.is_alive():
            print(f"You defeated the {monster.name}!")
            self.player.gain_experience(monster.experience_reward)
            self.player.gain_gold(monster.gold_reward)
        else:
            print("You were defeated by the monster!")

    def player_attack(self, monster):
        damage = Combat.calculate_damage(self.player, monster)
        print(f"You attack the {monster.name} for {damage} damage.")
        monster.take_damage(damage)

    def monster_attack(self, monster):
        damage = Combat.calculate_damage(monster, self.player)
        print(f"The {monster.name} attacks you for {damage} damage.")
        self.player.take_damage(damage)

    def use_ability(self):
        if not self.player.abilities:
            print("You don't have any abilities yet.")
            return

        print("Available Abilities:")
        for i, ability in enumerate(self.player.abilities, start=1):
            print(f"{i}. {ability.name} ({ability.description})")

        choice = input("Enter the number of the ability you want to use (0 to cancel): ")
        if choice.isdigit():
            index = int(choice) - 1
            abilities = self.player.abilities

            if 0 <= index < len(abilities):
                selected_ability = abilities[index]

                if selected_ability.type == "attack":
                    target_monster = self.select_target_monster()
                    if target_monster:
                        damage = Combat.calculate_ability_damage(self.player, selected_ability)
                        print(f"You use {selected_ability.name} on {target_monster.name} for {damage} damage.")
                        target_monster.take_damage(damage)
                elif selected_ability.type == "health":
                    health_restored = Combat.calculate_ability_healing(selected_ability)
                    self.player.heal(health_restored)
                    print(f"You use {selected_ability.name} and restore {health_restored} health points.")

                self.player.remove_ability(selected_ability)
            elif index == -1:
                print("You canceled ability usage.")
            else:
                print("Invalid ability number. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the ability you want to use.")

    def select_target_monster(self):
        print("Available Monsters:")
        for i, monster in enumerate(self.monsters, start=1):
            print(f"{i}. {monster.name} ({monster.health} HP)")

        choice = input("Enter the number of the monster you want to target (0 to cancel): ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(self.monsters):
                return self.monsters[index]
            elif index == -1:
                print("Ability usage canceled.")
            else:
                print("Invalid monster number. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the monster you want to target.")

    def visit_shop(self):
        # Implement shop logic
        pass

    def check_stats(self):
        print(f"{self.player.name}'s Stats:")
        print(f"Level: {self.player.level}")
        print(f"Health: {self.player.health}/{self.player.max_health}")
        print(f"Attack: {self.player.attack}")
        print(f"Defense: {self.player.defense}")
        print(f"Gold: {self.player.gold}")

    def view_quests(self):
        print("Available Quests:")
        for i, quest in enumerate(self.quests, start=1):
            if not quest.is_completed:
                print(f"{i}. {quest.name}: {quest.description} (XP Reward: {quest.experience_reward}, Gold Reward: {quest.gold_reward})")

        choice = input("Enter the number of the quest you want to accept (0 to cancel): ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(self.quests):
                quest = self.quests[index]
                self.player.accept_quest(quest)
            elif index == -1:
                print("Quest acceptance canceled.")
            else:
                print("Invalid quest number. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the quest you want to accept.")

    def accept_quest(self, quest):
        if quest not in self.player.completed_quests:
            if quest not in self.player.quests:
                self.player.quests.append(quest)
                print(f"You have accepted the quest: {quest.name}")
            else:
                print("You have already accepted this quest.")
        else:
            print("You have already completed this quest.")

    def calculate_quest_progress(self, quest):
        progress = 0

        for objective, required_count in quest.objectives.items():
            if objective in self.player.defeated_monsters:
                defeated_count = self.player.defeated_monsters[objective]
                if defeated_count >= required_count:
                    progress += 1
            elif objective in self.player.collected_items:
                collected_count = self.player.collected_items[objective]
                if collected_count >= required_count:
                    progress += 1

        return progress

    def complete_quest(self, quest):
        if quest in self.player.quests:
            quest_progress = self.calculate_quest_progress(quest)
            if quest_progress >= quest.required_progress:
                print(f"Quest completed: {quest.name}")
                self.player.gain_experience(quest.experience_reward)
                self.player.gain_gold(quest.gold_reward)
                self.reward_player(quest)
                quest.is_completed = True
                self.player.quests.remove(quest)
                self.player.completed_quests.append(quest)
            else:
                print(f"Quest progress: {quest_progress}/{quest.required_progress}")
        else:
            print("You have not accepted this quest yet.")

    def interact_with_character(self):
        # Implement interaction with friendly characters
        pass

    def move_to_location(self):
        print("Available Locations:")
        for i, (location_name, location) in enumerate(self.game_world.items(), start=1):
            print(f"{i}. {location_name}")

        choice = input("Enter the number of the location you want to move to (0 to cancel): ")
        if choice.isdigit():
            index = int(choice) - 1
            locations = list(self.game_world.keys())

            if 0 <= index < len(locations):
                new_location_name = locations[index]
                new_location = self.game_world[new_location_name]
                if new_location_name == "Village":
                    print("You have returned to the Village.")
                else:
                    self.current_location = new_location
                    print(f"You have moved to {new_location_name}.")
            elif index == -1:
                print("Location change canceled.")
            else:
                print("Invalid location number. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the location you want to move to.")

    def craft_items(self):
        # Implement crafting system
        pass

    def play_dice_game(self):
        # Implement a mini-game

     def interact_with_character(self):
        # Implement interaction with friendly characters
        pass

    def move_to_location(self):
        print("Available Locations:")
        for i, (location_name, location) in enumerate(self.game_world.items(), start=1):
            print(f"{i}. {location_name}")

        choice = input("Enter the number of the location you want to move to (0 to cancel): ")
        if choice.isdigit():
            index = int(choice) - 1
            locations = list(self.game_world.keys())

            if 0 <= index < len(locations):
                new_location_name = locations[index]
                new_location = self.game_world[new_location_name]
                self.current_location = new_location
                print(f"You have moved to {new_location_name}.")
            elif index == -1:
                print("Location change canceled.")
            else:
                print("Invalid location number. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the location you want to move to.")

    def craft_items(self):
        # Implement crafting system
        pass

    def play_dice_game(self):
        # Implement a mini-game
        pass

    def reward_player(self, quest):
        if quest.is_completed:
            reward_item = random.choice(self.items)
            self.player.inventory.append(reward_item)
            print(f"Congratulations! You received a {reward_item.name} as a quest reward.")

    def complete_quest(self, quest):
        if quest.is_completed:
            print(f"Quest completed: {quest.name}")
            self.player.gain_experience(quest.experience_reward)
            self.player.gain_gold(quest.gold_reward)
            self.reward_player(quest)
            quest.is_completed = True

    def get_quest_by_name(self, name):
        for quest in self.quests:
            if quest.name == name:
                return quest

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

warrior_class = CharacterClass("Warrior", "A skilled warrior with high physical strength.", warrior_abilities)
mage_class = CharacterClass("Mage", "A spellcaster with powerful magical abilities.", mage_abilities)
rogue_class = CharacterClass("Rogue", "A stealthy and agile rogue skilled in deception.", rogue_abilities)