current_population = 8045311447
growth_rate = 0.088
total = 0
for year in range(1, 76):
    total = current_population * (1 + growth_rate) ** year
    difference = total - current_population
    print(f"""
        {year}   {current_population}   {difference:.3f} """)
