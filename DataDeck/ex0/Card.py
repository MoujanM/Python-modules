from abc import ABC, abstractmethod
from enum import Enum

class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"
    TOURNAMENT = "Tournament"


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        try:
            self.rarity = Rarity(rarity)
        except ValueError:
            raise ValueError(f"Invalid rarity: {rarity}. Must be one of {[r.value for r in Rarity]}")
        self.card_type = None

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity.value,
                "type": self.card_type.value if self.card_type else "Unknown"}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

