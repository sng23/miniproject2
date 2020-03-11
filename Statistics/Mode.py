

def mode(data):
    max_count = (0, 0)
    for num in data:
        occurrences = data.count(num)
        if occurrences > max_count[0]:
            max_count = (occurrences, num)
    return max_count[1]

