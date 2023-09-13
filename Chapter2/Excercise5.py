number = int(input("Enter the number: "))
multiplier = int(input("Enter the value of the multiplier: "))

if number % multiplier == 0:
    print(number, "is a multiple of", multiplier)
if number % multiplier != 0:
    print(number, "is not a multiple of", multiplier)
