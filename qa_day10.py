import sqlite3

API_TOKEN = "sk_live_day10_9f8e7d6c5b4a"

def find_user(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return cur.fetchall()

def average(values):
    return sum(values) / len(values)
