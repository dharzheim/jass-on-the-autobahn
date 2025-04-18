suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
ranks_trump = ['6', '7', '8', '10', 'Queen', 'King', 'Ace', '9', 'Jack']

points = {
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 10,
    'Jack': 2,
    'Queen': 3,
    'King': 4,
    'Ace': 11
}

points_trump = {
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 14,
    '10': 10,
    'Jack': 20,
    'Queen': 3,
    'King': 4,
    'Ace': 11
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_points(self, trump_suit):
        if self.suit == trump_suit:
            return points_trump[self.rank]
        else:
            return points[self.rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None