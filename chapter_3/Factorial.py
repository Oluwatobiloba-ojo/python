number = int(input("Enter a number: "))
total = 1
while number > 1:
    total *= number
    number -= 1
print(total)