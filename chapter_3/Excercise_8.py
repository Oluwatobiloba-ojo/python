numbers = input("Enter a number: ")
total = 1
length = len(numbers)
for count in range(1, length, 1):
    total *= 10
first_Value = int(numbers) // total
print(first_Value)
for count in range(1, length, 1):
    pass
