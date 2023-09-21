number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

sum = number1 + number2 + number3
average = sum / 3
product = number2 * number3 * number1

minimum = number3

if number1 < minimum:
    minimum = number1
if number2 < minimum:
    minimum = number2

maximum = number1
if number2 > maximum:
    maximum = number2
if number3 > maximum:
    maximum = number3

    print("sum of the number is ", sum)
    print("Average of the numbers are", average)
    print("Product of the numbers are", product)
    print("Minimum value is ", minimum)
    print("Maximum value is ", maximum)

# refactor to use one print
# use a python file naming convention to name your files
