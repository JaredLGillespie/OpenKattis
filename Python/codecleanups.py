# https://open.kattis.com/problems/codecleanups

n = int(input())
dirty_pushes = list(map(int, input().split())) + [366]
next_push = 0

cleanup_phases = 0

dirty_accum = 0
num_dirties = 0

for day in range(1, 366):
    if day == dirty_pushes[next_push]:
        next_push += 1
        dirty_accum += 1

    num_dirties += dirty_accum

    if num_dirties >= 20:
        cleanup_phases += 1
        num_dirties = 0
        dirty_accum = 0

if num_dirties > 0:
    cleanup_phases += 1

print(cleanup_phases)
