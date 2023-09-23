def arrange_list(disorganized: list):
    for count in range(0, len(disorganized)):
        for number in range(count + 1, len(disorganized)):
            if disorganized[count] > disorganized[number]:
                disorganized[count], disorganized[number] = disorganized[number], disorganized[count]
    return disorganized


lists = [10, 20, 42, 25, 5, 30, 35, 40, 10, 20]

print(arrange_list(lists))
