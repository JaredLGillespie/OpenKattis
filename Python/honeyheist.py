# https://open.kattis.com/problems/honeyheist


from collections import deque


def construct_honey_comb(r):
    s = r**3 - (r - 1)**3
    edges = {i: set() for i in range(1, s + 1)}
    num_rows = 2 * r

    cell_index = 0
    for row in range(1, num_rows):
        num_cells = row + r - 1
        prev_num_cells = num_cells - 1
        next_num_cells = num_cells + 1
        if row > r: num_cells = num_rows - row + r - 1
        if row > r: prev_num_cells = num_cells + 1
        if row >= r: next_num_cells = num_cells - 1

        start_index = cell_index + 1
        end_index = cell_index + num_cells

        for cell_index in range(start_index, end_index + 1):
            # left
            if cell_index > start_index: edges[cell_index].add(cell_index - 1)

            # right
            if cell_index < end_index: edges[cell_index].add(cell_index + 1)

            # top left
            if row > r: edges[cell_index].add(cell_index - prev_num_cells)
            if 1 < row < r + 1 and cell_index > start_index: edges[cell_index].add(cell_index - num_cells)

            # top right
            if row > r: edges[cell_index].add(cell_index - num_cells)
            if 1 < row < r + 1 and cell_index < end_index: edges[cell_index].add(cell_index - prev_num_cells)

            # bottom left
            if row < r: edges[cell_index].add(cell_index + num_cells)
            if r - 1 < row < num_rows - 1 and cell_index > start_index: edges[cell_index].add(cell_index + next_num_cells)

            # bottom right
            if row < r: edges[cell_index].add(cell_index + next_num_cells)
            if r - 1 < row < num_rows - 1 and cell_index < end_index: edges[cell_index].add(cell_index + num_cells)

    return edges


def solve(edges, wax_hardened, a, b, n, r):
    s = r**3 - (r - 1)**3
    visited = [False] * (s + 1)

    for cell in wax_hardened:
        visited[cell] = True

    visited[a] = True
    queue = deque([(0, a)])

    while queue:
        dist, cell = queue.popleft()

        if cell == b: return dist
        if dist > n: return -1

        for o in edges[cell]:
            if visited[o]: continue
            visited[o] = True
            queue.append((dist + 1, o))

    return -1


r, n, a, b, x = map(int, input().split())
wax_hardened = list(map(int, input().split()))
edges = construct_honey_comb(r)
ans = solve(edges, wax_hardened, a, b, n, r)

if ans > -1 and ans <= n:
    print(ans)
else:
    print('No')
