import os
import sys
import time


def follow(filename):
    with open(filename) as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line == "":
                time.sleep(0.1)
                continue
            yield line


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        filename = args[1]
    else:
        print("you need a filename silly head: ", end="")
        filename = input()
    for line in follow(filename):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")

