
from ex0 import Card, CardType, Rarity
from enum import Enum
from abc import ABC, abstractmethod
from ex2 import Combatable, Magical

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_type = CardType.ELITE

        if attack < 0 or health <= 0:
            raise Exception("Creature's attack and health must be positive!")
        else:
            self.attack_power = attack
            self.health = health

        self.mana_pool = 0
        self.stats: dict = {'combat': {}, 'magic': {}}

    # abstract method from Card
    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana", 0)

        if self.is_playable(available_mana):

            game_state["mana"] -= self.cost

            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Elite unit summoned to battlefield!'}
        else:
            raise Exception('Insufficient mana!')

    # abstract methods from Combatable
    def attack(self, target: str) -> dict:
        attack_stat = {'attacker': self.name,
                'target': target,
                'damage': self.attack_power,
                'combat_type': 'melee'}
        self.stats['combat'].update({'attack': attack_stat})
        return attack_stat

    def defend(self, incoming_damage: int) -> dict:
        
        if incoming_damage < self.cost:
            blocked = incoming_damage
        else:
            blocked = self.cost

        taken = incoming_damage - blocked if incoming_damage > blocked else 0

        self.health -= taken

        alive = bool(self.health > 0)

        defense_stat = {'defender': self.name,
                'damage_taken': taken,
                'damage_blocked': blocked,
                'still_alive': alive}
        self.stats['combat'].update({'defense': defense_stat})
        return defense_stat
    
    def get_combat_stats(self) -> dict:
        return self.stats['combat']
    
    # abstract methods from Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_stat = {'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': self.cost}

        self.stats['magic'].update({'spell': spell_stat})

        return spell_stat

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        
        mana_stat = {'channeled': amount,
                'total_mana': self.mana_pool}

        self.stats['magic'].update({'mana': mana_stat})
        return mana_stat

    def get_magic_stats(self) -> dict:
        return self.stats['magic']


