# https://open.kattis.com/problems/tetris

c, p = map(int, input().split())
cols = list(map(int, input().split()))
s = 0

if p == 1:
    s += c
    s += sum(1 for i in range(3, c) if cols[i - 3] == cols[i - 2] == cols[i - 1] == cols[i])
elif p == 2:
    s += sum(1 for i in range(1, c) if cols[i - 1] == cols[i])
elif p == 3:
    s += sum(1 for i in range(2, c) if cols[i - 2] + 1 == cols[i - 1] + 1 == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] == cols[i] + 1)
elif p == 4:
    s += sum(1 for i in range(2, c) if cols[i - 2] == cols[i - 1] + 1 == cols[i] + 1)
    s += sum(1 for i in range(1, c) if cols[i - 1] + 1 == cols[i])
elif p == 5:
    s += sum(1 for i in range(2, c) if cols[i - 2] == cols[i - 1] == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] + 1 == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] == cols[i] + 1)
    s += sum(1 for i in range(2, c) if cols[i - 2] == cols[i - 1] + 1 == cols[i])
elif p == 6:
    s += sum(1 for i in range(2, c) if cols[i - 2] == cols[i - 1] == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] == cols[i] + 2)
    s += sum(1 for i in range(2, c) if cols[i - 2] + 1 == cols[i - 1] == cols[i])
else:
    s += sum(1 for i in range(2, c) if cols[i - 2] == cols[i - 1] == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] == cols[i])
    s += sum(1 for i in range(1, c) if cols[i - 1] + 2 == cols[i])
    s += sum(1 for i in range(2, c) if cols[i - 2] == cols[i - 1] == cols[i] + 1)

print(s)
