# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    file,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a file or iterable of comma separated values into a list of records
    """

    rows = csv.reader(file, delimiter=delimiter)
    #   read the file headers

    if has_headers:
        headers = next(rows)
    if select:
        if not has_headers:
            raise RuntimeError("No headers, cannot use select")
        indices = [headers.index(name) for name in select]
        headers = select
    # process the rows
    records = []
    for i, row in enumerate(rows):
        if not row:  # skip rows with no data
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [type_of(val) for type_of, val in zip(types, row)]
            except ValueError as err:
                if not silence_errors:
                    print(f"Row {i}: Could not convert {row}")
                    print(f"Row {i}: {err}")
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records
