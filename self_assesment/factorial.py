number = int(input("Enter a number: "))
result = 1
while number > 1:
    print(number, end="*")
    result *= number
    if number == 2:
        print("1", end=" = ")
    number -= 1
print(result)
