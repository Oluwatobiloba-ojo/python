def triple(numbers):
    lists = []
    for idx, number in enumerate(numbers):
        result = numbers[idx] ** 3
        lists.append(result)
    return lists
