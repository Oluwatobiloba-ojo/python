def display(lists: list):
    for index, count in enumerate(lists):
        print(index, end='\t')
        for counter in count:
            print(counter, end="\t")
        print()


display([[3, 4, 5, 6], [7, 9, 10, 67]])
