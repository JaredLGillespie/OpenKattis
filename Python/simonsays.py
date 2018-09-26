# https://open.kattis.com/problems/simonsays

n = int(input())

for _ in range(n):
    line = input()
    if line[:10] == 'Simon says':
        print(line[11:])
