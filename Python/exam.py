# https://open.kattis.com/problems/exam

k = int(input())
a = input()
b = input()
t = len(a)
ns = sum(1 for i in range(t) if a[i] != b[i])
s = t - ns

if s >= k:
    print(ns + k)
else:
    print(s + (ns - (k - s)))
