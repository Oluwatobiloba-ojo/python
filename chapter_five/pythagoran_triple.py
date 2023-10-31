for number in range(1, 50):
    for nums in range(1, 50):
        for numb in range(1, 50):
            if (number ** 2) + (nums ** 2) == (numb ** 2):
                print(f"""{number:> 4}    {nums:> 4}  {numb:>4}""")
