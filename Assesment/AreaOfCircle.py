import math

rad = float(input("Enter the radius of the circle: "))


def area(radius):
    result = (radius ** 2) * math.pi
    return f" {result:.3f}"


print(area(rad))
