import tkinter as tk
from utils.styles import *
from utils.assets import load_image

class Dashboard(tk.Frame):
    def __init__(self, master, user, switch):
        super().__init__(master, bg=PRIMARY_BG)
        self.user = user
        self.switch = switch

        # Logo
        logo = load_image("main_logo.png")
        tk.Label(self, image=logo, bg=PRIMARY_BG).pack(pady=10)
        self.logo = logo

        tk.Label(self, text="Today's Habits",
                 font=FONT_H1, fg=ACCENT, bg=PRIMARY_BG).pack(pady=5)

        self.habit_frame = tk.Frame(self, bg=PRIMARY_BG)
        self.habit_frame.pack(pady=10)

        self.load_habits()

        tk.Button(self, text="Manage Habits", font=FONT_BODY,
                  bg=BUTTON_BG, fg=BUTTON_FG,
                  command=lambda: self.switch("manage")).pack(pady=5)

        tk.Button(self, text="Statistics", font=FONT_BODY,
                  bg=BUTTON_BG, fg=BUTTON_FG,
                  command=lambda: self.switch("stats")).pack(pady=5)

    def load_habits(self):
        for w in self.habit_frame.winfo_children():
            w.destroy()

        if not self.user["habits"]:
            tk.Label(self.habit_frame, text="No habits yet.",
                     font=FONT_BODY, bg=PRIMARY_BG).pack()
            return

        for habit in self.user["habits"]:
            tk.Label(self.habit_frame, text=f"• {habit}",
                     font=FONT_BODY, fg=TEXT, bg=PRIMARY_BG).pack(anchor="w", padx=20)
