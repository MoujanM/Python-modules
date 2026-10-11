
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        super().__init__()
        self.name = 'AggressiveStrategy'


    def execute_turn(self, hand: list['Card'], battlefield: list) -> dict:
        
        # playing low-cost creatures first
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        game_state = {'mana': 15}

        targets = self.prioritize_targets(battlefield) if battlefield else ['Enemy Player']
        targets_attacked = []

        for cost in range(1, 7):
            for card in hand:
                if card.cost == cost:
                    card.play(game_state)
                    cards_played.append(card)
                    mana_used += card.cost

        card_names = []
        for card in cards_played:
            card_names.append(card.name)
        
        # combat phase
        for card in cards_played:
            target = targets[0]
            try:
                atk = card.attack
                targets_attacked.append(target)
                damage_dealt += card.attack
                card.attack_target(target)
            except (TypeError, AttributeError):
                pass
            try:
                card.resolve_effect(target)
                targets_attacked.append(target)
                damage_dealt += card.cost
            except (TypeError, AttributeError):
                pass

        target_names = []
        for target in targets_attacked:
            try:
                target_names.append(target.name)
            except AttributeError:
                target_names.append(str(target))
        
        return {'cards_played': card_names,
                'targets_attacked': target_names,
                'mana_used': mana_used,
                'damage_dealt': damage_dealt}
        

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        priority = []

        for target in available_targets:
            if target == "Enemy Player":
                priority.append(target)
        
        for target in available_targets:
            if target is CreatureCard:
                priority.append(target)

        return priority

