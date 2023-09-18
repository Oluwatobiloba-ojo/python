# palindrome
# 12221 is a palindrome

# palindrome = input("Enter a four digit number")
# if the number > 999 and less than or equal 9999
def is_palindrome(number):
    if 999 < number <= 9999:
        temp_number = number
        reverse = 0
        while number != 0:
            reverse = reverse * 10 + (number % 10)
            number //= 10
        return reverse == temp_number
    else:
        return False
