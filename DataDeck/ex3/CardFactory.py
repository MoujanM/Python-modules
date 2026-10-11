
from abc import ABC, abstractmethod
from ex0 import Card, CreatureCard, CardType
from ex1 import ArtifactCard, SpellCard, Deck



class CardFactory(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

    