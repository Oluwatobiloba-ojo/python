def even_odd(number):
    if number % 2 == 0:
        result = "It is an even number"
    else:
        result = "It is an odd number"
    return result


userInput = int(input("Enter a number: "))
print(even_odd(userInput))
