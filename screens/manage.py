import tkinter as tk
from utils.styles import *
from utils.database import update_user
from utils.assets import load_image

class ManageHabits(tk.Frame):
    def __init__(self, master, user, switch):
        super().__init__(master, bg=PRIMARY_BG)
        self.user = user
        self.switch = switch

        logo = load_image("ok_calendar.png")
        tk.Label(self, image=logo, bg=PRIMARY_BG).pack(pady=10)
        self.logo = logo

        tk.Label(self, text="Manage Habits",
                 font=FONT_H1, fg=ACCENT, bg=PRIMARY_BG).pack(pady=5)

        self.list_frame = tk.Frame(self, bg=PRIMARY_BG)
        self.list_frame.pack()

        self.update_list()

        # Add new habit
        self.entry = tk.Entry(self, font=FONT_BODY)
        self.entry.pack(pady=10)

        tk.Button(self, text="Add Habit", font=FONT_BODY,
                  bg=BUTTON_BG, fg=BUTTON_FG,
                  command=self.add_habit).pack(pady=5)

        tk.Button(self, text="Back", font=FONT_BODY,
                  bg=BUTTON_BG, fg=BUTTON_FG,
                  command=lambda: self.switch("dashboard")).pack()

    def update_list(self):
        for w in self.list_frame.winfo_children():
            w.destroy()

        for habit in self.user["habits"]:
            row = tk.Frame(self.list_frame, bg=PRIMARY_BG)
            row.pack(fill="x", pady=2)

            tk.Label(row, text=habit, font=FONT_BODY,
                     bg=PRIMARY_BG, fg=TEXT).pack(side="left")

            tk.Button(row, text="Remove", bg="#ff8a80", fg="white",
                      command=lambda h=habit: self.remove_habit(h)).pack(side="right")

    def add_habit(self):
        name = self.entry.get().strip()
        if name:
            self.user["habits"].append(name)
            update_user(self.user)
            self.update_list()
            self.entry.delete(0, tk.END)

    def remove_habit(self, habit):
        self.user["habits"].remove(habit)
        update_user(self.user)
        self.update_list()
