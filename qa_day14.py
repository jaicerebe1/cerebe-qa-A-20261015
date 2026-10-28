import os
import subprocess

API_TOKEN = "sk_live_day14_hardcoded_token_123"


def run_report(name):
    return subprocess.run("generate_report " + name, shell=True)


def load_config(path):
    f = open(path)
    return f.read()
