import random


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        for player in players:
            player.set_team(self)
        self.points = 0

    def add_points(self, points):
        self.points += points

    def show_players(self):
        return ', '.join(player.name for player in self.players)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.team = None

    def set_team(self, team):
        self.team = team

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self):
        return self.hand.pop() if self.hand else None

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def eligible_cards(self, round):
        if not self.hand:
            return []
        if round.get_lead_suit() is None:
            return self.hand

        lead_suit_cards = [
            card for card in self.hand
            if card.suit == round.get_lead_suit()
        ]

        if lead_suit_cards:
            trump_suit_cards = [
                card for card in self.hand
                if card.suit == round.match.trump
            ]
            return lead_suit_cards + trump_suit_cards
        else:
            return [
                card for card in self.hand
                if card.suit == round.get_lead_suit()
            ]

    def choose_card(self, round):
        # Placeholder for actual logic to choose a card
        eligible_cards = self.eligible_cards(round.match.trump)

        return random.choice(eligible_cards) if eligible_cards else None

    def choose_trump(self, trump_options):
        # Placeholder for actual logic to choose a trump
        return random.choice(trump_options) if trump_options else None

    def __repr__(self):
        return f"Player({self.name})"
