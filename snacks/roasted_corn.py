def update_dictionary(occurrence, store):
    dictionary = dict()
    for i in range(len(occurrence)):
        dictionary.update({store[i]: occurrence[i]})
    return dictionary


def character_frequency(sample: str):
    dictionary = {}
    for i in sample:
        if i not in dictionary.keys():
            dictionary = ({i: sample.count(i)})
    return dictionary


character_frequency("google.com")
