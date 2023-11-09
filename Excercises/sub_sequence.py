def sub_sequence_of_a_list(list1, list2) -> bool:
    index = 0
    for count in range(len(list1)):
        if index == 3:
            break
        if list1[count] == list2[index]:
            index += 1
    return index == len(list2)
