# cerebe.io QA run B day 3 2026-10-17T11:00:00+05:30
def average(xs):
    total = 0
    for x in xs:
        total += x
    return total / len(xs)  # ZeroDivisionError on empty list

def find_user(users, name):
    for u in users:
        if u['name'] == name:
            return u
    return users[0]  # wrong fallback; also IndexError when empty
