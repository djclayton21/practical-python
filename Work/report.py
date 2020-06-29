#!/usr/bin/env python3.8
# report.py
#
# Exercise 2.4

from pprint import pprint
import sys
from fileparse import parse_csv
from stock import Stock
import tableformat


def print_report(portfolio, prices, formatter):
    """
    print a report from a portfolio of Stock objects
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for stock in portfolio:
        lineData = [
            stock.name,
            str(stock.shares),
            f"${prices[stock.name]:0.2f}",
            f"{(prices[stock.name] - stock.price):0.2f}",
        ]
        formatter.row(lineData)


def portfolio_report(
    portfolio_filename="Data/portfolio.csv",
    prices_filename="Data/prices.csv",
    fmt="text",
):
    "print a report on your portfolio with current prices"
    with open(portfolio_filename) as file:
        portfolio_dicts = parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = [Stock(s["name"], s["shares"], s["price"]) for s in portfolio_dicts]

    with open(prices_filename) as prices:
        prices = dict(parse_csv(prices, has_headers=False, types=[str, float]))
    formatter = tableformat.create_formatter(fmt)
    print_report(portfolio, prices, formatter)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        portfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
        fmt = "text"
        if sys.argv[3]:
            fmt = sys.argv[3]
        portfolio_report(portfolio_filename, prices_filename, fmt)
    else:
        portfolio_report()
