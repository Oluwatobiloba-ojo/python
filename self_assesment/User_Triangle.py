lengthOfTriangle = int(input("Enter a value for length of the triangle: "))

for count in range(0, lengthOfTriangle + 1):
    for column in range(0, count):
        print("* ", end="")
    print()
