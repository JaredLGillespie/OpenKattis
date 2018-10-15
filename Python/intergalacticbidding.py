# https://open.kattis.com/problems/intergalacticbidding


def solve(p, s):
    if s == 0:
        return True

    if p < 0:
        return False

    if participants[p][0] * 2 - 1 < s:
        return False

    if s - participants[p][0] < 0:
        return solve(p - 1, s)

    if solve(p - 1, s - participants[p][0]):
        names.append(participants[p][1])
        return True

    return solve(p - 1, s)


n, s = map(int, raw_input().split())
names = []
participants = []
sum_bids = 0

for _ in range(n):
    name, bid = raw_input().split()
    sum_bids += int(bid)
    participants.append((int(bid), name))

participants.sort()

if sum_bids < s:
    print(0)
else:
    solve(n - 1, s)
    print(len(names))
    for name in names:
        print(name)
