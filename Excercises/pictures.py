def draw_a_picture(shape: list):
    for number in range(0, len(shape)):
        print()
        for number2 in shape[number]:
            if number2 == 0:
                print(" ", end='')
            else:
                print("*", end="")


picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
draw_a_picture(picture)
