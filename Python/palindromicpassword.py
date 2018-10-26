# https://open.kattis.com/problems/palindromicpassword


def gen_possibilities(num):
    poss = []

    x = str(int(num[:3]) + 1)[:3]
    poss.append(x + x[2::-1])

    poss.append(num[:3] + num[2::-1])

    x = int(num[:3]) - 1
    if x > 0:
        x = str(x)[:3]
        poss.append(x + x[2::-1])
    return poss


n = int(input())

for _ in range(n):
    num = input()
    best = num
    best_abs = float('inf')

    for poss in gen_possibilities(num):
        v = abs(int(poss) - int(num))
        if v <= best_abs:
            best_abs = v
            best = poss
    print(best)
