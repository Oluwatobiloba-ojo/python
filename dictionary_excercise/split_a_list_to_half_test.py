lists = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
first_list = []
second_list = []
for index in range(len(lists)):
    if index < len(lists)/2:
        first_list.append(lists[index])
    else:
        second_list.append(lists[index])
print(first_list)
print(second_list)
