import tkinter as tk
from tkinter import messagebox
import os

class LoginWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Poker")
        self.root.geometry("275x275")

        self.label = tk.Label(self.root, text="Welcome to Poker :3", font=("Arial",18))
        self.label.pack(padx=15, pady=15)

        self.label_login = tk.Label(self.root, text="Login:")
        self.label_login.pack(padx=5, pady=5)

        self.entry_login = tk.Entry(self.root)
        self.entry_login.pack(padx=5, pady=5)

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack(padx=5, pady=5)

        self.entry_password = tk.Entry(self.root)
        self.entry_password.pack(padx=5, pady=5)

        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack(padx=5, pady=5)

        self.button_register = tk.Button(self.root, text="Register", command=self.register)
        self.button_register.pack(padx=5, pady=5)

        self.root.mainloop()

    def login(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if not os.path.exists("passwords.txt"):
            messagebox.showerror("Error", "Register first :>")
            return

        if login and password:
            with open("passwords.txt", "r") as file:
                for line in file:
                    saved_login, saved_password = line.strip().split(' ')
                    if saved_login == login and saved_password == password:
                        self.root.destroy()
                        from GUI.MenuWindow import MenuWindow
                        MenuWindow()
                        return
            messagebox.showerror("Error", "There is no such user :o")
        else:
            messagebox.showerror("Error", "Please provide correct credentials ;<")

    def register(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if login and password:
            with open("passwords.txt", "a") as file:
                file.write(f"{login} {password}\n")
            messagebox.showinfo("Success", "The data has been saved ;)")
        else:
            messagebox.showerror("Error", "Please provide correct credentials ;<")