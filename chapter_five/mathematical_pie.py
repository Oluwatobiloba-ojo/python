count = 1
total = 0.0
constant = 4
number = 1
num = int(input("Enter the terms of exponential: "))
for number in range(1, num, 2):
    count += 1
    if count % 2 == 0:
        total += (constant / number)
    else:
        negative = -1
        total += negative * constant / number
print(f"{total:.5f}")
