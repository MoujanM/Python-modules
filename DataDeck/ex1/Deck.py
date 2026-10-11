
from ex0.Card import Card, CardType, Rarity
import random
from enum import Enum


class Deck():
    cards: list = []
    stats: dict = {}
    
    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        return 

    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def draw_card(self) -> Card:
        return self.cards.pop() if self.cards else None

    def get_deck_stats(self) -> dict:
        if not self.cards:
            return {'total_cards': 0, 'avg_cost': 0.0}
        
        stats = {'total_cards': 0,
                 'creatures': 0,
                 'spells': 0,
                 'artifacts': 0,
                 'avg_cost': 0.0}

        count = 0
        total_cost = 0.0
        for card in self.cards:
            count += 1
            total_cost += card.cost
            if card.card_type == CardType.CREATURE:
                stats['creatures'] += 1
            elif card.card_type == CardType.SPELL:
                stats['spells'] += 1
            elif card.card_type == CardType.ARTIFACT:
                stats['artifacts'] += 1

        avg = total_cost / count
        stats.update({'total_cards': count,
                      'avg_cost': ("%.1f" % avg)})
        return stats
