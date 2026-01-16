import sqlite3
import pickle
import subprocess

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
