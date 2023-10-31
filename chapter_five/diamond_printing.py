for space in range(5):
    for value in range(space, 5):
        print(" ", end=" ")
    for value2 in range(space + 1):
        print("*", end=" ")
    for value3 in range(space):
        print("*", end=" ")
    print()
for second_shape in range(5):
    for value4 in range(second_shape):
        print(" ", end=" ")
    print(end="    ")
    for value5 in range(second_shape, 3):
        print("*", end=" ")
    for value6 in range(second_shape, 4):
        print("*", end=" ")
    print()