# https://open.kattis.com/problems/judgingmoose

l, r = map(int, input().split())
if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print('Even %s' % (l + r))
else:
    print('Odd %s' % (max(l, r) * 2))
