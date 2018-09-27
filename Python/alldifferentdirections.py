# https://open.kattis.com/problems/alldifferentdirections


import math


def process_directions(x, y, direction, moves):
    for i in range(0, len(moves), 2):
        instruction = moves[i]
        value = float(moves[i + 1])

        if instruction == 'turn':
            direction = (direction + value) % 360
        else:  # walk
            x += math.cos(math.radians(direction)) * value
            y += math.sin(math.radians(direction)) * value

    return x, y


def average_points(points, n):
    avg_x, avg_y = 0, 0

    for x, y in points:
        avg_x += x
        avg_y += y

    return avg_x / n, avg_y / n


def worst_direction_distance(avg_x, avg_y, points):
    worst_sq_dist = -float('inf')

    for x, y in points:
        worst_sq_dist = max(worst_sq_dist, sq_distance(avg_x, avg_y, x, y))

    return worst_sq_dist**0.5


def sq_distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


n = int(input())

while n != 0:
    points = []
    for _ in range(n):
        x, y, _, start_direction, *moves = input().split()
        points.append(process_directions(float(x), float(y), float(start_direction), moves))

    avg_x, avg_y = average_points(points, n)
    worst_direction_dist = worst_direction_distance(avg_x, avg_y, points)

    print('%s %s %s' % (avg_x, avg_y, worst_direction_dist))

    n = int(input())
