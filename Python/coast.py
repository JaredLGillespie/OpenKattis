# https://open.kattis.com/problems/coast


from collections import deque


def count_edges(grid, n, m):
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    edges = 0

    while queue:
        spot = queue.popleft()

        for r, c in neighbor_iter(n, m, spot):
            if grid[r][c]:
                edges += 1
            elif not visited[r][c]:
                queue.append((r, c))
                visited[r][c] = 1

    return edges


def neighbor_iter(n, m, spot):
    r, c = spot
    if r - 1 >= 0:
        yield (r - 1, c)
    if r + 1 <= n - 1:
        yield (r + 1, c)
    if c - 1 >= 0:
        yield (r, c - 1)
    if c + 1 <= m - 1:
        yield (r, c + 1)


n, m = map(int, input().split())
grid = [[0] * (m + 2)] + [[0] + list(map(int, input())) + [0] for _ in range(n)] + [[0] * (m + 2)]
print(count_edges(grid, n + 2, m + 2))
