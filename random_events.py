import random

class RandomEvents:
    @staticmethod
    def explore_event(player):
        event_chance = random.random()
        if event_chance < 0.2:
            print("You found a hidden treasure chest!")
            player.gain_gold(50)
        elif event_chance < 0.4:
            print("You stumbled upon a rare item!")
            player.gain_item("Rare Potion")
        elif event_chance < 0.6:
            print("You discovered a mystical fountain. Drink from it?")
            choice = input("Enter your choice (1. Drink, 2. Ignore): ")
            if choice == "1":
                print("You feel rejuvenated and gain 20 health!")
                player.heal(20)
            else:
                print("You decided not to drink from the fountain.")
        else:
            print("You had a peaceful exploration.")

    @staticmethod
    def forest_event(player):
        event_chance = random.random()
        if event_chance < 0.3:
            print("You encountered a friendly forest spirit. It offered to heal you.")
            player.heal(20)
        elif event_chance < 0.6:
            print("You found a rare mushroom. Consume it for a stat boost?")
            choice = input("Enter your choice (1. Consume, 2. Leave it): ")
            if choice == "1":
                print("You gained a temporary boost to your attack!")
                player.gain_attack(10)
            else:
                print("You decided not to consume the mushroom.")
        else:
            print("Your journey through the forest was uneventful.")
    
    @staticmethod
    def mountain_event(player):
        event_chance = random.random()
        if event_chance < 0.2:
            print("A snowstorm is approaching. Take shelter or brave the storm?")
            choice = input("Enter your choice (1. Take shelter, 2. Brave the storm): ")
            if choice == "1":
                print("You found a cave and took shelter. You're safe from the storm.")
            else:
                print("You bravely face the snowstorm, but it takes a toll on your health.")
                player.take_damage(10)
        elif event_chance < 0.4:
            print("You discovered a hidden gem mine. Collect some gems?")
            choice = input("Enter your choice (1. Collect, 2. Leave): ")
            if choice == "1":
                print("You gained precious gems, which you can sell for gold.")
                player.gain_gold(100)
            else:
                print("You decided not to collect gems.")
        else:
            print("Your mountain adventure was uneventful.")

    @staticmethod
    def castle_event(player):
        event_chance = random.random()
        if event_chance < 0.2:
            print("You were invited to a royal feast. Partake in the feast?")
            choice = input("Enter your choice (1. Partake, 2. Decline): ")
            if choice == "1":
                print("You enjoyed the royal feast and gained new friends.")
                player.gain_experience(30)
            else:
                print("You politely declined the invitation.")
        elif event_chance < 0.4:
            print("A mysterious wizard offers to enhance your abilities. Accept the offer?")
            choice = input("Enter your choice (1. Accept, 2. Decline): ")
            if choice == "1":
                print("The wizard enhances your magical abilities!")
                player.gain_ability("Enhanced Magic")
            else:
                print("You declined the wizard's offer.")
        else:
            print("Your visit to the castle was uneventful.")