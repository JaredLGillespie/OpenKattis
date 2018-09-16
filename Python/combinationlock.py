# https://open.kattis.com/contests/akxgwd/problems/combinationlock

a, b, c, d = map(int, input().split())

while not (a == b == c == d == 0):
    t = 120
    t += (40 + a - b) % 40
    t += (40 + c - b) % 40
    t += (40 + c - d) % 40

    print(t * 9)
    a, b, c, d = map(int, input().split())
