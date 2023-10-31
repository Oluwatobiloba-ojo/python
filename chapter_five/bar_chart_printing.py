def display_asteriks(numbers):
    for number in numbers:
        for shape in range(number):
            print("*", end=" ")
        print()


lists = []
for num in range(5):
    nums = int(input("Enter the number to display"))
    lists.append(nums)

display_asteriks(lists)
