binary_Digit = int(input("Enter a binary digit: "))
strDigit = str(binary_Digit)
length = len(strDigit)
total = 1
addition = 0
constant = 2
for count in range(1, length):
    total *= 10
value = binary_Digit // total
multiply = constant * value
addition += multiply

total2 = total // 10
numbers = total2
while numbers > 0:
    digit = binary_Digit // numbers % 10
    addition += digit
    addition *= constant
    numbers //= 10
result = addition / 2
print(f"The decimal equivalence of {binary_Digit} is {result}")
