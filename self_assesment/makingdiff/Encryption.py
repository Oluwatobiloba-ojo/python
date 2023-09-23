replicateFirst = 0
replicateSecond = 0
encrypted_Value = int(input("Enter a four digit you wished to encrypt: "))

while encrypted_Value < 1111 or encrypted_Value > 9999:
    encrypted_Value = int(input("Enter a four digit you wished to encrypt: "))


firstDigit = encrypted_Value // 1000
secondDigit = encrypted_Value // 100 % 10
thirdDigit = encrypted_Value // 10 % 10
fourDigit = encrypted_Value % 10

firstDigit += 7
secondDigit += 7
thirdDigit += 7
fourDigit += 7
firstDigit %= 10
secondDigit %= 10
thirdDigit %= 10
fourDigit %= 10

replicateFirst = firstDigit
firstDigit = thirdDigit
thirdDigit = replicateFirst
replicateSecond = secondDigit
secondDigit = fourDigit
fourDigit = replicateSecond

first = str(firstDigit)
second = str(secondDigit)
third = str(thirdDigit)
four = str(fourDigit)

realDigit = int(first + second + third + four)
print(f"The encrypted values of {encrypted_Value} is {realDigit}")
