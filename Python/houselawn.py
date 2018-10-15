# https://open.kattis.com/problems/houselawn

l, m = map(int, input().split())
names = []
lowest_price = float('inf')

for _ in range(m):
    line = input().split(',')
    n = line[0]
    p, c, t, r = map(int, line[1:])

    if t / (t + r) * c * 10080 >= l:
        if p < lowest_price:
            names.clear()
            names.append(n)
            lowest_price = p
        elif p == lowest_price:
            names.append(n)

if len(names) == 0:
    print('no such mower')
else:
    for name in names:
        print(name)
