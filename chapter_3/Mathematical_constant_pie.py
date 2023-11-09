constant = 4
count = 1
total = 0.00
number = 1
num = int(input("Enter terms of the exponential terms: "))
for number in range(1, num, 2):
    count += 1
    if count % 2 == 0:
        total += (constant / number)
    else:
        negative = -1
        total += negative * constant / number
print(f"{total:.5f}")
