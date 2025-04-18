from unittest import TestCase

from deck import Card
from game import Match, Round, Turn
from play import setup_game, deal_cards, play_match


class TestGame(TestCase):
    def setUp(self):
        self.game = setup_game()

    def test_setup(self):

        self.assertEqual(len(self.game.teams), 2)
        self.assertEqual(len(self.game.get_initial_player_order()), 4)

    def test_deal_cards(self):

        deal_cards(self.game.get_initial_player_order())

        total_cards = []
        for player in self.game.get_initial_player_order():
            self.assertEqual(len(player.hand), 9)
            total_cards.extend(player.hand)

        self.assertEqual(len(set(total_cards)), 36)

    def test_match(self):
        match = play_match(self.game.get_initial_player_order())

        self.assertEqual(len(match.rounds), 9)
        self.assertEqual(self.game.teams[0].points + self.game.teams[1].points, 157)

    def test_winner_lead_suit(self):
        match = Match(self.game.get_initial_player_order())
        match.trump = 'Diamonds'

        round = Round(match)
        round.add_turn(Turn(match.player_order[0], Card('Hearts', '10')))
        round.add_turn(Turn(match.player_order[1], Card('Hearts', '8')))
        round.add_turn(Turn(match.player_order[2], Card('Spades', 'Ace')))
        round.add_turn(Turn(match.player_order[3], Card('Clubs', 'Jack')))

        self.assertEqual(match.player_order[0], round.determine_winner())

    def test_winner_lead_suit_higher(self):
        match = Match(self.game.get_initial_player_order())
        match.trump = 'Diamonds'

        round = Round(match)
        round.add_turn(Turn(match.player_order[0], Card('Hearts', '10')))
        round.add_turn(Turn(match.player_order[1], Card('Clubs', '8')))
        round.add_turn(Turn(match.player_order[2], Card('Spades', 'Ace')))
        round.add_turn(Turn(match.player_order[3], Card('Hearts', 'Jack')))

        self.assertEqual(match.player_order[3], round.determine_winner())

    def test_winner_trump(self):
        match = Match(self.game.get_initial_player_order())
        match.trump = 'Diamonds'

        round = Round(match)
        round.add_turn(Turn(match.player_order[0], Card('Hearts', '10')))
        round.add_turn(Turn(match.player_order[1], Card('Diamonds', '8')))
        round.add_turn(Turn(match.player_order[2], Card('Spades', 'Ace')))
        round.add_turn(Turn(match.player_order[3], Card('Clubs', 'Jack')))

        self.assertEqual(match.player_order[1], round.determine_winner())

    def test_winner_trump_nine(self):
        match = Match(self.game.get_initial_player_order())
        match.trump = 'Diamonds'

        round = Round(match)
        round.add_turn(Turn(match.player_order[0], Card('Hearts', '10')))
        round.add_turn(Turn(match.player_order[1], Card('Diamonds', '9')))
        round.add_turn(Turn(match.player_order[2], Card('Diamonds', 'Ace')))
        round.add_turn(Turn(match.player_order[3], Card('Clubs', 'Jack')))

        self.assertEqual(match.player_order[1], round.determine_winner())


