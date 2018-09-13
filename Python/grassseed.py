# https://open.kattis.com/problems/grassseed

c = float(input())
l = int(input())
t = 0

for _ in range(l):
    a, b = map(float, input().split())
    t += a * b

print(t * c)
