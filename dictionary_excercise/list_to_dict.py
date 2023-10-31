def list_to_dictionary(lists: list[str]):
    dicts = {}
    for value in lists:
        if value[0] in dicts.keys() and value not in dicts.values():
            dicts.update({value[0].upper(): value})
        else:
            dicts.update({value[0]: value})
    return dicts

