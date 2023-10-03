def largest(number):
    maximum = 0
    for nums in number:
        if nums > maximum:
            maximum = nums
    return maximum


def reverse(number):
    lists = []
    for num in number[::-1]:
        lists.append(num)
    return lists


def check_element(number, element):
    for num in number:
        if element == num:
            return True


def odd_position(number):
    lists = []
    for num in number[1::2]:
        lists.append(num)
    return lists


def even_position(number):
    lists = []
    for num in number[0::2]:
        lists.append(num)
    return lists


def running_total(number):
    total = 0
    for num in number:
        total += num
    return total


def is_palindrome(name):
    return name == name[::-1]


def sum_for_loop(number):
    total = 0
    for nums in number:
        total += nums
    return total


def sum_while_loop(number):
    total = 0
    num = 0
    while num < len(number):
        total += number[num]
        num += 1
    return total


def concatenate_lists(numbers: list, characters: list, ) -> list:
    lists = []
    for nums in characters:
        lists.append(nums)
    for value in numbers:
        lists.append(value)
    return lists


def combines_two_list(numbers, collection):
    lists = []
    first = 0
    for number in numbers:
        lists.append(number)
        if first < len(collection):
            lists.append(collection[first])
            first += 1
    if len(collection) > len(numbers):
        while first < len(collection):
            lists.append(collection[first])
            first += 1
    return lists


def convert_to_list(number: int) -> list:
    lists = []
    count = len(str(number))
    while number != 0:
        n = number % 10
        lists.append(n)
        number //= 10
        count -= 1
    value = reverse(lists)
    return value

