number = 1
add = 0
index = number + add
for count in range(1, 49):
    print(f"{add}", end=" ")
    add = number
    number = index
    index = add + number
    if add >= 50:
        break

while add < 50:
    print(f"{add}", end=" ")
    add = number
    number = index
    index = add + number
