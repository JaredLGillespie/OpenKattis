# https://open.kattis.com/problems/t9spelling

key_map = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
}

n = int(input())

for t in range(n):
    m = input()
    d = []

    for i in range(len(m)):
        if i > 0 and key_map[m[i - 1]][-1] == key_map[m[i]][-1]:
            d.append(' ')

        d.append(key_map[m[i]])

    print('Case #%s: %s' % (t + 1, ''.join(d)))
