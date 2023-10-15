for number in range(1, 50):
    for nums in range(1, 50):
        for numz in range(1, 50):
            if (number ** 2) + (nums ** 2) == (numz ** 2):
                print(f"""{number:> 4}    {nums:> 4}  {numz:>4}""")
