from statistics import mean

# This method attempts to avoid side numbers and only roll 1 axis (4 numbers)
axes = [[1, 2, 5, 6],
        [1, 3, 4, 6]
        ]

# Note: not all combination of 3 numbers can do this trick!
# Attempt to spin dice from a corner to get only 3 values.
# A dice has 8 corners/options.
spins = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 5],
    [1, 4, 5],
    [2, 4, 6],
    [2, 3, 6],
    [3, 5, 6],
    [4, 5, 6]]

print("Number = average value\nList = combination")

for axis in axes:
    print("%.2f" % mean(axis), axis)

for spin in spins:
    print("%.2f" % mean(spin), spin)
