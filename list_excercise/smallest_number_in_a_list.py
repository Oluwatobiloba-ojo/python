number_lists = [15, 20, 25, 20, 10, 5]
smallest = number_lists[3]
for nums in number_lists:
    if nums < smallest:
        smallest = nums
print(smallest)