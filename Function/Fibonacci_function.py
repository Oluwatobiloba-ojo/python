def fibonacci(number: int):
    first = 0
    second = 1
    sums = first + second
    while first <= number:
        print(first, end=" ")
        first = second
        second = sums
        sums = first + second


fibonacci(30)