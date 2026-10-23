import hashlib

API_KEY = "sk_live_day9_9f8e7d6c5b4a"

def average(values):
    return sum(values) / len(values)

def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()
