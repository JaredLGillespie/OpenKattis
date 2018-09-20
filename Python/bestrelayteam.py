# https://open.kattis.com/problems/bestrelayteam


n = int(input())
a_map, b_map = {}, {}

for _ in range(n):
    runner, a, b = input().split()
    a, b = float(a), float(b)
    a_map[runner] = a
    b_map[runner] = b

sorted_a = list(sorted(a_map.items(), key=lambda x: x[1])[0:4])
sorted_b = list(sorted(b_map.items(), key=lambda x: x[1])[0:4])

best_team = None
best_time = float('inf')

for i in range(4):
    a = sorted_a[i]
    bs = []
    for j in range(4):
        b = sorted_b[j]
        if b[0] != a[0]:
            bs.append(b)
        if len(bs) == 3:
            break
    time = a[1] + bs[0][1] + bs[1][1] + bs[2][1]
    if time < best_time:
        best_time = time
        best_team = [a] + bs

print(best_time)
for p in best_team:
    print(p[0])
