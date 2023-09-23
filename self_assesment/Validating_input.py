passes = 0
fail = 0
gradeCounter = 0
while gradeCounter < 10:
    score = int(input("Enter 1 to pass, 2 to fail: "))
    while score != 1 and score != 2:
        score = int(input("Enter 1 to pass, 2 to fail: "))
    if score == 1:
        passes += 1
    else:
        fail += 1
    gradeCounter += 1
print("The amount of student who passes is ", passes)
print("The amount of student who fail", fail)
