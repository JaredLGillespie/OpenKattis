# https://open.kattis.com/problems/goatrope


def dist(x1, y1, x2, y2):
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)


def solve():
    if x1 <= x <= x2:
        if y < y1: return y1 - y
        return y - y2

    if y1 <= y <= y2:
        if x < x1: return x1 - x
        return x - x2

    if x < x1:
        if y < y1: return dist(x, y, x1, y1)
        return dist(x, y, x1, y2)

    if y < y1: return dist(x, y, x2, y1)
    return dist(x, y, x2, y2)


x, y, x1, y1, x2, y2 = map(int, input().split())
print(solve())
