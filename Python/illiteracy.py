# https://open.kattis.com/problems/illiteracy


from collections import deque

NUM_ICONS = 8
NUM_UNIQUE_ICONS = 6
ROTATIONS = list('ABCDEF')
ROTATIONS_INV = {ROTATIONS[i]: i for i in range(NUM_UNIQUE_ICONS)}


def rotate(c):
    return ROTATIONS[(ROTATIONS_INV[c] + 1) % NUM_UNIQUE_ICONS]


def click(s, i):
    t = s[i]
    if t == 'A':
        if i == 0: return s[0] + rotate(s[1]) + s[2:]
        if i == 7: return s[:6] + rotate(s[6]) + s[7]
        return s[:i - 1] + rotate(s[i - 1]) + s[i] + rotate(s[i + 1]) + s[i + 2:]
    if t == 'B':
        if i in (0, 7): return s
        return s[:i + 1] + s[i - 1] + s[i + 2:]
    if t == 'C':
        p = 7 - i
        return s[:p] + rotate(s[p]) + s[p + 1:]
    if t == 'D':
        if i in (0, 7): return s
        if i < 4: return ''.join(rotate(s[x]) for x in range(i)) + s[i:]
        return s[:i + 1] + ''.join(rotate(s[x]) for x in range(i + 1, 8))
    if t == 'E':
        if i in (0, 7): return s
        if i < 4: y = i
        else: y = 7 - i
        p1, p2 = i - y, i + y
        return s[:p1] + rotate(s[p1]) + s[p1 + 1:p2] + rotate(s[p2]) + s[p2 + 1:]
    if t == 'F':
        i += 1
        p = (i + 9) // 2 if i & 1 else i // 2
        p -= 1
        return s[:p] + rotate(s[p]) + s[p + 1:]


def bfs(initial, target):
    visited = {initial}
    queue = deque([(0, initial)])

    while queue:
        level, s = queue.popleft()

        if s == target: return level

        for i in range(NUM_ICONS):
            ns = click(s, i)
            if ns in visited: continue
            if ns == target: return level + 1
            visited.add(ns)
            queue.append((level + 1, ns))

    return -1


print(bfs(raw_input(), raw_input()))
