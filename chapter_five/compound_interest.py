principal = 1000
for year in range(1, 11):
    for rate in range(5, 11):
        rate /= 100
        amount = principal * ((rate + 1.0) ** year)
        print(f"{year} {amount:.2f}", end="\t\t")
    print()
