data = input("Enter a number with commas: ")
data_list = []

for character in data:
    if character.isnumeric():
        data_list.append(character)
data_to_tuple = tuple(data_list)
print(data_list)
print(data_to_tuple)
