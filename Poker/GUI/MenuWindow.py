import tkinter as tk

class MenuWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu")
        self.root.geometry("500x400")

        self.label = tk.Label(self.root, text="We have money to lose 😎", font=("Arial", 18))
        self.label.pack(padx=15, pady=15)

        self.button_play = tk.Button(self.root, text="Play", command=self.startGame, width=20, height=2)
        self.button_play.pack(padx=15, pady=15)

        self.button_games_history = tk.Button(self.root, text="Games history", command=self.seeGameHistory, width=20, height=2)
        self.button_games_history.pack(padx=15, pady=15)

        self.button_saved_games = tk.Button(self.root, text="Saved games", command=self.seeSavedGames, width=20, height=2)
        self.button_saved_games.pack(padx=15, pady=15)

        self.button_logout = tk.Button(self.root, text="Logout", command=self.logout, width=20, height=2)
        self.button_logout.pack(padx=15, pady=15)

        self.root.mainloop()

    def startGame(self):
        self.root.destroy()
        from GUI.GameWindow import GameWindow
        GameWindow()

    def seeGameHistory(self):
        self.root.destroy()
        from GUI.GameHistoryWindow import GameHistoryWindow
        GameHistoryWindow()

    def seeSavedGames(self):
        self.root.destroy()
        from GUI.SavedGamesWindow import SavedGamesWindow
        SavedGamesWindow()

    def logout(self):
        self.root.destroy()
        from GUI.LoginWindow import LoginWindow
        LoginWindow()