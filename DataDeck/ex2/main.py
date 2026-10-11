
from ex0 import Card
from ex2 import EliteCard

def print_abilities(cls):

    for parent in cls.__bases__:
        methods = []
        for name in parent.__dict__:
            if name[0] != '_':
                methods.append(name)

        print(f"- {parent.__name__}: {methods}")

print("\n=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print_abilities(EliteCard)

warrior = EliteCard('Arcane Warrior', 3, 'legendary', 5, 7)
game_state = {'mana': 10}
try:
    warrior.play(game_state)
    print("\nPlaying Arcane Warrior (Elite Card):\n")
except ValueError as e:
    print(f'{e}')

warrior.attack('Enemy')
warrior.defend(5)
combat_stats = warrior.get_combat_stats()
print("Combat phase:")
print(f"Attack result: {combat_stats['attack']}")
print(f"Defense result: {combat_stats['defense']}")

warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])
warrior.mana_pool = 4
warrior.channel_mana(3)
magic_stats = warrior.get_magic_stats()
print("\nMagic phase:")
print(f"Spell cast: {magic_stats['spell']}")
print(f"Mana channel: {magic_stats['mana']}")

print("\nMultiple interface implementation successful!")
