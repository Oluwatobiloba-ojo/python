value = int(input("Enter five digit integers: "))
while value < 11111 or value > 99999:
    value = int(input("Enter five digit integers: "))

firstDigit = value // 10000
secondDigit = value // 1000 % 10
thirdDigit = value // 100 % 10
fourDigit = value // 10 % 10
lastDigit = value % 10

firstValue = str(firstDigit)
secondValue = str(secondDigit)
thirdValue = str(thirdDigit)
fourValue = str(fourDigit)
lastValue = str(lastDigit)
replicate = lastValue + fourValue + thirdValue + secondValue + firstValue
value2 = int(replicate)
if value == value2:
    print("its a palindrome ")
else:
    print("Its not a palindrome ")
