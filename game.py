from deck import ranks_trump, ranks, suits

class Game:
    def __init__(self, teams):
        self.teams = teams
        self.match = []

    def add_match(self, match):
        # add scores to teams based on the match results
        self.match.append(match)

    def get_initial_player_order(self):
        return [self.teams[0].players[0], self.teams[1].players[0], self.teams[0].players[1], self.teams[1].players[1]]

class Match:
    def __init__(self, players):
        self.rounds = []
        self.trump = None
        self.player_order = players

    def process_round(self, round):
        self.add_points_for_round(round, last_round=len(self.rounds) == 8)
        self.rounds.append(round)

        index_of_winner = self.player_order.index(round.determine_winner())
        self.player_order = self.player_order[index_of_winner:] + self.player_order[:index_of_winner]

    def choose_trump(self):
        self.trump = self.player_order[0].choose_trump(suits)

    def add_points_for_round(self, round, last_round=False):
        winner = round.determine_winner()
        if winner:
            winner.team.add_points(round.calculate_points())
            if last_round:
                winner.team.add_points(5)

class Turn:
    def __init__(self, player, card):
        self.player = player
        self.card = card

    def __repr__(self):
        return f"{self.player.name} plays {self.card}"

class Round:
    def __init__(self, match):
        self.cards_played = []
        self.match = match

    def add_turn(self, turn):
        self.cards_played.append(turn)

    def get_lead_suit(self):
        return self.cards_played[0].card.suit if self.cards_played else None

    def determine_winner(self):
        if not self.cards_played:
            return None

        trump_cards = [t for t in self.cards_played if t.card.suit == self.match.trump]
        if trump_cards:
            winning_card = max(trump_cards, key=lambda t: ranks_trump.index(t.card.rank))
            return winning_card.player
        else:
            # If no trump cards played, find the highest card of the lead suit
            lead_suit = self.get_lead_suit()
            lead_cards = [t for t in self.cards_played if t.card.suit == lead_suit]
            if lead_cards:
                winning_card = max(lead_cards, key=lambda t: ranks.index(t.card.rank))
                return winning_card.player
            else:
                # No valid cards played, no winner
                return None

    def calculate_points(self):
        points_round = 0
        for turn in self.cards_played:
            points_round += turn.card.get_points(self.match.trump)

        return points_round