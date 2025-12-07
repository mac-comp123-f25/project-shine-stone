import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from utils.database import load_json, save_json, USERS

ICONS = {
    "morning": "assets/morning_logo.png",
    "afternoon": "assets/afternoon_logo.png",
    "evening": "assets/evening_logo.png",
    "all": "assets/all_time_logo.png"
}


class HabitsScreen(tk.Frame):
    def __init__(self, master, username, go_logout):
        super().__init__(master)
        self.master = master
        self.username = username
        self.go_logout = go_logout
        self.pack(fill="both", expand=True)

        # Load user data
        self.users = load_json(USERS)
        self.user = self.find_user(username)

        # Ensure fields exist
        for h in self.user["habits"]:
            h.setdefault("progress", 0)
            h.setdefault("timeframe", "all")

        # ===== Top bar =====
        top = tk.Frame(self, bg="white", height=70)
        top.pack(fill="x", side="top")

        self.logo = ImageTk.PhotoImage(Image.open("assets/main_logo.png").resize((60, 60)))
        tk.Label(top, image=self.logo, bg="white").place(x=20, y=5)

        tk.Label(top,
                 text=f"Hello {self.username}, Welcome Back!",
                 fg="#496646", bg="white",
                 font=("Helvetica", 20, "bold")
                 ).place(x=100, y=18)

        tk.Button(top, text="Sign Out",
                  bg="#e0e0e0", fg="#555",
                  command=self.go_logout).place(x=830, y=20)

        # ===== Center title =====
        tk.Label(self, text="HABIT CENTER",
                 bg="#d78888", fg="white",
                 font=("Helvetica", 14, "bold")
                 ).pack(fill="x")

        # ===== Two columns =====
        container = tk.Frame(self, bg="white")
        container.pack(fill="both", expand=True)

        self.left = tk.Frame(container, bg="white")
        self.left.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.95)

        self.right = tk.Frame(container, bg="white")
        self.right.place(relx=0.52, rely=0.02, relwidth=0.46, relheight=0.95)

        # Left Title
        tk.Label(self.left, text="MY HABITS",
                 bg="#a8c3a4", fg="white",
                 font=("Helvetica", 13, "bold"),
                 pady=5).pack(fill="x")

        self.render_habits()

        # Right Title
        tk.Label(self.right, text="NEW HABIT",
                 bg="#a8c3a4", fg="white",
                 font=("Helvetica", 13, "bold"),
                 pady=5).pack(fill="x")

        self.render_add_panel()

    # ----------------------------------------------------------
    # FIND USER
    # ----------------------------------------------------------
    def find_user(self, username):
        for u in self.users:
            if u["username"] == username:
                return u
        return None

    # ----------------------------------------------------------
    # RENDER HABITS LIST
    # ----------------------------------------------------------
    def render_habits(self):
        for widget in self.left.winfo_children()[1:]:
            widget.destroy()

        for habit in self.user["habits"]:
            frame = tk.Frame(self.left, bg="white")
            frame.pack(fill="x", anchor="w", pady=10)

            # ICON
            icon_path = ICONS.get(habit["timeframe"], ICONS["all"])
            img = ImageTk.PhotoImage(Image.open(icon_path).resize((40, 40)))
            lbl = tk.Label(frame, image=img, bg="white")
            lbl.image = img
            lbl.pack(side="left", padx=10)

            # NAME + PROGRESS
            tk.Label(frame,
                     text=habit["name"].title(),
                     font=("Helvetica", 12, "bold"),
                     fg="#496646", bg="white").pack(anchor="w")

            tk.Label(frame,
                     text=f"{habit['progress']} / {habit['goal']}",
                     fg="#777", bg="white").pack(anchor="w")

            # DONE BUTTON
            btn = tk.Button(frame,
                            text="Done",
                            bg="#a8c3a4", fg="white",
                            command=lambda h=habit: self.mark_done(h))
            btn.pack(anchor="e", pady=5)

    # ----------------------------------------------------------
    # MARK HABIT DONE
    # ----------------------------------------------------------
    def mark_done(self, habit):
        if habit["progress"] < habit["goal"]:
            habit["progress"] += 1
        else:
            messagebox.showinfo("Completed",
                                f"You already met your goal for {habit['name']}!")

        save_json(USERS, self.users)
        self.render_habits()

    # ----------------------------------------------------------
    # ADD PANEL
    # ----------------------------------------------------------
    def render_add_panel(self):
        tk.Label(self.right, text="Habit Name:", bg="white").pack(anchor="w")
        self.habit_name = tk.Entry(self.right, width=25)
        self.habit_name.pack(anchor="w", pady=5)

        tk.Label(self.right, text="Weekly Goal:", bg="white").pack(anchor="w")
        self.habit_goal = tk.Entry(self.right, width=10)
        self.habit_goal.pack(anchor="w", pady=5)

        tk.Label(self.right, text="Time of Day:", bg="white").pack(anchor="w", pady=10)

        # TIMEFRAME SELECTION
        self.time_choice = tk.StringVar(value="all")
        times = [("Morning", "morning"),
                 ("Afternoon", "afternoon"),
                 ("Evening", "evening"),
                 ("All Time", "all")]

        for label, val in times:
            tk.Radiobutton(self.right, text=label, bg="white",
                           variable=self.time_choice, value=val).pack(anchor="w")

        tk.Button(self.right, text="Add Habit",
                  bg="#a8c3a4", fg="white",
                  command=self.add_habit).pack(pady=20)

    # ----------------------------------------------------------
    # ADD HABIT
    # ----------------------------------------------------------
    def add_habit(self):
        name = self.habit_name.get().strip()
        goal = self.habit_goal.get().strip()
        timeframe = self.time_choice.get()

        if not name or not goal:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            goal = int(goal)
        except:
            messagebox.showerror("Error", "Daily Goal must be a number.")
            return

        self.user["habits"].append({
            "name": name,
            "goal": goal,
            "progress": 0,
            "timeframe": timeframe
        })

        save_json(USERS, self.users)
        messagebox.showinfo("Success", "Habit Added!")

        self.render_habits()
