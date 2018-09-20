# https://open.kattis.com/problems/cups

n = int(input())
cups = []

for _ in range(n):
    a, b = input().split()
    if a.isnumeric():
        color = b
        radius = int(a) / 2
    else:
        color = a
        radius = int(b)
    cups.append((radius, color))

for cup in sorted(cups):
    print(cup[1])
