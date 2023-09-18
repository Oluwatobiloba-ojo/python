count = 0
while count <= 6:
    if count % 3 != 0 or count == 0:
        print(count, end=" ")
    count = count + 1


for count in range(0, 6, 1):
    if count % 3 != 0 or count == 0:
        print(count, end=" ")