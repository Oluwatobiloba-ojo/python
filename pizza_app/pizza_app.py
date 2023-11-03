from pizza_main import *
print("""
    =============================
    WELCOME TO PIZZA TALENTED APP
    =============================
    """)
box_size = input("Enter the box size you desired: ")
while pizza_box_size_slices(box_size) == 0:
    box_size = input("Enter a valid box size within big, medium and small: ")
super_hungry = int(input("Enter the number of super hungry people: "))
hungry = int(input("Enter the number of hungry people: "))
classic = int(input("Enter the number of classic people: "))

print(f"""
    Number Of Slices is: {calculate_number_of_slices(super_hungry, hungry, classic)}
    Number Of Boxes Needed is: {calculate_number_of_boxes(super_hungry, hungry,classic, box_size)}
    Number of slices left is: {calculate_excess_slices(super_hungry, hungry, classic, box_size)}
    Total cost is: {calculate_total_of_pizza(super_hungry, hungry, classic, box_size)}
    """)
