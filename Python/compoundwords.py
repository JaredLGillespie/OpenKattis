# https://open.kattis.com/problems/compoundwords

import sys

words = []
for line in sys.stdin:
    words.extend(line.split())

out = set()
for i in range(0, len(words) - 1):
    for j in range(i + 1, len(words)):
        out.add(words[i] + words[j])
        out.add(words[j] + words[i])

for i in sorted(out):
    print(i)
