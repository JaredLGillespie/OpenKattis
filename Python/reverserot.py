# https://open.kattis.com/problems/reverserot

from string import ascii_uppercase
m = dict(zip(ascii_uppercase, range(26)))
m['_'] = 26
m['.'] = 27
mr = {v: k for k, v in m.items()}

line = input()

while line[0] != '0':
    n, message = line.split()
    n = int(n)
    encrypted = []
    for c in reversed(message):
        encrypted.append(mr[(m[c] + n) % 28])
    print(''.join(encrypted))
    line = input()
