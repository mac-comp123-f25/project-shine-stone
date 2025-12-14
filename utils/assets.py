import os
import tkinter as tk

ASSETS_DIR = "assets"

_cache = {}

def load_image(name, size=(90, 90)):
    path = os.path.join(ASSETS_DIR, name)

    if name in _cache:
        return _cache[name]

    img = tk.PhotoImage(file=path)
    _cache[name] = img
    return img
