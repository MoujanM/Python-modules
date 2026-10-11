from ex4 import Rankable, TournamentCard, TournamentPlatform

print("\n=== DataDeck Tournament Platform ===\n")

platform = TournamentPlatform()

print("Resgistering Tournament Cards...\n")
card1 = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
card1.id = 'dragon_001'
card2 = TournamentCard("Ice Wizard", 4, "Rare", 3, 4)
card2.id = 'wizard_001'

test_cards = [card1, card2]
for card in test_cards:
    print(f'{platform.register_card(card)} (ID: {card.id}):')
    print(f'- Interfaces: {[parent.__name__ for parent in card.__class__.__bases__]}')
    print(f'- Rating: {card.rating}')
    print('- Record: 0-0')
    print()

print("Creating tournament match...")
match_result = platform.create_match(card1.id, card2.id)
print(f'Match result: {match_result}')

print("\nTournament Leaderboard:")
leaderboard = platform.get_leaderboard()
print(*leaderboard, sep='\n')

print("\nPlatform Report:")
print(platform.generate_tournament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
print('All abstract patterns working. together harmoniously!')