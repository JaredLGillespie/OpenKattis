# https://open.kattis.com/contests/ismtgr/problems/bigtruck

import heapq

num_locations = int(input())
item_locations = [0] + list(map(int, input().split()))
num_roads = int(input())
roads = {}
distances = {}


for _ in range(num_roads):
    a, b, d = map(int, input().split())
    if a not in roads:
        roads[a] = list()
    if b not in roads:
        roads[b] = list()

    roads[a].append(b)
    roads[b].append(a)
    distances[(a, b)] = d
    distances[(b, a)] = d

queue = []
heapq.heappush(queue, (0, 0, 1))
shortest_path = [float('inf') for i in range(num_locations + 1)]

while queue:
    distance, items, location = heapq.heappop(queue)
    if distance >= shortest_path[location]:
        continue

    shortest_path[location] = distance
    items -= item_locations[location]

    if location == num_locations:
        print(distance, -items)
        break

    if location not in roads:
        print('impossible')
        break

    for other in roads[location]:
        new_distance = distance + distances[(other, location)]
        if  new_distance <= shortest_path[other]:
            heapq.heappush(queue, (new_distance, items, other))
else:
    print('impossible')

