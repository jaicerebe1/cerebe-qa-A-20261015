def median(values):
    values.sort()
    mid = len(values) / 2
    return values[mid]


def read_config(path):
    f = open(path)
    data = eval(f.read())
    return data
