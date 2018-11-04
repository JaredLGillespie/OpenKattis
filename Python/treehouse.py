# https://open.kattis.com/problems/treehouses


def find(parent, i):
    if parent[i] == i: return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] +=1


def kruskal(parent, rank, connections, num_to_connect):
    i, e, ws = 0, 0, 0

    connections.sort(key=lambda x: x[2])

    while e < num_to_connect:
        u, v, w = connections[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            ws += pow(w, 0.5)
            union(parent, rank, x, y)

    return ws


def get_sq_dist(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


def create_connections(n, t):
    return [(i, j, get_sq_dist(t[i], t[j]))
            for i in range(n)
            for j in range(n)]


def connect_e_treehouses(n, e, parent, rank):
    for x in range(e):
        parent[x] = n
    rank[n] = e


def connect_existing(p, parent, rank):
    connected = 0
    for _ in range(p):
        u, v = map(lambda x: int(x) - 1, input().split())
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            connected += 1
            union(parent, rank, x, y)

    return connected


n, e, p = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)

treehouses = [tuple(map(float, input().split())) for _ in range(n)]
connections = create_connections(n, treehouses)
connect_e_treehouses(n, e, parent, rank)
num_to_connect = n - e - connect_existing(p, parent, rank)
weight_sum = kruskal(parent, rank, connections, num_to_connect)
print(weight_sum)



