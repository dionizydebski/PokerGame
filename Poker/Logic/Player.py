from Enums.States import PlayerState


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.balance = 100
        self.state = PlayerState.FOLD
        self.current_bet = 0
        self.my_turn = False

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return [str(card) for card in self.hand]