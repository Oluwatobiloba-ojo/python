num1 = int(input("Enter first number: "))

num2 = int(input("Enter another input "))

num3 = int(input("Enter the third input: "))

minimum = num3

if num1 < minimum:
    minimum = num1
if num2 < minimum:
    minimum = num2

print("Minimum value is", minimum)


maximum = num2

if num1 > maximum:
    maximum = num1
if num3 > maximum:
    maximum = num3

    print("Maximum is ", maximum)
