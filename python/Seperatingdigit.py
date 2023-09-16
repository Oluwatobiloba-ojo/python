number_one = int(input("Enter a five digit number: "))
first_digit = number_one // 10000
second_digit = number_one // 1000 % 10
third_digit = number_one // 100 % 10
four_digit = number_one // 10 % 10
fifth_digit = number_one % 10
print(f"{first_digit:> 4} {second_digit:> 4} {third_digit:> 4} {four_digit:> 4} {fifth_digit:> 4}")
