def area_of_triangle(base, height):
    return base * height * 0.5


bases = int(input("Enter the base of the triangle: "))
heights = int(input("Enter the height of the triangle: "))
print(area_of_triangle(base=bases, height=heights))
