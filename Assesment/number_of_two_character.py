def no_of_copy(word, number):
    result = 0
    if len(word) > 2:
        result = word[0] * number + "" + word[1] * number
    else:
        result = word * number
    return result


print(no_of_copy("Ope", 3))
