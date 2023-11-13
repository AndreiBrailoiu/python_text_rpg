# Text-Based RPG Game in Python

## Overview

This is a text-based RPG (Role-Playing Game) implemented in Python. In this game, players can create a character, explore various locations, engage in battles with monsters, complete quests, and interact with the game world. The game is structured using several classes that represent different aspects of the game.

## Classes

### `CharacterClass`

Represents the character classes in the game, such as Warrior, Mage, and Rogue. Each class has a name, description, and a set of abilities.

### `Combat`

Handles combat-related calculations, including damage calculation between attackers and defenders.

### `Item`

Represents items in the game, such as health potions and strength elixirs. Each item has a name and description.

### `Location`

Represents different locations in the game world. Each location has a name, description, and a set of interactions that players can choose from.

### `Monster`

Represents monsters that players can encounter and battle in the game. Each monster has attributes such as name, health, attack, defense, experience reward, and gold reward.

### `Player`

Represents the player's character in the game. Players can level up, gain gold, collect items, complete quests, and engage in battles with monsters.

### `Quest`

Represents quests that players can undertake. Each quest has a name, description, experience reward, gold reward, and objectives.

### `RandomEvents`

Handles random events that can occur during exploration, such as finding treasure chests, encountering friendly spirits, or facing challenges.

### `SaveLoad`

Manages the saving and loading of game states using the `pickle` module.

### `Ability`

Represents abilities that characters can learn and use in battles.

### `ASCIIArt`

Provides ASCII art for different locations, monsters, and characters in the game.

### `GameManager`

Manages the overall flow of the game, including player interactions, location changes, quest handling, and more.

## How to Play

To play the game, run the `main()` function in the script. Players can create a character by choosing a name and a character class (Warrior, Mage, or Rogue). Once in the game, players can explore different locations, engage in battles, complete quests, and interact with the game world.

Players can use abilities in battles, view their stats, check available quests, and move between locations. The game also features a saving and loading system to continue progress.

**Note:** The game script includes placeholder methods for shop visit, crafting, and dice game, which are not yet implemented.
