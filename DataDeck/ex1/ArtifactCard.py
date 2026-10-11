
from ex0.Card import Card, CardType, Rarity

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.card_type = CardType.ARTIFACT
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana", 0)

        if self.is_playable(available_mana):
            game_state['mana'] -= self.cost
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect}
        else:
            raise Exception("Not enough mana!")

    def activate_ability(self) -> dict:
        return {'effect': self.effect}
