positive = 0
negative = 0
zero = 0

stop_value = int(input("Enter a value you hate the most"))
numbers = int(input("Enter the value you love the most "))

while numbers != stop_value:
    numbers = int(input("Enter a number or the value you hate the most to stop: "))
    if numbers > 0:
        positive = positive + 1
    if numbers < 0:
        negative = negative + 1
    if numbers == 0:
        zero = zero + 1
print("Positive number counted is  ", positive)
print("Negative numbers counted is  ", negative)
print("Zeros input value is  ", zero)