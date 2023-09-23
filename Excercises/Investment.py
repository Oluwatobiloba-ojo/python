# year = 1
# capital_investment = int(input("Enter the amount you want to invest"))
# while year <= 30:
#     profit = capital_investment
#     profit *= 10 / 100
#     capital_investment += profit
#     print(f"""Your ROI is ${profit:.2f} and your investment for year{year} is ${capital_investment:.2f}
#                 """)
#     year += 1

capital_investment = int(input("Enter the amount you want to invest: "))
for year in range(1, 31):
    profit = capital_investment
    profit *= 0.1
    capital_investment += profit
    print(f"Your ROI is ${profit:.2f} and your investment for year{year} is ${capital_investment:.2f}")
