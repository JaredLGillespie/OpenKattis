# https://open.kattis.com/problems/batterup


n = int(input())
b = list(map(int, input().split()))
bases = sum(x for x in b if x >= 0)
bats = sum(1 for x in b if x >= 0)
print(bases / bats)
