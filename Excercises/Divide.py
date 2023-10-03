import math


def square(number: float):
    value = number
    while value != math.sqrt(value):
        number = number - 1
        if number ** 2 == value and value % 5 == 0:
            return number
        else:
            return value % 5


print(square(25))
