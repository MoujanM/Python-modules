
from ex0 import Card, CreatureCard

print("\n=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")
dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
goblin = CreatureCard('Goblin Warrior', 2, 'Common', 2, 1)
print(f"CreatureCard Info:\n{dragon.get_card_info()}\n")

game_state = {"mana": 6}
print(f"Playing {dragon.name} with 6 mana available:")
print(f"Playable: {dragon.is_playable(6)}")
print(f"Play result: {dragon.play(game_state)}\n")

print(f"{dragon.name} attacks {goblin.name}:")
print(f"Attack result: {dragon.attack_target(goblin)}\n")

print("Testing insufficient mana (3 available):")
print(f"Playable: {dragon.is_playable(3)}\n")

print("Abstract pattern successfully demonstrated!")
