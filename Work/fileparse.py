# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as file:
        rows = csv.reader(file, delimiter=delimiter)
        #   read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(name) for name in select]
                headers = select
        # process the rows
        records = []
        for row in rows:
            if not row:  # skip rows with no data
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                row = [type_of(val) for type_of, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records
