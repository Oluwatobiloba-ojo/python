def credit_card_type(card_details):
    if len(card_details) == 13 or len(card_details) >= 16:
        first_details = int(card_details[0])
        second_details = int(card_details[1])
        result = ''
        if first_details == 4:
            result = 'Visa cards'
        elif first_details == 5:
            result = 'Master Cards'
        elif first_details == 3 and second_details == 7:
            result = 'American Express Cards'
        elif first_details == 6:
            result = 'Discover Cards'
        else:
            result = 'Invalid'
        return result
    else:
        return "Invalid input"


def validate_credit_cards(numbers):
    first_value = 0
    second_value = 0
    validate = ''
    for number in numbers[0:len(numbers):2]:
        multiply = int(number) * 2
        if multiply >= 10:
            multiply = add(multiply)
        first_value += multiply
    for num in range(1, len(numbers), 2):
        second_value += int(numbers[num])
    total = first_value + second_value
    if total % 10 == 0:
        validate = 'Valid'
    else:
        validate = 'Invalid'
    return validate


def add(number):
    total = 0
    while number != 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

