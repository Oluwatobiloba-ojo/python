for num in range(10):
    for value in range(num):
        print("*", end=" ")
    for space in range(num, 10):
        print(" ", end=" ")
    for value in range(num, 10):
        print("*", end=" ")
    for value2 in range(num):
        print(" ", end=" ")
    print(end='  ')
    for value3 in range(num):
        print(" ", end=" ")
    for value6 in range(num, 10):
        print("*", end=" ")
    for value4 in range(num, 10):
        print(" ", end=" ")
    for value5 in range(num):
        print("*", end=" ")
    print()

