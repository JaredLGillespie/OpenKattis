# https://open.kattis.com/problems/cold

n = int(input())
temps = map(int, input().split())
print(sum(1 for t in temps if t < 0))
