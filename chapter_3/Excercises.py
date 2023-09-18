number1 = int(input("Enter first number: "))
number2 = int(input("Enter a second number: "))

if number1 == number2:
    print(f"{number1} is equal to {number2}")
else:
    print(f"{number1} is not equal to {number2}")

if number1 > number2:
    print(f"{number1} is greater than {number2}")
else:
    print(f"{number1} is less than {number2}")

if number1 >= number2:
    print(f"{number1} is greater than or equal to {number2}")
else:
    print(f"{number1} is less than or equal to {number2}")