# https://open.kattis.com/problems/flipfive

from collections import deque


def flip(grid, v):
    if v == 0:
        grid ^= 1 << 0
        grid ^= 1 << 1
        grid ^= 1 << 3
    elif v == 1:
        grid ^= 1 << 0
        grid ^= 1 << 1
        grid ^= 1 << 2
        grid ^= 1 << 4
    elif v == 2:
        grid ^= 1 << 1
        grid ^= 1 << 2
        grid ^= 1 << 5
    elif v == 3:
        grid ^= 1 << 0
        grid ^= 1 << 3
        grid ^= 1 << 4
        grid ^= 1 << 6
    elif v == 4:
        grid ^= 1 << 1
        grid ^= 1 << 3
        grid ^= 1 << 4
        grid ^= 1 << 5
        grid ^= 1 << 7
    elif v == 5:
        grid ^= 1 << 2
        grid ^= 1 << 4
        grid ^= 1 << 5
        grid ^= 1 << 8
    elif v == 6:
        grid ^= 1 << 3
        grid ^= 1 << 6
        grid ^= 1 << 7
    elif v == 7:
        grid ^= 1 << 4
        grid ^= 1 << 6
        grid ^= 1 << 7
        grid ^= 1 << 8
    else:
        grid ^= 1 << 5
        grid ^= 1 << 7
        grid ^= 1 << 8

    return grid


def flip_five(grid):
    if grid == 0:
        return 0

    queue = deque([(0, grid)])
    visited = {grid}

    while queue:
        flips, grid = queue.popleft()
        for i in range(9):
            new_grid = flip(grid, i)

            if new_grid == 0:
                return flips + 1

            queue.append((flips + 1, new_grid))
            visited.add(new_grid)

    return -1


def create_grid():
    x = 0
    c = []
    for i in range(3):
        c.extend(input())

    for i in range(9):
        if c[i] == '*':
            x |= (1 << i)

    return x


p = int(input())

for _ in range(p):
    grid = create_grid()
    print(flip_five(grid))
