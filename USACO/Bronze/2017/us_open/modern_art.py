import sys
# sys.stdin = open('art.in', 'r')
# sys.stdout = open('art.out', 'w')

n = int(input())
colors = set()
paint = []
possible = set()
boundary = [((0, 0), (0, 0))]

for _ in range(n):
    s = input()
    for c in s:
        colors.add(c)
    paint.append(list(s))

colors.discard('0')

from itertools import permutations
per = permutations(colors, len(colors))

def get_boundary(m):
    i1 = j1 = n - 1
    i2 = j2 = 0

    for x in range(n):
        for y in range(n):
            if paint[x][y] == m:
                i1 = min(i1, x)
                j1 = min(j1, y)
                i2 = max(i2, x)
                j2 = max(j2, y)

    return (i1, j1), (i2, j2)

def paint_canvas(col, c):
    begin, end = boundary[int(col)]
    for i in range(begin[0], end[0] + 1):
        for j in range(begin[1], end[1] + 1):
            c[i][j] = col

for i in range(1, 10):
    boundary.append(get_boundary(str(i)))

before = {x: set() for x in colors}
for x in colors:
    (x1, y1), (x2, y2) = get_boundary(x)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            after = paint[i][j]
            if after!= x:
                before[after].add(x)

for seq in per:
    flag = False
    for e in seq:
        for d in before[e]:
            if seq.index(d) > seq.index(e):
                flag = True
                break
        if flag:
            break

    if flag:
        continue

    canvas = [['0'] * n for _ in range(n)]
    if seq[0] not in possible:
        for color in seq:
            paint_canvas(color, canvas)

        if canvas == paint:
            possible.add(seq[0])

print(len(possible))



