from ex0.Card import Card, CardType, Rarity



class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_type = CardType.CREATURE
        if attack < 0 or health <= 0:
            raise Exception("Creature's attack and health must be positive!")
        else:
            self.attack = attack
            self.health = health
    
    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana", 0)

        if self.is_playable(available_mana):
            game_state["mana"] -= self.cost
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        else:
            raise Exception('Insufficient mana!')

    def attack_target(self, target: ("CreatureCard", str)) -> dict:
        try:
            if self.attack >= target.health:
                resolved = True
            elif target.attack >= self.health:
                resolved = False
        except (TypeError, AttributeError):
            resolved = True 

        return {'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': resolved}


    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({'attack': self.attack, 'health': self.health})
        return info