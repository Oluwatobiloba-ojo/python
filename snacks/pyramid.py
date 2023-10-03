number = 5
for a in range(number):
    print()
    for i in range(a, number):
        print(" ", end=" ")
    for j in range(a+1):
        print("*", end=" ")
    for b in range(a):
        print("*", end=" ")
for b in range(number):
    print()
    for i in range(b + 1):
        print(" ", end=" ")
    for j in range(b+1, number):
        print("*", end=" ")
    for n in range(b, number):
        print("*", end=" ")
