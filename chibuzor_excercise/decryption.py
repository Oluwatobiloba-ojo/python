from chibuzor_excercise.encryption import generate_cipher


def get_decrypt(index):
    plain_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return plain_letter[index]


def decrypt(letter: str, key):
    result = ''
    cipher_key = generate_cipher(key)
    for char in letter.upper():
        for index, value in enumerate(cipher_key):
            if char == value:
                result += get_decrypt(index)
    return result
