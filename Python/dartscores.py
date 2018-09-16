# https://open.kattis.com/problems/dartscores


def score(r):
    if 0 <= r <= 20:
        return 10
    if 20 < r <= 40:
        return 9
    if 40 < r <= 60:
        return 8
    if 60 < r <= 80:
        return 7
    if 80 < r <= 100:
        return 6
    if 100 < r <= 120:
        return 5
    if 120 < r <= 140:
        return 4
    if 140 < r <= 160:
        return 3
    if 160 < r <= 180:
        return 2
    if 180 < r <= 200:
        return 1
    return 0


t = int(input())

for _ in range(t):
    total_score = 0
    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())
        total_score += score((x**2 + y**2)**0.5)
    print(total_score)
