number_lists = [15, 20, 25, 20, 10, 5]
for i in number_lists:
    for j in range(i + 1, len(number_lists)):
        if number_lists[i] == number_lists[j]:
            number_lists[j].append(0)
print(number_lists)
