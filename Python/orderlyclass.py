# https://open.kattis.com/problems/orderlyclass


def solve(A, B):
    if len(A) != len(B): return 0
    i, j = 0, len(A) - 1

    while i < j:
        if A[i] == B[i]: i += 1
        elif A[j] == B[j]: j -= 1
        else: break

    for k in range(j - i + 1):
        if A[i + k] != B[j - k]: return 0

    i -= 1
    j += 1

    num_ways = 1
    while i >= 0 and j < len(B):
        if A[i] == B[j]:
            num_ways += 1
            i -= 1
            j += 1
        else:
            break

    return num_ways


print(solve(input(), input()))
