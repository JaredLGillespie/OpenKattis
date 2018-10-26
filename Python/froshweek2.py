# https://open.kattis.com/problems/froshweek2

n, m = map(int, input().split())
tasks = sorted(list(map(int, input().split())), reverse=True)
quiets = sorted(list(map(int, input().split())), reverse=True)

completed_tasks = 0
task_index = 0
for quiet in quiets:
    if task_index >= n:
        break

    while task_index < n and tasks[task_index] > quiet:
        task_index += 1

    if task_index >= n:
        break

    if tasks[task_index] <= quiet:
        completed_tasks += 1
        task_index += 1

print(completed_tasks)
