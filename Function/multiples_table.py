def tables_of_square_cube(number: int):
    count = 1
    while count <= number:
        print(f"{count:> 4} {count ** 2:> 4} {count ** 3:> 4}")
        count += 1


tables_of_square_cube(9)