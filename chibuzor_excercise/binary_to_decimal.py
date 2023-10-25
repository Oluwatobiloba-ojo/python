def binary_to_decimal(number):
    lists_of_number = str(number)
    base_power = 2
    third_digit = int(lists_of_number[len(lists_of_number) - 1]) * 1
    result = 0 + third_digit
    count = len(lists_of_number) - 1
    for value in range(len(lists_of_number) - 1):
        result = result + int(lists_of_number[value]) * (base_power ** count)
        count -= 1
    return result
