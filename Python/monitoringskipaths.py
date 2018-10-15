# https://open.kattis.com/problems/monitoringskipaths

from collections import deque


def mark_depths(paths, depths, parent):
    for i in range(len(paths)):
        if parent[i] == -1:
            mark_path_depth(paths, depths, i)


def mark_path_depth(paths, depths, junction):
    queue = deque([(0, junction)])

    while queue:
        depth, junc = queue.pop()

        for o in paths[junc]:
            depths[o] = depth + 1
            queue.append((depth + 1, o))


def traverse(start, stop, parent, paths, marked_junctions):
    node = stop
    last_junction = start
    if node in marked_junctions:
        return

    while node != start:
        node = parent[node]
        if node in marked_junctions:
            return
        if len(paths[node]) > 1:
            last_junction = node

    marked_junctions.add(last_junction)


n, k, m = map(int, input().split())
paths = [set() for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]
marked_junctions = set()
depths = [0 for _ in range(n + 1)]

for _ in range(k):
    u, v = map(int, input().split())
    paths[u].add(v)
    parent[v] = u

ski_paths = [tuple(map(int, input().split())) for _ in range(m)]

mark_depths(paths, depths, parent)
ski_paths.sort(key=lambda x: (-depths[x[0]], depths[x[1]]))

for start, stop in ski_paths:
    traverse(start, stop, parent, paths, marked_junctions)

print(len(marked_junctions))
