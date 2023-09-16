number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for count in number:
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even number is ", even)
print("Number of odd number is ", odd)
