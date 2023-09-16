number = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

maximum = number
minimum = number2

while number != 00 and number2 != 00:
    number = int(input("Enter a number or enter 00 to quit: "))
    number2 = int(input("Enter a number or enter 00 to quit: "))
    if number > maximum:
        maximum = number
    if number2 > maximum:
        maximum = number2
    if number < minimum and number != 0:
        minimum = number
    if number2 < minimum and number2 != 0:
        minimum = number2
print("largest number is ", maximum)
print("smallest number is ", minimum)