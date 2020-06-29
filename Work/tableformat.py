# practical python table formatter


class TableFormatter:
    def headings(self, headers):
        "emit the table headings"
        raise NotImplementedError()

    def row(self, rowData):
        "emit a row of data"
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    "emit a table in plain text format"

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    "output portfolio data in csv format"

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    "output portfolio data as html"

    def headings(self, headers):
        inner = "".join([f"<th>{h}</th>" for h in headers])
        print(f"<tr>{inner}</tr>")

    def row(self, rowdata):
        inner = "".join([f"<td>{d}</td>" for d in rowdata])
        print(f"<tr>{inner}</tr>")


def create_formatter(name="text"):
    "create a formatter of type name in html, csv, text"
    if name == "text":
        return TextTableFormatter()
    elif name == "html":
        return HTMLTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    else:
        raise ValueError("Invalid Table Format: " + name)

