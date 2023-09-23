def palindrome(number: int):
    return str(number) == str(number)[::-1]


print(palindrome(131))
