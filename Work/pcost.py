# pcost.py
#
# Exercise 1.27

path = "Data/portfolio.csv"
cost = 0


with open(path, "rt") as portfolio:
    next(portfolio)
    for stock in portfolio:
        deets = stock.split(",")
        shares = int(deets[1])
        price = float(deets[2])
        cost += shares * price

print(f"Total cost is ${cost:.2f}")
