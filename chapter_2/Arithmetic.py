number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

sums = number1 + number2 + number3
average = sums / 3
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

    print(f"""
        sum of this is {sums}
        Average of the number is {average}
        product of three number is {product}
        The largest number is {maximum}
        The smallest number is {minimum}
        """)

# refactor to use one print
# use a python file naming convention to name your files
