gradesCounter = 0
total = 0
average = 0
while gradesCounter < 10:
    grade = int(input("Enter the grade "))
    total += grade
    gradesCounter += 1
    print(gradesCounter)
    if grade != 0:
        average = total / gradesCounter
    else:
        print("No score have been entered")

print(f"Average of this score is {average:.2f}")
