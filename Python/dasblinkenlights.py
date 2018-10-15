# https://open.kattis.com/problems/dasblinkenlights

p, q, s = map(int, input().split())

for t in range(1, s + 1):
    if t % p == 0 and t % q == 0:
        print('yes')
        break
else:
    print('no')
