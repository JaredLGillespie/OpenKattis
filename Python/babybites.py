# https://open.kattis.com/problems/babybites

n = int(input())
inp = input().split()

for i in range(0, n):
    if inp[i].isdigit():
        if int(inp[i]) != i + 1:
            print('something is fishy')
            break
else:
    print('makes sense')
