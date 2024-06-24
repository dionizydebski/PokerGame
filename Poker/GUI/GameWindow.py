import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

from Enums.States import GameState, PlayerState
from Logic.Deck import Deck
from Logic.Player import Player


class GameWindow:

    def __init__(self):
        self.pot = 0
        self.current_bet = 0
        self.deck = Deck()
        self.players = self.setup_players(5)
        self.table = self.deck.deal(5)
        self.game_state = GameState.FIRST
        self.gui()

        self.start_game()

    def gui(self):
        self.root = tk.Tk()
        self.root.title("Poker")
        self.root.geometry("1080x720")

        self.setup_balance_and_pot_frame()
        self.setup_players_frame()
        self.setup_table_frame()
        self.setup_cards_frame()
        self.setup_buttons_frame()
        self.setup_grid()

        self.root.mainloop()
    def setup_balance_and_pot_frame(self):
        balance_frame = tk.Frame(self.root)
        balance_frame.grid(row=0, column=0)

        self.balance_label = tk.Label(balance_frame, text=f"Balance: ${self.players[0].balance}",font=("Arial", 12))
        self.balance_label.grid(row=0, column=0, pady=10)

        pot_frame = tk.Frame(self.root)
        pot_frame.grid(row=0, column=2)

        self.pot_label = tk.Label(pot_frame, text=f"Pot: ${self.pot}", font=("Arial", 12))
        self.pot_label.grid(row=0, column=0, pady=10)

        self.current_bet_label = tk.Label(pot_frame, text=f"Current bet: ${self.current_bet}", font=("Arial", 12))
        self.current_bet_label.grid(row=1, column=0, pady=10)
    def setup_players_frame(self):
        players_frame = tk.Frame(self.root)
        players_frame.grid(row=0, column=1)

        tmp = 0

        for i in range(1,len(self.players)):
            name_label = tk.Label(players_frame, text=self.players[i].name, font=("Arial", 12))
            name_label.grid(row=0, column=tmp)

            balance_label = tk.Label(players_frame, text=f"$ {self.players[i].balance}", font=("Arial", 12))
            balance_label.grid(row=0, column=tmp+1)

            first_card_image = self.get_card_image(self.players[i].hand[0],60,92)
            sec_card_image = self.get_card_image(self.players[i].hand[1],60,92)

            first_card_label = tk.Label(players_frame, image=first_card_image)
            first_card_label.image = first_card_image
            first_card_label.grid(row=1, column=tmp, pady=10)

            sec_card_label = tk.Label(players_frame, image=sec_card_image)
            sec_card_label.image = sec_card_image
            sec_card_label.grid(row=1, column=tmp+1, pady=10)

            tmp += 2
    def setup_table_frame(self):
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=1, column=1)

        self.table_labels = []

        for i in range(len(self.table)):
            image = self.get_card_image("back",120,184)
            label = tk.Label(table_frame, image=image)
            label.image = image
            label.grid(row=0, column=i)
            self.table_labels.append(label)
    def setup_cards_frame(self):
        cards_frame = tk.Frame(self.root)
        cards_frame.grid(row=2, column=1)

        first_card_image = self.get_card_image(self.players[0].hand[0],120,184)
        sec_card_image = self.get_card_image(self.players[0].hand[1],120,184)

        first_card_label = tk.Label(cards_frame, image=first_card_image)
        first_card_label.image = first_card_image
        first_card_label.grid(row=0, column=0, pady=10)

        sec_card_label = tk.Label(cards_frame, image=sec_card_image)
        sec_card_label.image = sec_card_image
        sec_card_label.grid(row=0, column=1, pady=10)
    def setup_buttons_frame(self):
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=3, column=1, padx=10, pady=10, sticky=tk.S)

        bet_button = tk.Button(button_frame, text="Bet", font=("Arial", 13), command=self.bet)
        bet_button.grid(row=0, column=0, padx=10, pady=10)

        fold_button = tk.Button(button_frame, text="Fold", font=("Arial", 13), command=self.fold)
        fold_button.grid(row=0, column=1, padx=10, pady=10)

        check_button = tk.Button(button_frame, text="Check", font=("Arial", 13), command=self.check)
        check_button.grid(row=0, column=3, padx=10, pady=10)
    def setup_grid(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1, minsize=150)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1, minsize=150)
    def get_card_image(self, card_name, width, hight):
        cards_dir = os.path.join(os.path.dirname(__file__), 'Cards')
        card_image_path = os.path.join(cards_dir, f"{card_name}.png")
        original_image = Image.open(card_image_path)
        resized_image = original_image.resize((width, hight), Image.NEAREST)
        return ImageTk.PhotoImage(resized_image)
    def setup_players(self, num_of_players):
        tmp = []
        for i in range(num_of_players):
            tmp.append(Player(f"Player {i}", self.deck.deal(2)))
        tmp[0].my_turn = True
        return tmp
    def update_table(self):
        tmp = self.game_state.value

        for i in range(len(self.table_labels)-tmp):
            image = self.get_card_image(self.table[i], 120, 184)
            self.table_labels[i].config(image=image)
            self.table_labels[i].image = image
    def check_if_auction_ended(self):
        result = True
        for player in self.players:
            if not (player.state == PlayerState.FOLD or player.current_bet == self.current_bet):
                result = False

        if result and self.game_state != GameState.RIVER:
            self.current_bet = 0
            self.current_bet_label.config(text=f"Current bet: ${self.current_bet}")
            self.update_game_state()
            self.update_table()
    def update_game_state(self):
        if self.game_state == GameState.FIRST:
            self.game_state = GameState.FLOP
        elif self.game_state == GameState.FLOP:
            self.game_state = GameState.TURN
        else:
            self.game_state = GameState.RIVER
    def bet(self):
        if self.players[0].my_turn:
            user_input = simpledialog.askinteger("💲", "How much: ")

            if not user_input:
                return
            elif user_input > self.players[0].balance:
                messagebox.showwarning("Error", "Not enough money :<")
                return
            elif user_input == 0:
                messagebox.showwarning("Error", "Rly ?")
                return
            elif user_input < self.current_bet:
                messagebox.showwarning("Error", "Bet must me >= current bet 😡")
                return
            else:
                self.players[0].balance -= user_input
                self.pot += user_input
                self.current_bet = user_input
                self.balance_label.config(text=f"Balance: ${self.players[0].balance}")
                self.pot_label.config(text=f"Pot: ${self.pot}")
                self.current_bet_label.config(text=f"Current bet: ${self.current_bet + self.players[0].current_bet}")
                # self.players[0].my_turn = False
                self.players[0].current_bet = user_input
                self.check_if_auction_ended()
    def fold(self):
        if self.players[0].my_turn:
            self.players[0].state = PlayerState.FOLD
            self.players[0].my_turn = False
            self.check_if_auction_ended()
    def check(self):
        if self.players[0].my_turn and self.current_bet == 0:
            self.players[0].my_turn = False
            self.check_if_auction_ended()


GameWindow()