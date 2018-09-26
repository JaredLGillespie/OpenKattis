# https://open.kattis.com/problems/splat


import math

c = int(input())

for _ in range(c):
    p = []
    n = int(input())

    for _ in range(n):
        x, y, v, color = input().split()
        x, y, v = float(x), float(y), float(v)
        p.append((x, y, v / math.pi, color))

    m = int(input())

    for _ in range(m):
        x1, y1 = map(float, input().split())
        for i in range(n - 1, -1, -1):
            x2, y2, r2, color = p[i]
            if (x2 - x1)**2 + (y2 - y1)**2 <= r2:
                print(color)
                break
        else:
            print('white')
