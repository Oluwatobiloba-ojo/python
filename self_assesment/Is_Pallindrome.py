def is_palindrome(number):
    temp_Number = number
    reverse = 0
    while number != 0:
        value = number % 10
        reverse = reverse * 10 + value
        number //= 10
    if temp_Number == reverse:
        return True
    else:
        return False


print(is_palindrome(1112111))
