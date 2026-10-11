
from ex0.Card import Card, CardType, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        
        if attack < 0 or health <= 0:
            raise Exception("Creature's attack and health must be positive!")
        else:
            self.attack_power = attack
            self.health = health

        self.id: str = ''
        self.rating: int = 0

        self.card_type = CardType.TOURNAMENT
        self.stats: dict = {
                    'combat': {}, 
                    'tournament': {'matches': 0, 'wins': 0, 'losses': 0}}

    #from card
    def play(self, game_state: dict) -> dict:
        
        available_mana = game_state.get("mana", 0)

        if self.is_playable(available_mana):

            game_state["mana"] -= self.cost

            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Tournament unit summoned to battlefield!'}
        else:
            raise Exception('Insufficient mana!')
    
    #from Combatable
    def attack(self, target) -> dict:
        attack_stat = {'attacker': self.name,
                'target': target,
                'damage': self.attack_power,}
        self.stats['combat']['attack'] = attack_stat
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
        self.stats['combat']['defense'] = defense_stat
        return defense_stat

    def get_combat_stats(self) -> dict:
        return self.stats['combat']
    
    #from Rankable
    def calculate_rating(self) -> int:
        rarity_bonus = 0
        if self.rarity == Rarity.RARE:
            rarity_bonus = 50
        elif self.rarity == Rarity.LEGENDARY:
            rarity_bonus = 10
        
        self.rating = 1000 + (self.attack_power * 20) + (self.health * 10) + rarity_bonus
        return self.rating 

    def get_tournament_stats(self) -> dict:
        return self.stats['tournament']
    
    def update_wins(self, wins: int) -> None:
        self.stats['tournament']['wins'] = wins
    
    def update_losses(self, losses: int) -> None:
        self.stats['tournament']['losses'] = losses

    def get_rank_info(self) -> dict:
        
        return self.stats['tournament']
