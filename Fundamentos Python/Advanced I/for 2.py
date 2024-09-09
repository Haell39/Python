#range(start, stop[, step])
def sum(previous, current):
    for i in range(10):
        current = i
        previous += current
    return previous

previous = 0
current = 0
print(sum(previous, current))
