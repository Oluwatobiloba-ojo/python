for first_shape in range(1, 19):
    for value in range(first_shape, 19):
        print(" ", end=" ")
    for value2 in range(first_shape):
        print("*", end=" ")
    for value3 in range(1, first_shape):
        print("*", end=" ")
    print()
for second_shape in range(1, 19):
    for value4 in range(second_shape):
        print(" ", end=" ")
    print(end="    ")
    for value5 in range(second_shape, 17):
        print("*", end=" ")
    for value6 in range(second_shape, 18):
        print("*", end=" ")
    print()
