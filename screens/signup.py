import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from utils.database import load_json, save_json, USERS

class SignupScreen(tk.Frame):
    def __init__(self, master, go_login):
        super().__init__(master)
        self.master = master
        self.go_login = go_login
        self.pack(fill="both", expand=True)

        img = Image.open("assets/background.png")
        img = img.resize((950, 600))
        self.bg = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(self, bg="#eef2e1")
        frame.place(x=500, y=120, width=350, height=340)

        tk.Label(frame, text="Create Account",
                 bg="#eef2e1", fg="#496646",
                 font=("Helvetica", 22, "bold")).pack(pady=20)

        tk.Label(frame, text="Username:", bg="#eef2e1", fg="#496646").pack()
        self.username = tk.Entry(frame, width=30)
        self.username.pack(pady=5)

        tk.Label(frame, text="Password:", bg="#eef2e1", fg="#496646").pack()
        self.password = tk.Entry(frame, width=30, show="*")
        self.password.pack(pady=5)

        tk.Button(frame, text="Create Account",
                  bg="#e88c8c", fg="white",
                  relief="flat", command=self.create_account).pack(pady=15, ipadx=20)

        tk.Button(frame, text="Back to Login",
                  bg="#aac7a0", fg="white",
                  relief="flat", command=self.go_login).pack(ipadx=10, pady=5)

    def create_account(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return

        users = load_json(USERS)

        for u in users:
            if u["username"] == username:
                messagebox.showerror("Error", "User already exists.")
                return

        new_user = {
            "username": username,
            "password": password,
            "habits": []
        }

        users.append(new_user)
        save_json(USERS, users)

        messagebox.showinfo("Success", "Account created!")
        self.go_login()
