# for number in range(1, 51):
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     if number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     if number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#     if number % 5 == 0 or number % 3 == 0:
#         continue
#     print(number)

# for number in range(1, 51):
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     elif number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     elif number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)

count = 1
while count <= 50:
    if count % 3 == 0 and count % 5 != 0:
        print("Fizz")
    elif count % 5 == 0 and count % 3 != 0:
        print("Buzz")
    elif count % 3 == 0 and count % 3 == 0:
        print("FizzBuzz")
    else:
        print(count)
    count += 1
