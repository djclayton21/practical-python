# report.py
#
# Exercise 2.4


def read_portfolio(filename):
    import csv

    portfolio = []

    with open(filename, "rt") as portfolio_file:
        lines = csv.reader(portfolio_file)
        header = next(lines)
        for entries in lines:
            name = entries[0]
            nShares = int(entries[1])
            sharePrice = float(entries[2])

            portfolio.append((name, nShares, sharePrice))
    return portfolio

