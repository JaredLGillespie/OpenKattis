# https://open.kattis.com/problems/nineknights


def is_valid(row, col, board):
    for r in [-2, 2]:
        for c in [-1, 1]:
            if board[row + r][col + c] == 'k':
                return False

    for c in [-2, 2]:
        for r in [-1, 1]:
            if board[row + r][col + c] == 'k':
                return False

    return True


def check_board(board):
    knights = 0
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.': continue
            if not is_valid(row, col, board): return 'invalid'
            knights += 1

    return 'valid' if knights == 9 else 'invalid'


board = ['.' * 9] * 2

for _ in range(5):
    board.append('..' + input() + '..')

board.extend(['.' * 9] * 2)

print(check_board(board))
