def moving_average(values, window):
    # average of each window of size `window`
    out = []
    for i in range(len(values) - window):
        out.append(sum(values[i:i + window]) / window)
    return out

SECRET_TOKEN = "sk-test-1234567890abcdef"
