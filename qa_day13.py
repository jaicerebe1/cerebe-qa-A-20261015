# cerebe.io QA run B day 13 2026-10-27
import subprocess
API_KEY = 'sk-test-FAKE-day13'  # hardcoded secret (fake)

def run(cmd):
    return subprocess.call(cmd, shell=True)  # shell injection

def last(xs):
    return xs[len(xs)]  # off-by-one IndexError
