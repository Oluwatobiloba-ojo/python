def my_sort_function(lists: list, reverse=False):
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if reverse:
                if lists[i] < lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
            else:
                if lists[i] > lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
    return lists


print(my_sort_function([30, 50, 80, 6, 5, 4, 3], reverse=False))
