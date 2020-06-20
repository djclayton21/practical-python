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
            holding = {}
            holding["name"] = entries[0]
            holding["nShares"] = int(entries[1])
            holding["sharePrice"] = float(entries[2])

            portfolio.append(holding)

    return portfolio

