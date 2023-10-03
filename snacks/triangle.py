number = 5
for a in range(number):
    print()
    for i in range(a + 1):
        print("*", end=" ")
    for j in range(a, number):
        print(" ", end=" ")
for b in range(number):
    print()
    for n in range(b + 1, number):
        print("*", end=" ")
