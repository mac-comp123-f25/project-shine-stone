import tkinter as tk
from screens.login import LoginScreen
from screens.signup import SignupScreen
from screens.habits import HabitsScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Habit Tracker")
        self.geometry("950x600")
        self.resizable(False, False)

        self.current_screen = None
        self.show_login()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

    def show_login(self):
        self.clear_screen()
        self.current_screen = LoginScreen(
            master=self,
            go_signup=self.show_signup,
            go_habits=self.show_habits
        )

    def show_signup(self):
        self.clear_screen()
        self.current_screen = SignupScreen(
            master=self,
            go_login=self.show_login
        )

    def show_habits(self, username):
        self.clear_screen()
        self.current_screen = HabitsScreen(
            master=self,
            username=username,
            go_logout=self.show_login
        )


if __name__ == "__main__":
    App().mainloop()
