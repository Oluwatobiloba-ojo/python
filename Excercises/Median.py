disorganized = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]

# for number in range(0, len(disorganized)):
#     for number2 in range(number + 1, len(disorganized)):
#         if disorganized[number] > disorganized[number2]:
#             disorganized[number], disorganized[number2] = disorganized[number2], disorganized[number]
# print(disorganized)

#
# length = len(disorganized)
# if length % 2 == 0:
#     first_mid = disorganized[length // 2]
#     second_mid = disorganized[(length // 2) - 1]
#     result = (first_mid + second_mid) / 2
#     print(result)
# else:
#     result = disorganized[length // 2]
#     print(result)
#
# add = 0
# average = 0.0
# for number in disorganized:
#     add += number
#     average = add / len(disorganized)
# print(f"The mean of the sum of the list {add} is {average}")

disorganized.sort()
print(disorganized)
