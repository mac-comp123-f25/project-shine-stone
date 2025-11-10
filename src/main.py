import tkinter as tk
import random
import time

# === Sentences ===
sentences = [
    "This is a typing test",
    "Type the sentence above this one",
    "The quick brown fox jumps over the lazy dog",
    "I love to type because it is so much fun",
    "Type as fast as you can without making mistakes",
    "The rain in Spain falls mainly on the plain"
]

# === Globals ===
current_sentence = ""
score = 0
mistakes = 0
word_count = 0
start_time = None
test_duration = 60  # seconds
running = False


# === Functions ===
def start_test():
    """Start or restart the test."""
    global current_sentence, score, mistakes, word_count, start_time, running
    score = 0
    mistakes = 0
    word_count = 0
    random.shuffle(sentences)
    entry_box.config(state="normal")
    start_button.config(state="disabled")
    result_label.config(text="")
    time_label.config(text=f"Time Left: {test_duration}s")
    progress_label.config(text="Correct: 0 | Mistakes: 0")
    next_sentence()
    start_time = time.time()
    running = True
    countdown(test_duration)
    entry_box.delete(0, tk.END)
    entry_box.focus()


def countdown(t):
    """Countdown timer."""
    global running
    if t > 0 and running:
        time_label.config(text=f"Time Left: {t}s")
        window.after(1000, countdown, t - 1)
    else:
        end_test()


def next_sentence():
    """Display the next sentence."""
    global current_sentence
    if sentences:
        current_sentence = sentences.pop()
        sentence_label.config(text=current_sentence)
        entry_box.delete(0, tk.END)
    else:
        end_test()


def check_sentence(event=None):
    """Check user's input when pressing Enter."""
    global score, mistakes, word_count
    typed = entry_box.get()
    if not running:
        return

    if typed == current_sentence:
        sentence_label.config(fg="limegreen")
        score += 1
        word_count += len(current_sentence.split())
        window.after(300, lambda: sentence_label.config(fg="white"))
        next_sentence()
    else:
        sentence_label.config(fg="red")
        mistakes += 1
        window.after(300, lambda: sentence_label.config(fg="white"))
    progress_label.config(text=f"Correct: {score} | Mistakes: {mistakes}")
    entry_box.delete(0, tk.END)


def end_test():
    """Stop test and show results."""
    global running
    running = False
    entry_box.config(state="disabled")
    elapsed = time.time() - start_time
    wpm = word_count / (elapsed / 60) if elapsed > 0 else 0
    accuracy = (score / (score + mistakes)) * 100 if (score + mistakes) > 0 else 0
    sentence_label.config(text="Test complete!", fg="gold")
    result_label.config(
        text=f"✅ Correct: {score}\n❌ Mistakes: {mistakes}\n🕒 Time: {elapsed:.1f}s\n⌨️ WPM: {wpm:.1f}\n🎯 Accuracy: {accuracy:.1f}%",
        fg="white"
    )
    start_button.config(state="normal")


# === GUI Setup ===
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("800x500")
window.configure(bg="#1e1e1e")

title_label = tk.Label(
    window, text="Typing Speed Test", font=("Helvetica", 24, "bold"),
    fg="pink", bg="#1e1e1e"
)
title_label.pack(pady=20)

sentence_label = tk.Label(
    window, text="Click Start to begin!", wraplength=700,
    font=("Helvetica", 16), fg="white", bg="#1e1e1e"
)
sentence_label.pack(pady=40)

entry_box = tk.Entry(
    window, font=("Helvetica", 16), width=60,
    bg="#2b2b2b", fg="white", insertbackground="white"
)
entry_box.pack(pady=10)
entry_box.bind("<Return>", check_sentence)

progress_label = tk.Label(
    window, text="Correct: 0 | Mistakes: 0", font=("Helvetica", 14),
    fg="lightgray", bg="#1e1e1e"
)
progress_label.pack(pady=5)

time_label = tk.Label(
    window, text="Time Left: 60s", font=("Helvetica", 14, "bold"),
    fg="lightblue", bg="#1e1e1e"
)
time_label.pack(pady=5)

result_label = tk.Label(
    window, text="", font=("Helvetica", 14),
    fg="white", bg="#1e1e1e"
)
result_label.pack(pady=20)

start_button = tk.Button(
    window, text="Start Test", command=start_test,
    font=("Helvetica", 14, "bold"),
    bg="pink", fg="black", activebackground="hotpink"
)
start_button.pack(pady=20)

window.mainloop()

