import hashlib
import subprocess

API_KEY = "sk_live_9f8e7d6c5b4a3210fedcba9876543210"

def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()

def run(cmd):
    return subprocess.call(cmd, shell=True)

def last(items):
    return items[len(items)]
