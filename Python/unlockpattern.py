# https://open.kattis.com/problems/unlockpattern


import math


def distance(a, b):
    if a[0] == b[0]:
        return abs(a[1] - b[1])
    if a[1] == b[1]:
        return abs(a[0] - b[0])
    return math.sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2)


m = {}
for row in range(3):
    for col, x in enumerate(map(int, input().split())):
        m[x] = (row, col)

print(sum(distance(m[i], m[i + 1]) for i in range(1, 9)))
