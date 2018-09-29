# https://open.kattis.com/problems/judging

n = int(input())
dom_judge = {}
kattis = {}

for _ in range(n):
    line = input()
    if line not in dom_judge:
        dom_judge[line] = 0
    dom_judge[line] += 1

for _ in range(n):
    line = input()
    if line not in kattis:
        kattis[line] = 0
    kattis[line] += 1

max_results = 0
for item in dom_judge:
    if item in kattis:
        max_results += min(dom_judge[item], kattis[item])

print(max_results)
