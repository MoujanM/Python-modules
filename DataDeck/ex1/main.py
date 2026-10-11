
from ex1 import Deck, ArtifactCard, SpellCard
from ex0 import CreatureCard

print("\n=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...")
card1 = CreatureCard('Fire Dragon', 5, 'legendary', 7, 5)
card2 = SpellCard('Lightning Bolt', 3, 'common', 'damage')
card3 = ArtifactCard('Mana Crystal', 2, 'common', 5, 'Permanent: +1 mana per turn')

deck = Deck()
deck.add_card(card1)
deck.add_card(card2)
deck.add_card(card3)

print(deck.get_deck_stats())

print("\nDrawing and playing cards:\n")
game_state = {'mana': 10}
while deck.cards:
    card = deck.draw_card()
    print(f"Draw: {card.name} ({card.card_type.value})")
    print(f"Play result: {card.play(game_state)}")
    print()

print("Polymorphism in action: Same interface, different card behaviors!")
