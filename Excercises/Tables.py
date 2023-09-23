# print("number  square    cube")
# for number in range(1, 11):
#     print(f"{number}  {number * number:> 6}  {number * number * number:> 9} ")

count = 1
print("number  square  cube")
while count <= 10:
    print(f"{count} {count * count:> 6} {count * count * count:> 9}")
    count += 1
