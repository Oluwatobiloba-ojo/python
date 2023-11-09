def even_list(lists):
    even_set = set(lists)
    return list({i for i in even_set if i % 2 == 0})