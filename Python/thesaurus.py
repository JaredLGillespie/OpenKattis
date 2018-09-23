# https://open.kattis.com/problems/thesaurus

from collections import deque


n, m = map(int, input().split())
essay = input().split()
synonyms = {}

for _ in range(m):
    a, b = input().split()

    if a not in synonyms:
        synonyms[a] = set()

    if b not in synonyms:
        synonyms[b] = set()

    synonyms[a].add(b)
    synonyms[b].add(a)


best_mapping = {}

while synonyms:
    k, v = synonyms.popitem()
    synonyms[k] = v

    queue = deque([k])
    visited = {k}
    best = len(k)

    while queue:
        k = queue.pop()
        v = synonyms.pop(k)

        for i in v:
            if i not in visited:
                visited.add(i)
                queue.append(i)

                best = min(best, len(i))

    for i in visited:
        best_mapping[i] = best

count = 0
for w in essay:
    if w in best_mapping:
        count += best_mapping[w]
    else:
        count += len(w)

print(count)
