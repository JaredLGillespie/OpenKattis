# https://open.kattis.com/problems/nine

t = int(input())

for _ in range(t):
    d = int(input())

    x = 9
    r = 1
    y = d - 1
    while y > 0:
        if y & 1:
            r *= x
        y = y // 2
        x = ((x % 1000000007) * (x % 1000000007)) % 1000000007

    print((8 * r % 1000000007) % 1000000007)
