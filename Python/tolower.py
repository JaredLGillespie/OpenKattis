# https://open.kattis.com/problems/tolower

p, t = map(int, input().split())
nums = [input()[1:] for _ in range(p * t)]
solved = 0

for i in range(p):
    for j in range(t):
        if not nums[i * t + j].islower():
            break
    else:
        solved += 1

print(solved)
