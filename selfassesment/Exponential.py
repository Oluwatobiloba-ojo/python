power = 1.0
divide = 1.0
factorial = 1.0
index = 1
number = int(input("Enter the numbers of terms to calculate exponent"))
while index <= number:
    power *= number
    factorial *= index
    divide += power / factorial
    index += 1
print(f"The estimated factorial is {divide}")
