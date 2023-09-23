from Function.custom_sort import arrange_list


def custom_median(lists: list):
    total = arrange_list(lists)
    length = len(lists)
    if length % 2 == 0:
        first_value = total[(length // 2)]
        second_value = total[(length // 2) - 1]
        result = (first_value + second_value) / 2
        return result
    else:
        return total[length // 2]


def custom_mean(lists: list):
    sums = 0
    for count in lists:
        sums += count
    return sums / len(lists)


number = [10, 20, 42, 25, 5, 30, 35, 40, 10, 20]

# print(custom_median(number))
print(custom_mean(number))
