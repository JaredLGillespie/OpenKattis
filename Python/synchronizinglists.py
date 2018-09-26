# https://open.kattis.com/problems/synchronizinglists

n = int(input())

while n != 0:
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(n)]
    m = dict(zip(sorted(a), sorted(b)))

    for x in a:
        print(m[x])

    n = int(input())

    if n != 0:
        print()


