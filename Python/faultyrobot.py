# https://open.kattis.com/problems/faultyrobot


def solve(edges, resting_nodes, visited):
    dfs(edges, resting_nodes, visited, 1, False)


def dfs(edges, resting_nodes, visited, node, used_buggy_move):
    if visited[node]: return

    visited[node] = True

    if edges[node]['forced']:
        dfs(edges, resting_nodes, visited, edges[node]['forced'], used_buggy_move)
    else:
        resting_nodes.add(node)

    if not used_buggy_move:
        for other in edges[node]['unforced']:
            dfs(edges, resting_nodes, visited, other, True)

    visited[node] = False


n, m = map(int, input().split())
edges = {(x + 1): {'forced': None, 'unforced': set()} for x in range(n)}
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    if a < 0:
        edges[abs(a)]['forced'] = b
    else:
        edges[a]['unforced'].add(b)

resting_nodes = set()


solve(edges, resting_nodes, visited)

print(len(resting_nodes))
