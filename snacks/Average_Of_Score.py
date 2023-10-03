
def average(*args):
    total = 0
    for i in args:
        total += i
    value = total / len(args)
    return f"{value:.2f}"


print(average(1, 2, 3, 4, 6, 7, 8, 9, 9, 10))
