# https://open.kattis.com/problems/luhnchecksum

for _ in range(int(input())):
    count = 0
    for i, d in enumerate(reversed(input())):
        if i % 2 == 0:
            count += int(d)
            continue
        x = 2 * int(d)
        if x < 10:
            count += x
        else:
            x = str(x)
            count += int(x[0]) + int(x[1])
    print('PASS' if count % 10 == 0 else 'FAIL')
