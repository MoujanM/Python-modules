
from ex3 import FantasyCardFactory, AggressiveStrategy, GameEngine

print("\n=== DataDeck Game Engine ===\n")

engine = GameEngine()
print("Configuring Fantasy Card Game...")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine.configure_engine(factory, strategy)

print("\nSimulating aggressive turn...")

simulation_result = engine.simulate_turn()

hand_str = []
for card in simulation_result['cards']:
    name = card.name
    cost = card.cost
    hand_str.append(f'{name} ({cost})')
print(f'Hand: {hand_str}\n')

print("Turn execution:")
print(f'Strategy: {strategy.name}')
print(f'Actions: {simulation_result['actions']}\n')

print("Game report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")






