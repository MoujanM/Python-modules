
from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
from ex1 import ArtifactCard, SpellCard
from .CardFactory import CardFactory
from enum import Enum
import random

class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.name = 'FantasyCardFactory'
        self._cards : dict = {CardType.CREATURE: [],
                          CardType.SPELL : [],
                          CardType.ARTIFACT: [],
                          CardType.ELITE: []}
        
        creatures_data = [
            {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary", "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2, "rarity": "Common", "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4, "rarity": "Rare", "attack": 3, "health": 4},
            {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon", "attack": 4, "health": 2},
            {"name": "Stone Golem", "cost": 6, "rarity": "Rare", "attack": 5, "health": 8},
            {"name": "Healing Angel", "cost": 4, "rarity": "Rare", "attack": 2, "health": 6},
            {"name": "Forest Spirit", "cost": 1, "rarity": "Common", "attack": 1, "health": 1}]

        spells_data = [{"name": "Lightning Bolt", "cost": 3, "rarity": "Common", "effect_type": "damage"},
            {"name": "Fireball", "cost": 4, "rarity": "Uncommon", "effect_type": "damage"},
            {"name": "Divine Light", "cost": 5, "rarity": "Rare", "effect_type": "heal"},
            {"name": "Ice Shard", "cost": 2, "rarity": "Common", "effect_type": "damage"}]

        artifacts_data = [{"name": "Mana Crystal", "cost": 2, "rarity": "Common", "durability": 5, "effect": "Permanent: +1 mana per turn"},
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare", "durability": 4, "effect": "Permanent: Draw an extra card each turn"},
            {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary", "durability": 7, "effect": "Permanent: +1 spell damage"}]    
    
        for data in creatures_data:
            self._cards[CardType.CREATURE].append(CreatureCard(*data.values()))

        for data in spells_data:
            self._cards[CardType.SPELL].append(SpellCard(*data.values()))

        for data in artifacts_data:
            self._cards[CardType.ARTIFACT].append(ArtifactCard(*data.values()))
    

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature_list = self._cards[CardType.CREATURE]
        try:
            name_or_power = name_or_power.upper()
            for creature in creature_list:
                if creature.name == name_or_power:
                    return creature
        except AttributeError:
            pass

        try:
            name_or_power += 0
            for creature in creature_list:
                if creature.attack == name_or_power:
                    return creature
        except TypeError:
            pass

        return random.choice(creature_list)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spell_list = self._cards[CardType.SPELL]

        try:
            name_or_power = name_or_power.upper()
            for spell in spell_list:
                if spell.name == name_or_power:
                    return spell
        except AttributeError:
            pass

        try:
            name_or_power += 0
            for spell in spell_list:
                if spell.cost == name_or_power:
                    return spell
        except TypeError:
            pass

        return random.choice(spell_list)


    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifact_list = self._cards[CardType.ARTIFACT]

        try:
            name_or_power = name_or_power.upper()
            for artifact in artifact_list:
                if artifact.name == name_or_power:
                    return artifact
        except AttributeError:
            pass

        try:
            name_or_power += 0
            for artifact in artifact_list:
                if artifact.cost == name_or_power:
                    return artifact
        except TypeError:
            pass

        return random.choice(artifact_list)

    def create_themed_deck(self, size: int) -> dict:
        
        card_share = size // 4
        num_creatures = card_share * 2

        random.shuffle(self._cards[CardType.CREATURE])
        random.shuffle(self._cards[CardType.SPELL])
        random.shuffle(self._cards[CardType.ARTIFACT])

        deck_creatures = self._cards[CardType.CREATURE][0 : num_creatures]
        deck_spells = self._cards[CardType.SPELL][0 : card_share]
        deck_artifacts = self._cards[CardType.ARTIFACT][0 : card_share]

        deck = {'creatures': [], 'spells': [], 'artifacts': []}
        for creature in deck_creatures:
            deck['creatures'].append(creature.name)
        for spell in deck_spells:
            deck['spells'].append(spell.name)
        for artifact in deck_artifacts:
            deck['artifacts'].append(artifact.name)

        return deck

    def register_new_type(self, card_type: CardType, cards: str | list) -> None:
        self._cards[card_type] = cards

    def get_supported_types(self) -> dict:
        card_count = 0
        idx = 0
        
        return {{self._cards[CardType]}}