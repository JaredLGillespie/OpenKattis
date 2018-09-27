# https://open.kattis.com/problems/boundingrobots


def walk_think(x, y, c, v):
    if c == 'u':
        return x, y + v
    if c == 'r':
        return x + v, y
    if c == 'd':
        return x, y - v
    return x - v, y


def walk_actual(w, l, x, y, c, v):
    x, y = walk_think(x, y, c, v)
    return min(max(0, x), w - 1), min(max(0, y), l - 1)


w, l = map(int, input().split())

while w != 0 and l != 0:
    n = int(input())
    tx, ty, ax, ay = 0, 0, 0, 0
    for _ in range(n):
        c, v = input().split()
        tx, ty = walk_think(tx, ty, c, int(v))
        ax, ay = walk_actual(w, l, ax, ay, c, int(v))

    print('Robot thinks %s %s' % (tx, ty))
    print('Actually at %s %s' % (ax, ay))
    print()

    w, l = map(int, input().split())
