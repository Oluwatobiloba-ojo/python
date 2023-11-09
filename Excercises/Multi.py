lists = [[25, 50, 75],
         [40, 50, 60],
         [75, 65, 80]]
totalTotal = []
total = 0
totalAverage = 0
for row, number in enumerate(lists):
    for column, numb in enumerate(number):
        total += numb
    totalTotal.append(total)
print(lists)

for num in totalTotal:
    totalAverage += num

average1 = totalTotal[0] / len(lists[0])
average2 = totalTotal[1] / len(lists[1])
average3 = totalTotal[2] / len(lists[2])
averageTotal = totalAverage / len(lists)

print(f"""
    The average of the first row is {average1:.2f}
    The average of the second row is {average2:.2f}
    The average of the third row is {average3:.2f}
    The total average is {averageTotal:.2f}
    """)
