# https://open.kattis.com/problems/squarepegs

n, m, k = map(int, input().split())
plots = list(map(int, input().split()))
circular_houses = list(map(float, input().split()))
square_houses = list(map(float, input().split()))

houses = circular_houses
houses.extend(pow(2 * pow(i, 2), 0.5) / 2 for i in square_houses)
houses.sort(reverse=True)
plots.sort(reverse=True)

plots_filled = 0
house_index = 0
for plot_index in range(n):
    while house_index < m + k and houses[house_index] >= plots[plot_index]:
        house_index += 1

    if house_index >= m + k:
        break

    plots_filled += 1
    house_index += 1

print(plots_filled)
