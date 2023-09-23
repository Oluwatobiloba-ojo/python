largest = 0
for count in range (10):
    number = int(input("Enter a number: "))
    if number > largest:
        largest = number
print(f"The largest number is {largest}")