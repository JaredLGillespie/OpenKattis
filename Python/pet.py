# https://open.kattis.com/problems/pet

largest = 0
index = 1
for i in range(5):
    s = sum(map(int, input().split()))
    if s > largest:
        largest = s
        index = i + 1

print('%s %s' % (index, largest))
