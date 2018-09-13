# https://open.kattis.com/problems/zamka

l = int(input())
d = int(input())
x = int(input())

print(min([i for i in range(l, d + 1) if sum(map(int, str(i))) == x]))
print(max([i for i in range(l, d + 1) if sum(map(int, str(i))) == x]))
