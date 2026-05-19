# USACO 2025 February Contest, Bronze
# Problem 1. Reflection
# https://usaco.org/index.php?page=viewproblem2&cpid=1491
# don't use counter!!!

n, u = map(int, input().split())

canvas = []
updates = []

for _ in range(n):
    canvas.append(list(input()))

for _ in range(u):
    updates.append(list(map(int, input().split())))

def get_num(x1, x2, x3, x4):
    x = 0
    num = 0

    if x1 == '#':
        x += 1
    if x2 == '#':
        x += 1
    if x3 == '#':
        x += 1
    if x4 == '#':
        x += 1

    if x == 1 or x == 3:
        num = 1
    elif x == 2:
        num = 2

    return num

def switch(s):
    return '.' if s == '#' else '#'

cur_num = 0
for i in range(n // 2):
    for j in range(n // 2):
        cur_num += get_num(canvas[i][j], canvas[i][n - 1 - j], canvas[n - 1 - i][j], canvas[n - 1 - i][n - 1 - j])

print(cur_num)

for c, d in updates:
    a = c - 1
    b = d - 1
    num_1 = get_num(canvas[a][b], canvas[a][n - 1 - b], canvas[n - 1 - a][b], canvas[n - 1 - a][n - 1 - b])
    canvas[a][b] = switch(canvas[a][b])
    num_2 = get_num(canvas[a][b], canvas[a][n - 1 - b], canvas[n - 1 - a][b], canvas[n - 1 - a][n - 1 - b])

    cur_num += (num_2 - num_1)

    print(cur_num)

