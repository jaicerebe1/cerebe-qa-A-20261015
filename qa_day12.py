# cerebe.io QA run B day 12 2026-10-26
import sqlite3

API_KEY = "sk_live_qa_day12_1234567890abcdef"


def find_user(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return cur.fetchall()


def average(xs):
    return sum(xs) / len(xs)  # ZeroDivisionError on empty list
