def count_character(value: str) -> dict:
    result: dict = dict()
    for letter in value:
        result[letter] = value.count(letter)
    return result
