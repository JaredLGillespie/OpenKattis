# https://open.kattis.com/problems/flowfree


def find_color_positions(board):
    colors = {}
    squares_to_visit = 0

    for row in range(4):
        for col in range(4):
            v = board[row][col]
            if v == 'W':
                squares_to_visit += 1
                continue

            if v not in colors:
                colors[v] = {}

            if 'start' not in colors[v]:
                colors[v]['start'] = (row, col)
            else:
                colors[v]['stop'] = (row, col)
    return colors, squares_to_visit


def gen_neighbors(position, start, board, color_char):
    row, col = position
    if row > 0 and board[row - 1][col] in ('W', color_char):
        v = (row - 1, col)
        if v != start: yield v
    if row < 3 and board[row + 1][col] in ('W', color_char):
        v = (row + 1, col)
        if v != start: yield v
    if col > 0 and board[row][col - 1] in ('W', color_char):
        v = (row, col - 1)
        if v != start: yield v
    if col < 3 and board[row][col + 1] in ('W', color_char):
        v = (row, col + 1)
        if v != start: yield v


def solve(color, position, color_positions, board, squares_to_visit):
    if color == 4 or (color == 3 and 'Y' not in color_positions):
        return squares_to_visit == 0

    color_char = COLOR_SEARCH_ORDER[color]
    color_position = color_positions[color_char]
    start = color_position['start']
    stop = color_position['stop']

    if position is None:
        position = start

    for neighbor in gen_neighbors(position, start, board, color_char):
        if neighbor == stop:
            if solve(color + 1, None, color_positions, board, squares_to_visit):
                return True
            continue

        row, col = neighbor
        board[row][col] = 'X'

        if solve(color, neighbor, color_positions, board, squares_to_visit - 1):
            return True

        board[row][col] = 'W'

    return False


board = [list(input()) for _ in range(4)]
color_positions, squares_to_visit = find_color_positions(board)
COLOR_SEARCH_ORDER = ['B', 'R', 'G', 'Y']
print('solvable' if solve(0, None, color_positions, board, squares_to_visit) else 'not solvable')
