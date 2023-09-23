for count in range(1, 10):
    for index in range(1, count):
        print(" *", end="")
    print()
    for index in range(1, count):
        print(" *", end="")
    for row in range(count, 10):
        print(" ", end=" ")
    for row in range(count, 10):
        print("*", end="")
    for space in range(1, count):
        print(" ", end="")
    for space in range(1, count):
        print(" ", end="")
    for index in range(count, 10):
        print("*", end="")
    print()
