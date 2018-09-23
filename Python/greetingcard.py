# https://open.kattis.com/problems/greetingcard

n = int(input())
points = {tuple(map(int, input().split())) for _ in range(n)}
neighbor_distances = {(0, 2018),
                      (1118, 1680),
                      (1680, 1118),
                      (2018, 0),
                      (1118, -1680),
                      (1680, -1118),
                      (0, -2018),
                      (-1118, -1680),
                      (-1680, -1118),
                      (-2018, 0),
                      (-1118, 1680),
                      (-1680, 1118)}
pairs = 0
for point in points:
    for nd in neighbor_distances:
        if (point[0] + nd[0], point[1] + nd[1]) in points:
            pairs += 1

print(pairs // 2)
