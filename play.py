from deck import Deck
from game import Game, Match, Round, Turn
from player import Player, Team

def setup_game():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")
    player4 = Player("Player 4")

    team1 = Team("Team 1", [player1, player2])
    team2 = Team("Team 2", [player3, player4])

    game = Game([team1, team2])
    return game

def deal_cards(players):
    deck = Deck()
    deck.shuffle()

    for _ in range(9):
        for player in players:
            player.add_card(deck.deal())

def play_match(players):
    match = Match(players)
    match.choose_trump()
    deal_cards(players)

    for _ in range(9):  # Play 9 rounds
        round = play_round(match)
        match.process_round(round)
        # TODO: Add logic to determine if the match is over and update team scores

    return match

def play_round(match: Match):
    round = Round(match)
    for player in match.player_order:
        card = player.play_card()
        if card:
            turn = Turn(player, card)
            round.add_turn(turn)
            print(turn)
    return round

game = setup_game()
players = game.get_initial_player_order()

while game.teams[0].points < 2500 and game.teams[1].points < 2500:
    print("Starting a new match...")
    match = play_match(players)
    game.add_match(match)

    players = players[3:] + players[:3]  # Rotate players for the next match

    # Update team scores based on match results
    print(f"Match finished. Scores: {game.teams[0].points} - {game.teams[1].points}")

