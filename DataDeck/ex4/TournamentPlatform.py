from ex4.TournamentCard import TournamentCard

class TournamentPlatform():
    def __init__(self):
        self.cards: list = []
        self.stats: dict = {'total_cards': 0,
                            'matches_played': 0,
                            'avg_rating': 0,
                            'platform_status': ''}

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        self.stats['total_cards'] += 1
        self.stats['platform_status'] = 'active'

        return card.name

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        player1 = None
        player2 = None
        
        for card in self.cards:
            if card.id == card1_id:
                player1 = card
            if card.id == card2_id:
                player2 = card

        if not player1 or not player2:
            raise Exception("Card not found - register all cards first!")

        player1.calculate_rating()
        player2.calculate_rating()
        if player1.attack_power > player2.attack_power:
            winner, loser = player1, player2
        else:
            winner, loser = player2, player1
        
        winner.rating += 16
        loser.rating -= 16
        
        winner.update_wins(1)
        loser.update_losses(1)
        self.stats['matches_played'] += 1

        return {'winner': winner.id, 
                'loser': loser.id,
                'winner_rating': winner.rating,
                'loser_rating': loser.rating}

    def get_leaderboard(self) -> list:
        
        count = 0
        for card in self.cards:
            count += 1

        i = 0
        while i < count:
            j = 0
            while j < count - i - 1:
                if self.cards[j].rating < self.cards[j + 1].rating:
                    self.cards[j], self.cards[j + 1] = self.cards[j + 1], self.cards[j]
                j += 1
            i += 1

        leaderboard = []
        idx = 1
        for card in self.cards:
            record = f'{card.stats['tournament']['wins']}-{card.stats['tournament']['losses']}'
            entry = f'{idx}. {card.name} - Rating: {card.rating} ({record})'
            leaderboard.append(entry)
            idx += 1

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating = 0
        count = 0

        for card in self.cards:
            count += 1
            total_rating += card.rating

        self.stats['avg_rating'] = total_rating // count if count > 0 else 0
        
        return self.stats