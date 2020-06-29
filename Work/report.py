#!/usr/bin/env python3.8
# report.py
#
# Exercise 2.4

from pprint import pprint
import sys
from fileparse import parse_csv


def update_portfolio(portfolio, prices):

    result = {"holdings": [], "total_value": 0, "total_p/l": 0}

    for stock in portfolio:
        stock["current_price"] = prices[stock["name"]]
        stock["change"] = stock["current_price"] - stock["price"]
        stock["value"] = stock["shares"] * stock["current_price"]
        stock["value"] = round(stock["value"], 2)
        stock["change"] = round(stock["change"], 2)

        result["holdings"].append(stock)
        result["total_value"] += stock["value"]
        result["total_p/l"] += stock["shares"] * stock["change"]

    return result


def make_report(portfolio):
    """
    print a report from a portfolio including keys name, shares,
    current_price, and change
    """
    header = "%10s %10s %10s %10s" % ("name", "Shares", "Price", "Change")
    print(header)
    print(len(header) * "-")
    for stock in portfolio["holdings"]:
        line = "%10s %10d %10s %10.2f" % (
            stock["name"],
            stock["shares"],
            f'${stock["current_price"]:0.2f}',
            stock["change"],
        )
        print(line)


def portfolio_report(
    portfolio_filename="Data/portfolio.csv", prices_filename="Data/prices.csv"
):
    "print a report on your portfolio from current prices"
    with open(portfolio_filename) as file:
        portfolio = parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float]
        )
    with open(prices_filename) as prices:
        current_prices = dict(parse_csv(prices, has_headers=False, types=[str, float]))

    current_portfolio = update_portfolio(portfolio, current_prices)
    make_report(current_portfolio)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        portfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
        portfolio_report(portfolio_filename, prices_filename)
    else:
        portfolio_report()
