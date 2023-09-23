for count in range(1, 13):
    for multiply in range(1, 21):
        print(f"{multiply:>2}  *  {count:>2} = {multiply * count:^3}  ", end=" ")
    print()
