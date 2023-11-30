def isValids(value: str):
    list_of_parentheses = ['(', ')', '{', '}', '[', ']']
    list_for_value = list(value)
    for index, bracket in enumerate(list_for_value):
        if bracket in list_of_parentheses:
            index_in_list = list_of_parentheses.index(bracket) + 1
            value_in_list = list_of_parentheses[index_in_list]
            if value_in_list in list_for_value:
                values = list_for_value.index(value_in_list)
                list_for_value.remove(list_for_value[values])
            else:
                return False
        else:
            return False
    return True


