# https://open.kattis.com/problems/sumoftheothers

import sys


for line in sys.stdin:
    arr = list(map(int, line.split()))
    n = len(arr)
    counts = [0] * n

    s = 0
    for i in range(n):
        counts[i] += s
        s += arr[i]

    s = 0
    for i in range(n - 1, -1, -1):
        counts[i] += s
        s += arr[i]

    for i in range(n):
        if arr[i] == counts[i]:
            print(arr[i])
            break
