# https://open.kattis.com/problems/gradecurving


import math


def curve_func(x):
    return 10 * math.sqrt(x)


x, ylow, yhigh = map(int, input().split())


ylowi, yhighi = -1, -1

i = 0
while i <= 100000:
    if math.ceil(x) <= yhigh:
        yhighi = i

        if math.ceil(x) >= ylow and ylowi == -1:
            ylowi = i

    if math.ceil(x) > yhigh:
        break

    x = curve_func(x)
    i += 1

if ylowi == -1:
    print('impossible')
elif yhighi == 100000:
    if ylowi == 100000:
        print('inf inf')
    else:
        print('%s inf' % ylowi)
else:
    print('%s %s' % (ylowi, yhighi))
