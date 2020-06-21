import sys


def portfolio_cost(filename):

    from pathlib import Path
    import csv

    try:
        path = Path(__file__).parent / filename
    except NameError:
        path = filename

    cost = 0
    with open(path, "rt") as portfolio_file:

        lines = csv.reader(portfolio_file)
        headers = next(lines)
        for i, stock in enumerate(lines):
            record = dict(zip(headers, stock))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                cost += shares * price
            except ValueError:
                print(f"could not process line {i}:", stock)

    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)

print("Total Cost: ", cost)

