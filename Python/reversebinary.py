# https://open.kattis.com/problems/reversebinary

print(int(''.join(reversed('{0:b}'.format(int(input())))), 2))
