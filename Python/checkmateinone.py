# https://open.kattis.com/problems/checkmateinone


n = 8


def can_checkmate_in_one_move(K, R, k):
    for Rf in valid_rook_moves(K, R, k):
        if is_checkmate(K, Rf, k):
            return True

    for Kf in valid_king_moves(K, R, k):
        if is_checkmate(Kf, R, k):
            return True

    return False


def is_valid_move(p):
    return (0 <= p[0] <= n - 1 and
            0 <= p[1] <= n - 1)


def valid_opponent_moves(K, R, k):
    def yield_check(K, R, k):
        if k == K:
            return None, R, k
        elif k == R:
            return K, None, k
        else:
            return K, R, k

    for i in range(-1, 2):
        for j in range(-1, 2):
            v = (k[0] + i, k[1] + j)
            if is_valid_move(v):
                yield yield_check(K, R, v)


def valid_king_moves(K, R, k):
    for i in range(-1, 2):
        for j in range(-1, 2):
            v = (K[0] + i, K[1] + j)
            if is_valid_move(v) and v != R and not is_threatened(v, k):
                yield v


def valid_rook_moves(K, R, k):
    lb, rb = 0, n
    if K[1] == R[1]:
        if K[0] < R[0]:
            lb = K[0] + 1
        else:
            rb = K[0]

    for i in range(lb, rb):
        if i == R[0]:
            continue

        yield (i, R[1])

    lb, rb = 0, n
    if K[0] == R[0]:
        if K[1] < R[1]:
            lb = K[0] + 1
        else:
            rb = K[0]

    for i in range(lb, rb):
        if i == R[1]:
            continue

        yield (R[0], i)


def is_checkmate(K, R, k):
    if not is_opponent_threatened(K, R, k):
        return False

    for K, R, k in valid_opponent_moves(K, R, k):
        if K is None or not is_opponent_threatened(K, R, k):
            return False

    return True


def is_threatened(K, k):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (k[0] + i, k[1] + j) == K:
                return True
    return False


def is_opponent_threatened(K, R, k):
    if K is not None:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (K[0] + i, K[1] + j) == k:
                    return True

    if R is not None:
        if R[0] == k[0]:
            if K[0] != R[0]:
                return True

            if k[0] < R[0] and (K[0] < k[0] or K[0] > R[0]):
                return True

            if k[0] > R[0] and (K[0] < R[0] or K[0] > k[0]):
                return True

        if R[1] == k[1]:
            if K[1] != R[1]:
                return True

            if k[1] < R[1] and (K[1] < k[1] or K[1] > R[1]):
                return True

            if k[1] > R[1] and (K[1] < R[1] or K[1] > k[1]):
                return True
    return False


K, R, k = None, None, None

for row in range(8):
    line = input()
    for col in range(8):
        if line[col] == 'K':
            K = (row, col)
        elif line[col] == 'k':
            k = (row, col)
        elif line[col] == 'R':
            R = (row, col)


print('Yes' if can_checkmate_in_one_move(K, R, k) else 'No')
