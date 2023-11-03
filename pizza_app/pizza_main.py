def pizza_box_size_slices(size: str):
    boxes_slice = {"BIG": 10, "MEDIUM": 6, "SMALL": 4}
    if size.upper() in boxes_slice.keys():
        return boxes_slice[size.upper()]
    else:
        return 0


def calculate_number_of_slices(super_hungry_human, hungry_human, classic_human):
    if super_hungry_human >= 0 and hungry_human >= 0 and classic_human >= 0:
        return (super_hungry_human * 4) + (hungry_human * 2) + (classic_human * 1)
    else:
        return 0


def calculate_number_of_boxes(super_h_human, hungry_human, classic_human, size):
    box = 0
    value_of_size = pizza_box_size_slices(size)
    sum_up_the_humans = calculate_number_of_slices(super_h_human, hungry_human, classic_human)
    while sum_up_the_humans >= value_of_size:
        sum_up_the_humans -= value_of_size
        box += 1
    if sum_up_the_humans < value_of_size and sum_up_the_humans != 0:
        box += 1
    return box


def calculate_excess_slices(super_human, hungry_human, classic_human, size):
    value_of_size = pizza_box_size_slices(size)
    number_of_box = calculate_number_of_boxes(super_human, hungry_human, classic_human, size)
    sum_up_the_human = calculate_number_of_slices(super_human, hungry_human, classic_human)
    return (number_of_box * value_of_size) - sum_up_the_human


def calculate_total_of_pizza(super_human, hungry_human, classic_human, size: str):
    size_cost = {"BIG": 5000, "MEDIUM": 3000, "SMALL": 1200}
    number_of_box = calculate_number_of_boxes(super_human, hungry_human, classic_human, size)
    return size_cost[size.upper()] * number_of_box
