constant = 7
firstValue = 0
secondValue = 0
thirdValue = 0
fourthValue = 0
encrypted = int(input("Enter an encrypted value: "))
while encrypted > 9999 or encrypted < 0000:
    encrypted = int(input("Enter an encrypted value:"))

# SEPARATION OF THE ENCRYPTED INTO SEPARATE DIGIT
firstDigit = encrypted // 1000
secondDigit = encrypted // 100 % 10
thirdDigit = encrypted // 10 % 10
fourthDigit = encrypted % 10

# VARIABLE SWAP OF THE ENCRYPTED CODE
replicateThird = thirdDigit
thirdDigit = firstDigit
firstDigit = replicateThird
replicateFour = fourthDigit
fourthDigit = secondDigit
secondDigit = replicateFour

# PERFORMING DECRYPTION
if constant - firstDigit > 0:
    firstValue = firstDigit + 10
else:
    firstValue = firstDigit

if constant - secondDigit > 0:
    secondValue = secondDigit + 10
else:
    secondValue = secondDigit

if constant - thirdDigit > 0:
    thirdValue = thirdDigit + 10
else:
    thirdValue = thirdDigit

if constant - fourthDigit > 0:
    fourthValue = fourthDigit + 10
else:
    fourthValue = fourthDigit

firstValue -= 7
secondValue -= 7
thirdValue -= 7
fourthValue -= 7

print(f"{firstValue}{secondValue}{thirdValue}{fourthValue}")
 