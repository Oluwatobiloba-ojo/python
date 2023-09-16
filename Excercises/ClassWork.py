number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

maximum = number1

if number2 > maximum:
    maximum = number2
if number3 > maximum:
    maximum = number3

print(maximum)
