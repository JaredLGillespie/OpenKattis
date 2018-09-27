# https://open.kattis.com/problems/baconeggsandspam

n = int(input())

while n != 0:
    m = {}
    for _ in range(n):
        name, *items = input().split()
        for item in items:
            if item not in m:
                m[item] = []
            m[item].append(name)

    for item, people in sorted(m.items()):
        print('%s %s' % (item, ' '.join(sorted(people))))

    print()
    n = int(input())
