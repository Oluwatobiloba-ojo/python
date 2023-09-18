addition = 0
product = 1
count = 1
numbers = int(input("Enter a number: "))
lowest = numbers
addition += numbers
product *= numbers
largest = numbers
for number2 in range(2):
    count += 1
    number = int(input("Enter a number: "))

    if number > largest:
        largest = number
    else:
        lowest = number

    addition += number
    product *= number

average = addition / count
print("The sum of the value is ", addition)
print("The product of the value is ", product)
print("The largest number is ", largest)
print("The lowest number is ", lowest)
print("The average number is ", average)
