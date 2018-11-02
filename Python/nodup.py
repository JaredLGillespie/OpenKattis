# https://open.kattis.com/problems/nodup

inp = input().split()
print('yes' if len(set(inp)) == len(inp) else 'no')
