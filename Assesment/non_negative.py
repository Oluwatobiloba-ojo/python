string = input("Enter a string value: ")
number = int(input("Enter number of copies: "))
result = string * number
print(result)


def time_of_copy(word, num):
    return word * num


print(time_of_copy("joy", 5))
