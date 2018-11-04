# https://open.kattis.com/problems/pokerhand

cards = input().split()
freq = {}
max_rank = 0

for card in cards:
    r, _ = card
    if r not in freq:
        freq[r] = 0
    freq[r] += 1
    max_rank = max(max_rank, freq[r])

print(max_rank)
