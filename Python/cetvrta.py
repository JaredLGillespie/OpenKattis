# https://open.kattis.com/problems/cetvrta


def f(a, b, c):
    if a == b:
        return c
    if a == c:
        return b
    return a


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(f(x1, x2, x3), f(y1, y2, y3))
