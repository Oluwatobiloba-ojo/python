def element_to_the_end(numbers: list, element):
    none_of_element = 0
    element_no = len(numbers) - 1
    while none_of_element < element_no:
        while none_of_element < element_no and numbers[element_no] == element:
            element_no -= 1
        if numbers[none_of_element] != element_no:
            numbers[none_of_element], numbers[element_no] = numbers[element_no], numbers[none_of_element]
        none_of_element += 1
    return numbers
