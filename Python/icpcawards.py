# https://open.kattis.com/problems/icpcawards

n = int(input())
unis = set()
count = 0

for _ in range(n):
    uni, team = input().split()
    if count == 12 or uni in unis:
        continue

    print('%s %s' % (uni, team))
    unis.add(uni)
    count += 1
