# https://open.kattis.com/problems/rectanglesurrounding

MAX_SIZE = 501
ONES = 2**MAX_SIZE - 1


def fill_grid(grid, x1, y1, x2, y2):
    f = (2**(x2 - x1) - 1 << (MAX_SIZE - x2))
    for i in range(y1, y2):
        grid[i] |= f


def count_area(grid):
    c = 0
    for i in range(MAX_SIZE):
        while grid[i]:
            c += (grid[i] >> 1) & 1
            grid[i] >>= 1
    return c


n = int(input())

while n != 0:
    grid = [0] * MAX_SIZE
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        fill_grid(grid, x1, y1, x2, y2)

    print(count_area(grid))
    n = int(input())
