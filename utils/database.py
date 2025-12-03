# utils/storage.py
import json
import os

USERS = "data/users.json"

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def get_user(username):
    users = load_json(USERS)
    for u in users:
        if u["username"] == username:
            return u
    return None

def update_user(updated):
    users = load_json(USERS)
    for i, u in enumerate(users):
        if u["username"] == updated["username"]:
            users[i] = updated
            break
    save_json(USERS, users)

