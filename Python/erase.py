# https://open.kattis.com/problems/erase

n = int(input())
a = input()
b = input()

for i in range(len(a)):
    if n % 2 == 1:
        if a[i] == b[i]:
            print('Deletion failed')
            break
    else:
        if a[i] != b[i]:
            print('Deletion failed')
            break
else:
    print('Deletion succeeded')
