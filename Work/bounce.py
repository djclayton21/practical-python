# bounce.py
#
# Exercise 1.5
i = 1
height = 100
decay = 3 / 5

while i <= 10:
    height = round(height * decay, 4)
    print(i, height)
    i += 1
