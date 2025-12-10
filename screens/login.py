import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from utils.database import get_user

class LoginScreen(tk.Frame):
    def __init__(self, master, go_signup, go_habits):
        super().__init__(master)
        self.master = master
        self.go_signup = go_signup
        self.go_habits = go_habits
        self.pack(fill="both", expand=True)

        img = Image.open("assets/background.png")
        img = img.resize((950, 600))
        self.bg = ImageTk.PhotoImage(img)

        tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(self, bg="#eef2e1")
        frame.place(x=500, y=120, width=350, height=340)

        tk.Label(frame, text="Habit Tracker",
                 bg="#eef2e1", fg="#496646",
                 font=("Helvetica", 22, "bold")).pack(pady=20)

        tk.Label(frame, text="Username:", bg="#eef2e1",
                 fg="#496646", font=("Helvetica", 11, "bold")).pack(fill="x", padx=25)
        self.username = tk.Entry(frame, width=30)
        self.username.pack(pady=5)

        tk.Label(frame, text="Password:", bg="#eef2e1",
                 fg="#496646", font=("Helvetica", 11, "bold")).pack(fill="x", padx=25)
        self.password = tk.Entry(frame, width=30, show="*")
        self.password.pack(pady=5)

        tk.Button(frame, text="Log In", bg="#e88c8c",
                  fg="#2e4e1f", relief="flat",
                  font=("Helvetica", 11, "bold"),
                  command=self.try_login).pack(pady=20, ipadx=40, ipady=6)

        tk.Button(frame, text="New user? Sign up",
                  bg="#aac7a0", fg="#2e4e1f",
                  relief="flat", font=("Helvetica", 10, "bold"),
                  command=self.go_signup).pack(ipadx=10, ipady=3)

    def try_login(self):
        username = self.username.get().strip()
        password = self.password.get().strip()
        user = get_user(username)

        if user is None:
            messagebox.showerror("Error", "User does not exist.")
            return

        if user["password"] != password:
            messagebox.showerror("Error", "Wrong password.")
            return

        self.go_habits(username)
