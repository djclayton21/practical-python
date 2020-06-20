import sys

def portfolio_cost(filename):

    from pathlib import Path

    try:
        path = Path(__file__).parent / filename
    except NameError:
        path = filename

    cost = 0
    with open(path, "rt") as portfolio_file:
        next(portfolio_file)
        for stock in portfolio_file:
            stock_data = stock.split(",")
            try:
                shares = int(stock_data[1])
                price = float(stock_data[2])
                cost += shares * price
            except ValueError:
                print("missing data:", stock)

    return cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print('Total Cost: ', cost)

