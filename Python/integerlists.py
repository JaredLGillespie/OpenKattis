# https://open.kattis.com/problems/integerlists

from collections import deque


def process(p, n, l):
    if sum(1 for c in p if c == 'D') > n:
        return 'error'

    d = deque(l)
    is_rev = False

    for c in p:
        if c == 'R':
            is_rev = not is_rev
        elif is_rev:
            d.pop()
        else:
            d.popleft()

    a = []
    if is_rev:
        while d:
            a.append(d.pop())
    else:
        while d:
            a.append(d.popleft())
    return '[' + ','.join(a) + ']'


t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    l = input()[1:-1].split(',')

    print(process(p, n, l))
