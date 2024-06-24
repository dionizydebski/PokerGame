from Logic.Deck import Deck
from Logic.Player import Player


class Game:
    def __init__(self):
        self.pot = 0
        self.deck = Deck()
        self.players = [Player("Me"), Player("Player 1")]
        self.table = []
        self.start_game()


    def start_game(self):
        self.table.extend(self.deck.deal(5))

        for player in self.players:
            player.receive_cards(self.deck.deal(2))