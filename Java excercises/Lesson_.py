name = "Tobi is a boy"

for count in range (2,10,2):
    print(count)

for letter in name:
    print(letter, end= "")

print()

count = 1
for count in range (5,len(name)):
    if name.count("4", len(name)):
        print(name.__getitem__(count),end="")
   # print(name.__getitem__(count), end= "")