passes = 0
failure = 0
for count in range(10):
    result = int(input("Enter the grade (1 for passes, 2 for failed)"))
    while result != 1 and result != 2:
        result = int(input("Enter the grade for 1 for passes and 2 for failed"))
    if result == 1:
        passes += 1
    else:
        failure += 1
print("Passes is ", passes)
print("failure is ", failure)

if passes > 8:
    print("Bonus to instructor")