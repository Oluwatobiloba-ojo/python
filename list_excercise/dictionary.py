def sort(dictionary: dict):
    keys = list(set(dictionary.keys()))
    values = list(set(dictionary.values()))
    dicts = {}
    for i in range(len(keys)):
        dicts.update({keys[i]: values[i]})
    return dicts


dictionary = {2: 4, 1: 1, 3: 9, 4: 16, 5: 25}
print(sort(dictionary))
