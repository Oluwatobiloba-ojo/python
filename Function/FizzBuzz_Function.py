def fizz_buzz(number: int):
    count = 1
    while count <= number:
        if count % 3 == 0 and count % 5 != 0:
            print("Fizz")
        elif count % 5 == 0 and count % 3 != 0:
            print("Buzz")
        elif count % 5 == 0 and count % 3 == 0:
            print("FizzBuzz")
        else:
            print(count)
        count += 1


fizz_buzz(10)