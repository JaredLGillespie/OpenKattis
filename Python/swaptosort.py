# https://open.kattis.com/problems/swaptosort

# NOTE: This problem isn't plausible in Python3, and should be reimplemented in C++ or Java to succeed.


from collections import deque

QUEUE = deque()


def dfs(x):
    visited[x] = id
    QUEUE.append(x)

    while QUEUE:
        x = QUEUE.pop()
        for o in edges[x]:
            if visited[o] == -1:
                visited[o] = id
                QUEUE.append(o)


n, k = map(int, input().split())
edges = [set() for _ in range(n + 1)]
visited = [-1] * (n + 1)
id = 0

for _ in range(k):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

for i in range(1, n // 2 + 1):
    if visited[i] == -1:
        dfs(i)
        id += 1

    if visited[i] != visited[n + 1 - i]:
        print('No')
        break
else:
    print('Yes')


