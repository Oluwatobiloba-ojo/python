def element_greater_than_k(lists: list, k):
    list1 = {value for value in lists if lists.count(value) > k}
    return list(list1)
