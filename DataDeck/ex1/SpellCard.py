
from ex0.Card import Card, CardType, Rarity
from enum import Enum

class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.card_type = CardType.SPELL
        try:
            self.effect_type = EffectType(effect_type)
            if self.effect_type == EffectType.DAMAGE:
                self.effect_str = f'Deal {cost} damage to target'
            elif self.effect_type == EffectType.HEAL:
                self.effect_str = f'Heal target by +{cost} health'
            elif self.effect_type == EffectType.BUFF:
                self.effect_str = f'Buff target with +{cost} strength'
        except ValueError:
            raise ValueError(f"Unknown effect type: {effect_type}")

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana", 0)

        if self.is_playable(available_mana):
            game_state['mana'] -= self.cost
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect_str}
        else:
            raise Exception("Not enough mana!")
    
    def resolve_effect(self, targets: list) -> dict:
        power = self.cost
        total_damage = 0
        results = []

        for target in targets:
            is_player = False

            try:
                if target == 'Enemy Player' or target == 'Player':
                    is_player = True
            except:
                pass

            if self.effect_type == EffectType.DAMAGE:
                if not is_player:
                    target.health -= power
                total_damage += power
                return {'effect': self.effect_str}
            elif self.effect_type == EffectType.HEAL:
                if not is_player:
                    target.health += power
                total_damage += power
                return {'effect': self.effect_str}
            elif self.effect_type == EffectType.BUFF:
                if not is_player:
                    target.attack += power
                total_damage += power
                return {'effect': self.effect_str}


    def get_card_info(self) -> dict:
        info = super().get_card_info(self)
        info.update({'effect': self.resolve_effect()['effect']})

        return info
        