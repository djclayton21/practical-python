# report.py
#
# Exercise 2.4

from pprint import pprint
import sys


def read_portfolio(filename):
    import csv

    portfolio = []

    with open(filename, "rt") as portfolio_file:
        lines = csv.reader(portfolio_file)
        header = next(lines)
        for i, line in enumerate(lines):
            record = dict(zip(header, line))
            try:
                holding = {}
                holding["symbol"] = record["name"]
                holding["n_shares"] = int(record["shares"])
                holding["purchace_price"] = float(record["price"])
                portfolio.append(holding)
            except ValueError:
                print(f"Could not process line {i}:", line)

    return portfolio


def read_prices(filename):
    import csv

    prices = {}

    with open(filename, "rt") as prices_file:
        lines = csv.reader(prices_file)

        for price in lines:
            if len(price) != 2:
                continue

            prices[price[0]] = float(price[1])

    return prices


def update_portfolio(portfolio, prices):

    result = {"holdings": [], "total_value": 0, "total_p/l": 0}

    for stock in portfolio:
        stock["current_price"] = prices[stock["symbol"]]
        stock["change"] = stock["current_price"] - stock["purchace_price"]
        stock["value"] = stock["n_shares"] * stock["current_price"]
        stock["value"] = round(stock["value"], 2)
        stock["change"] = round(stock["change"], 2)

        result["holdings"].append(stock)
        result["total_value"] += stock["value"]
        result["total_p/l"] += stock["n_shares"] * stock["change"]

    return result


def make_report(portfolio):
    header = "%10s %10s %10s %10s" % ("Symbol", "Shares", "Price", "Change")
    print(header)
    print(len(header) * "-")
    for stock in portfolio["holdings"]:
        line = "%10s %10d %10s %10.2f" % (
            stock["symbol"],
            stock["n_shares"],
            f'${stock["current_price"]:0.2f}',
            stock["change"],
        )
        print(line)


if len(sys.argv) == 3:
    filename = sys.argv[1]
    prices = sys.argv[2]
elif len(sys.argv) == 2:
    filename = sys.argv[1]
    prices = "Data/prices.csv"
else:
    filename = "Data/portfolio.csv"
    prices = "Data/prices.csv"

my_portfolio = read_portfolio(filename)
current_prices = read_prices(prices)

updated_portfolio = update_portfolio(my_portfolio, current_prices)

make_report(updated_portfolio)
