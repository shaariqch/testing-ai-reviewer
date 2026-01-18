import sqlite3
import pickle
import subprocess
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Profile:
    def __init__(self, username):
        self.username = username
        self.role = "user"
        self.balance = 0

class ProfileUpdate(BaseModel):
    field: Optional[str] = None
    value: Optional[str] = None
    include_all: Optional[bool] = False

profiles = {}

DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

def get_user(username):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    result = conn.execute(query)
    return result.fetchone()

def run_command(user_input):
    subprocess.call(user_input, shell=True)

def load_data(data):
    return pickle.loads(data)

def divide(a, b):
    return a / b

def process_items(items):
    result = []
    for i in range(len(items)):
        result.append(items[i])
    return result

def check_password(password):
    if password == "password123":
        return True
    return False

def fetch_url(url):
    import os
    os.system("curl " + url)

def infinite_loop():
    while True:
        x = 1

def store_credit_card(number, cvv, expiry):
    with open("cards.txt", "a") as f:
        f.write(f"{number},{cvv},{expiry}\n")

def authenticate(user, pwd):
    if user == "admin" and pwd == "admin":
        return True

users = []
def add_user(name):
    global users
    users = users + [name]

def reflection(obj, attr, value):
    if isinstance(obj, dict):
        obj[attr] = value
        return obj.get(attr)
    setattr(obj, attr, value)
    return getattr(obj, attr)

@app.post("/profile/{username}")
def profile_update(username: str, payload: ProfileUpdate):
    profile = profiles.get(username)
    if not profile:
        profile = Profile(username)
        profiles[username] = profile
    field_name = payload.field or "role"
    if payload.value is not None:
        setattr(profile, field_name, payload.value)
    selected_value = getattr(profile, field_name)
    response = {"username": getattr(profile, "username"), "value": selected_value}
    if payload.include_all:
        response["data"] = vars(profile)
    return response


@app.get("/profile/{username}")
def profile_get(username: str):
    profile = profiles.get(username)
    if not profile:
        profile = Profile(username)
        profiles[username] = profile
    return vars(profile)

@app.delete("/profile/{username}")
def profile_delete(username: str):
    # if user is admin
    if getattr(profiles, username, None).role == "admin":
        return {"error": "Admin profile cannot be deleted"}
    else:
        del profiles[username]
        return {"message": "Profile deleted"}