from chibuzor_snacks.student_grade_function import display_subject, position, \
    display_subject_summary, class_summary, display_class_summary

average = 0
total = 0
totalTotal = []
averageTotal = []
student = int(input("Enter the number of student:\n"))
subject = int(input("Enter the number of subject:\n "))
studentPosition = []
lists_of_subject_passes = [1 for passes in range(subject)]
lists_of_subject_failure = [1 for failure in range(subject)]
student_lists = [[0 for i in range(subject)] for col in range(student)]

for i, numb in enumerate(student_lists):
    for j, value in enumerate(numb):
        score = int(input(f"Enter the score for Student {i + 1} Subject {j + 1}\n"))
        student_lists[i][j] = score
        total += student_lists[i][j]
        print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    totalTotal.append(total)
    averageTotal.append(total / len(student_lists[i]))
    total = 0
studentPosition = (position(totalTotal))

display_subject(subject)
for index, value in enumerate(student_lists):
    print(f"STUDENT {index + 1} ", end="\t")
    for idx, value2 in enumerate(value):
        print(student_lists[index][idx], end="\t\t")
    print(f"{totalTotal[index]}      {averageTotal[index]:.2f}      {studentPosition[index]}")
print("========================================================")

print("SUBJECT SUMMARY", end="\n")
result = display_subject_summary(subject, student, student_lists)
lists_of_subject_passes = result[0]
lists_of_subject_failure = result[1]
result_of_class_summary = class_summary(student_lists, lists_of_subject_failure, lists_of_subject_passes, subject,
                                        totalTotal)
display_class_summary(result_of_class_summary, totalTotal)
