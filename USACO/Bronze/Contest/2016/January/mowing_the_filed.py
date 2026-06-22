"""
USACO 2016 January Contest, Bronze - Problem 3: Mowing the Field
https://usaco.org/index.php?page=viewproblem2&cpid=593

Problem Description:
  FJ mows grass on a large 2D grid. He starts at t=0. Each statement "D S"
  means he takes S steps in direction D (N/E/S/W), one step per unit of time.
  Grass cut at time t regrows at time t+x. FJ never steps on already-cut grass.

  That is, for any cell visited twice, the time between visits must be >= x.
  Find the maximum possible x. If no cell is visited twice, output -1.

  Example: N 10; E 2; S 3; W 4; S 5; E 8  →  x = 10
    (cell visited at t=7 and t=17 → gap=10; cell at t=2 and t=26 → gap=24)

Input (mowing.in):
  Line 1: N (1 ≤ N ≤ 100)
  Next N lines: D S  (D in {N,E,S,W}, 1 ≤ S ≤ 10)

Output (mowing.out):
  Maximum x such that FJ never steps on cut grass, or -1 if never revisited.
"""

import sys

sys.stdin = open('mowing.in', 'r')
sys.stdout = open('mowing.out', 'w')


# ============================================================
# Solution 1: Track all visited cells with per-step aging
# Idea: maintain a list `snake` of visited cells. Each step,
#       increment the "age" of every cell by 1 (via update()).
#       When revisiting a cell, its age is the time gap since
#       the last visit. Keep the minimum of these gaps as x.
# Time: O(N * S * V) where V = number of distinct cells visited,
#       bounded by total steps ≤ 1000.
# ============================================================

n = int(input())
s = 2001                              # grid size large enough for all coords
grid = [[0] * s for _ in range(s)]    # grid[i][j] = time since last visit
cur_i, cur_j = s // 2, s // 2         # start at center to avoid negative coords
grid[cur_i][cur_j] = 1
max_x = -1                             # answer: max valid x
snake = [(cur_i, cur_j)]              # list of all visited cells, in order


def mow(d):
    """Return (di, dj) step vector for direction d."""
    di = dj = 0

    if d == 'N':
        di = -1
    elif d == 'S':
        di = 1
    elif d == 'E':
        dj = 1
    elif d == 'W':
        dj = -1

    return di, dj


def update():
    """Increment age of all previously visited cells by 1 time unit."""
    for i, j in snake:
        grid[i][j] += 1


for k in range(n):
    D, steps = input().split()
    for m in range(int(steps)):
        update()                     # age all visited cells by one
        x, y = mow(D)
        cur_i += x
        cur_j += y

        if grid[cur_i][cur_j] != 0:
            # Revisiting this cell: time gap = current age - 1
            x = grid[cur_i][cur_j] - 1
            if max_x == -1:
                max_x = x
            else:
                max_x = min(max_x, x)   # x must satisfy the tightest constraint
        else:
            # First visit to this cell
            snake.append((cur_i, cur_j))
        grid[cur_i][cur_j] = 1        # reset age to 1 (just visited)

print(max_x)


# ============================================================
# Solution 2: Timestamp array (official solution, Python translation)
# Idea: Instead of tracking all cells each step, store the absolute
#       timestamp when each cell was last visited. On revisit,
#       compute gap = currentTime - lastVisit directly.
# Time: O(total_steps), each step is O(1).
#
# To use this solution, uncomment the block below and comment out Solution 1.
# ============================================================

# ---- START: Official Solution ----

import sys
sys.stdin = open('mowing.in', 'r')
sys.stdout = open('mowing.out', 'w')

SIZE = 2001
# last_time[i][j] = last timestamp cell (i,j) was visited, or -1 if unvisited
last_time = [[-1] * SIZE for _ in range(SIZE)]

cur_x = cur_y = SIZE // 2            # start at center to avoid negative coords
last_time[cur_x][cur_y] = 0          # mark start at time 0
current_time = 0
answer = 1001                        # max gap can't exceed total steps (≤ 1000)

n = int(input())

for _ in range(n):
    direction, steps = input().split()
    steps = int(steps)

    # Determine step direction vector
    dir_x = dir_y = 0
    if direction == 'N':
        dir_x = -1
    elif direction == 'S':
        dir_x = 1
    elif direction == 'W':
        dir_y = -1
    elif direction == 'E':
        dir_y = 1

    for _ in range(steps):
        cur_x += dir_x
        cur_y += dir_y
        current_time += 1

        # If visited before, gap is constraint on x
        if last_time[cur_x][cur_y] >= 0:
            gap = current_time - last_time[cur_x][cur_y]
            if gap < answer:
                answer = gap

        last_time[cur_x][cur_y] = current_time

print(-1 if answer == 1001 else answer)

# ---- END: Official Solution ----
