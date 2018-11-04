# https://open.kattis.com/problems/heirsdilemma

L, H = map(int, input().split())
count = 0
for v in range(L, H + 1):
    for c in str(v):
        if c == '0': break
        if v % int(c) != 0: break
    else:
        if len(set(str(v))) == 6:
            count += 1

print(count)
