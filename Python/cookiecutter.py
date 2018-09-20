# https://open.kattis.com/problems/cookiecutter


def area(n, points):
    area = 0
    j = n - 1

    for i in range(n):
        area += (points[j][0] + points[i][0]) * (points[j][1] - points[i][1])
        j = i

    return abs(area / 2)


def centers(points):
    x_max, x_min, y_max, y_min = -float('inf'), float('inf'), -float('inf'), float('inf')

    for point in points:
        x_min = min(x_min, point[0])
        x_max = max(x_max, point[0])
        y_min = min(y_min, point[1])
        y_max = max(y_max, point[1])

    return (x_min + x_max) / 2, (y_min + y_max) / 2


def offsets(points):
    x_min, y_min = float('inf'), float('inf')

    for point in points:
        x_min = min(x_min, point[0])
        y_min = min(y_min, point[1])

    return -x_min, -y_min


n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]
desired_area = int(input())
curr_area = area(n, points)
x_center, y_center = centers(points)
scale = (desired_area / curr_area) ** 0.5

for i in range(n):
    x, y = points[i]
    new_x = scale * (x - x_center) + x_center
    new_y = scale * (y - y_center) + y_center
    points[i] = (new_x, new_y)

x_offset, y_offset = offsets(points)

for i in range(n):
    x, y = points[i]
    new_x = x + x_offset
    new_y = y + y_offset
    points[i] = (new_x, new_y)

for point in points:
    print('%f %f' % (point[0], point[1]))
