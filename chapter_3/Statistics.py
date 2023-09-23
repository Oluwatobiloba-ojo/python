score = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]
for nums in range(0, len(score)):
    for count in range (nums + 1, len(score)):
        if score[nums] > score[count]:
            score[nums], score[count] = score[count], score[nums]
print(score)
length = len(score)

if length % 2 == 0:
    m1 = score[length // 2]
    m2 = score[(length // 2) - 1]
    median = (m1 + m2) / 2
    print(median)
else:
    median = score[length // 2]
    print(median)

product = 0
for index in score:
    product += index
average = product / length
print(average)