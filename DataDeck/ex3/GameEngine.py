
from .CardFactory import CardFactory 
from .GameStrategy import GameStrategy

class GameEngine():
    def __init__(self):
        self.stats: dict = {'turns_simulated': 0, 'strategy_used': '',
                            'total_damage': 0, 'cards_created': 0}
        self.strategy: GameStrategy = None
        self.hand: list =[]
        self.factory: CardFactory = None
    
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.strategy = strategy
        self.factory = factory
        self.stats['strategy_used'] = strategy.name
        
        print(f'Factory: {factory.name}')
        print(f'Strategy: {strategy.name}')
        print(f'Available types: {factory.create_themed_deck(5)}')

    def simulate_turn(self) -> dict:
        card1 = self.factory.create_creature()
        self.hand.append(card1)
        card2 = self.factory.create_creature()
        self.hand.append(card2)
        card3 = self.factory.create_spell()
        self.hand.append(card3)
        
        self.stats['turns_simulated'] += 1
        self.stats['cards_created'] += 3
        
        turn_report = self.strategy.execute_turn(self.hand, [])

        self.stats['total_damage'] += turn_report.get('damage_dealt')
        
        return {'cards': self.hand, 'actions': turn_report}

    def get_engine_status(self) -> dict:
        return self.stats