# https://open.kattis.com/problems/battlesimulation

m = input()
o = []

i = 0
while i < len(m):
    if i + 2 < len(m) and len(set(m[i:i+3])) == 3:
        o.append('C')
        i += 3
        continue
    elif m[i] == 'R':
        o.append('S')
    elif m[i] == 'B':
        o.append('K')
    elif m[i] == 'L':
        o.append('H')
    i += 1

print(''.join(o))
