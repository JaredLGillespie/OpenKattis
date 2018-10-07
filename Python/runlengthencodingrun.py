# https://open.kattis.com/problems/runlengthencodingrun


def decode(line):
    message = []
    for i in range(0, len(line), 2):
        c = line[i]
        m = int(line[i + 1])
        message.extend([c] * m)
    return ''.join(message)


def encode(line):
    message = []
    prev_char = ''
    counter = 0
    for c in line:
        if c == prev_char:
            counter += 1
        else:
            if prev_char != '':
                message.append(prev_char)
                message.append(str(counter))
            prev_char = c
            counter = 1

    if prev_char != '':
        message.append(prev_char)
        message.append(str(counter))

    return ''.join(message)


op, line = input().split()
if op == 'D':
    print(decode(line))
else:
    print(encode(line))
