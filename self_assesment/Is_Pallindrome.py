def is_palindrome(number):
    temp_Number = number
    reverse = 0
    while number != 0:
        value = number % 10
        reverse = reverse * 10 + value
        number //= 10
    return temp_Number == reverse


# print(is_palindrome(-1112111))
