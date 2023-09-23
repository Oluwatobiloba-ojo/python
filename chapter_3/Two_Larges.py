count = 0
largest = 0
largest2 = 0
while count < 10:
    numbers = int(input("Enter a number: "))
    if numbers > largest:
        largest2 = largest
        largest = numbers
    elif largest2 < numbers:
        largest2 = numbers
    count += 1
print(f"The largest number is {largest}")
print(f"The second largest number is {largest2}")
