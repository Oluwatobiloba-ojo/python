largest = 0
lowest = 0
addition = 0
product = 1
for number in range(3):
    numbers = int(input("Enter a number: "))
    if numbers > largest:
        largest = numbers
        lowest = largest

    elif numbers < lowest:
        lowest = numbers

    addition += numbers
    product *= numbers

print("The sum of the value is ", addition)
print("The product of the value is ", product)
print("The largest number is ", largest)
print("The lowest number is ", lowest)
