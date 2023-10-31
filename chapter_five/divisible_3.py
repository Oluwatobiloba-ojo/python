def number_divisible():
    lists = {number for number in range(1, 31) if number % 3 == 0}
    return sum(lists)


print(number_divisible())
