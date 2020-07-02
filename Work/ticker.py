from follow import follow
import csv


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def ticker(portfolio_file, logfile, fmt="text"):
    import report
    import tableformat

    formatter = tableformat.create_formatter(fmt)

    portfolio = report.read_portfolio(portfolio_file)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    headers = ["Name", "Price", "Change"]
    formatter.headings(headers)
    for row in rows:
        formatter.row(row)


if __name__ == "__main__":
    ticker("Data/portfolio.csv", "Data/stocklog.csv", "text")

