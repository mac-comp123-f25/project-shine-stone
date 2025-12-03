import tkinter as tk
from utils.styles import *
from utils.assets import load_image

class Stats(tk.Frame):
    def __init__(self, master, user, switch):
        super().__init__(master, bg=PRIMARY_BG)
        self.user = user
        self.switch = switch

        logo = load_image("ok_streak.png")
        tk.Label(self, image=logo, bg=PRIMARY_BG).pack(pady=10)
        self.logo = logo

        tk.Label(self, text="Statistics",
                 font=FONT_H1, fg=ACCENT, bg=PRIMARY_BG).pack(pady=5)

        tk.Label(self, text="(Statistics coming soon)",
                 font=FONT_BODY, bg=PRIMARY_BG).pack(pady=20)

        tk.Button(self, text="Back", font=FONT_BODY,
                  bg=BUTTON_BG, fg=BUTTON_FG,
                  command=lambda: self.switch("dashboard")).pack(pady=10)
