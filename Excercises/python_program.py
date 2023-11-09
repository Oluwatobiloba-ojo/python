import re


def duplicate_first_char(value: str, char: str):
    result = value[0]
    for i in range(1, len(value)):
        if value[i] == value[0]:
            result += char
        else:
            result += value[i]
    return result


print('true' if re.fullmatch(r'\d+[A-Z][a-z]*[A-Z][a-z]*', '45TB') else 'false')
# def duplicate_first_char2(value: str, char: str):
#     dictionary = dict({i: value[i] for i in range(1, len(value)) if value[i] == value[0]})
#     result = '0' * len(value)
#     for i, n in enumerate(result):
#         if i == dictionary.keys():
#     return result
