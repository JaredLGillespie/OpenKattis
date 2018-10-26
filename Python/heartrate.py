# https://open.kattis.com/problems/heartrate

n = int(input())
for _ in range(n):
    b, p = map(float, input().split())
    print('%.4f %.4f %.4f' % (60 * b / p - 60 / p, 60 * b / p, 60 * b / p + 60 / p))
