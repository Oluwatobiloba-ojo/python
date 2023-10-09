def reverse(numbers: tuple):
    reverses = ()
    for numbered in range(len(numbers) - 1, 0, -1):
        reverses += numbers[numbered],
    reverses += numbers[0],
    return reverses


def check_element(value: tuple):
    values = 0
    second_value = 0
    i = 0
    indices = value[len(value) - 1][2]
    for number in value:
        for index in number:
            if index == value[1][1]:
                values = (index, indices)
    for i in range(0, len(values) - 1):
        second_value = values[i]
    for idx, nums in enumerate(values):
        values = ((i, second_value), (idx, nums))
    return values


def unpack(tuple3):
    first_digit = tuple3[0]
    last_digit = tuple3[len(tuple3) - 1]
    tuple_value = (last_digit, first_digit)
    return tuple_value


def swap_indices_element(tuple4):
    x, y, v, z = tuple4
    swap = v, x, z, y
    return swap


def duplicate(tuple5):
    tuple1 = ()
    for nums in range(0, len(tuple5)):
        for number in range(nums + 1, len(tuple5)):
            if tuple5[nums] == tuple5[number]:
                if tuple5[nums] is not tuple1:
                    tuple1 += tuple5[nums],
    return tuple
