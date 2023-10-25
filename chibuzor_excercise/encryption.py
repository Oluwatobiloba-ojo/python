def function_shift(cipher_list, key, character):
    begin = len(cipher_list) - key
    for index in range(key):
        cipher_list[index] = character[begin]
        begin += 1
    return cipher_list


def generate_cipher(key):
    character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cipher_list = [0 for i in range(len(character))]
    count = key
    for index in range(len(character) - key):
        cipher_list[count] = character[index]
        count += 1
    return function_shift(cipher_list, key, character)


def get_encrypt(index, key):
    cipher = generate_cipher(key)
    return cipher[index]


def encrypt(key, plain: str):
    chars = ''
    character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for char in plain.upper():
        for index, value in enumerate(character):
            if char == value:
                chars += get_encrypt(index, key)
    return chars
