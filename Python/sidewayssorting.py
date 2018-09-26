# https://open.kattis.com/problems/sidewayssorting

r, c = map(int, input().split())

while r != 0 and c != 0:
    x = [input() for _ in range(r)]
    x = list(sorted(zip(*x), key=lambda x: ''.join(x).lower()))
    x = list(zip(*x))
    for v in x:
        print(''.join(v))
    r, c = map(int, input().split())
