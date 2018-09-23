# https://open.kattis.com/problems/maximumrent

a, b = map(int, input().split())
m, s = map(int, input().split())

if a > b:
    x = m - 1
    y = 1
else:
    l, r = 0, m - 1

    while l <= r:
        y = (l + r) // 2
        x = m - y
        if 2 * x + y < s:
            r = y - 1
        else:
            l = y + 1

    y = r
    x = m - y

print(a * x + b * y)
