def isPalindrome(inputs: str):
    string: str = ''
    lists: list = list(inputs)
    inputs = inputs.upper()
    for count in range(len(inputs), 0, -1):
        string += lists.pop(count-1)
    string = string.upper()
    return inputs == string
