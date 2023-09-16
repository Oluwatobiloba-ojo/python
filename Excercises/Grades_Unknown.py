grade = int(input("Enter a grade, (Enter -1 to quit): "))
total = 0
counter = 0
while grade != -1:
    total += grade
    counter += 1
    grade = int(input("Enter a grade, (Enter -1 to quit):"))
average = total / counter
print(f"""
    ************************************
    The total score is {total}
    The average score is {average}
    the number of score entered {counter:.2f}
    ************************************
    """)