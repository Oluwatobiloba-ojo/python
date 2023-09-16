count = 0
passes = 0
failure = 0
for count in range(10):
    result = int(input("Enter the grade (1 for passes, 2 for failed)"))
    if result == 1:
        passes += 1
    elif result == 2:
        failure += 1
    else:
        print ("Enter 1= passes, 2 = failures: ")
print("Passes is ", passes)
print("failure is ", failure)

if passes > 8:
    print("Bonus to instructor")