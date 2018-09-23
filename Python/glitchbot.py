# https://open.kattis.com/problems/glitchbot

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
directions = [0, 1, 2, 3]


def check_instructions(position, destination, instructions, num_instructions, start_index, current_direction):
    if start_index >= num_instructions:
        return position == destination

    for i in range(start_index, num_instructions):
        instruction = instructions[i]

        if instruction == 'Forward':
            position = move_direction(current_direction, position)
        else:
            current_direction = change_direction(current_direction, instruction)

    return position == destination


def print_correction(i, instruction):
    print('%s %s' % (i, instruction))


def move_direction(current_direction, position):
    if current_direction == UP:
        return position[0], position[1] - 1
    if current_direction == RIGHT:
        return position[0] + 1, position[1]
    if current_direction == DOWN:
        return position[0], position[1] + 1
    if current_direction == LEFT:
        return position[0] - 1, position[1]


def change_direction(current_direction, movement):
    if movement == 'Left':
        return (current_direction + 1) % 4
    return (current_direction - 1) % 4


start = (0, 0)
start_direction = DOWN
destination = tuple(map(int, input().split()))
num_instructions = int(input())
instructions = list(input() for _ in range(num_instructions))

for i in range(num_instructions):
    instruction = instructions[i]

    if instruction != 'Forward':
        if check_instructions(move_direction(start_direction, start), destination, instructions, num_instructions, i + 1, start_direction):
            print_correction(i + 1, 'Forward')
            break

    if instruction != 'Right':
        if check_instructions(start, destination, instructions, num_instructions, i + 1, change_direction(start_direction, 'Right')):
            print_correction(i + 1, 'Right')
            break

    if instruction != 'Left':
        if check_instructions(start, destination, instructions, num_instructions, i + 1, change_direction(start_direction, 'Left')):
            print_correction(i + 1, 'Left')
            break

    if instruction == 'Forward':
        start = move_direction(start_direction, start)
    elif instruction == 'Left':
        start_direction = change_direction(start_direction, 'Left')
    elif instruction == 'Right':
        start_direction = change_direction(start_direction, 'Right')
