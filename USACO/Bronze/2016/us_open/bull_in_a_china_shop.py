"""
USACO 2016 US Open Contest, Bronze - Problem 2: Bull in a China Shop
====================================================================

Problem Description:
-------------------
Farmer John buys a glass cow figurine represented by an N x N grid (3 <= N <= 8),
where '#' characters are part of the figurine and '.' characters are empty space.
A bull runs through the shop and breaks the figurine into exactly 2 pieces, which
get mixed among K total pieces on the floor (3 <= K <= 10).

Each of the K pieces is also an N x N grid. The pieces were NOT rotated or flipped
when they fell — they only need to be shifted horizontally and/or vertically to
reassemble the original figurine. When superimposed, the two correct pieces must:
  - Not overlap (no '#' in the same position from both pieces)
  - Together exactly form the original figurine

We need to find which two pieces (1-indexed) can be shifted and superimposed to
reconstruct the original figurine.

Sample Input:              Sample Output:
4 3                        1 3
####
#..#
#.##
....
.#..
.#..
##..
....
####
##..
#..#
####
....
.###
.#..
.#..

Explanation: The original figurine (first N lines) is a 4x4 grid. Pieces 1 and 3
can be shifted and superimposed to exactly reconstruct it without overlapping.

====================================================================
Solution 1: User's Algorithm (Recursive Shift Generation)
====================================================================
Instead of iterating over all possible shift offsets (which would require nested
loops over [-N+1, N-1] for each piece), this algorithm pre-generates all valid
shifted configurations of a piece by recursively sliding it in four directions
(left, right, up, down). A shift is valid only if it doesn't push any '#'
character outside the N x N grid (i.e., the number of '#' characters is preserved).

Then, for each pair of pieces whose combined '#' count equals the original's '#'
count, we try all combinations of their shifted configurations. Two shifted pieces
are checked by superimposing them — if they have no overlapping '#' cells and
together match the original grid exactly, they are the answer.
"""

import sys
sys.stdin = open('bcs.in', 'r')
sys.stdout = open('bcs.out', 'w')

n, k = map(int, input().split())

# Read the original figurine
origin = []
pieces = []
cnt = 0  # total number of '#' cells in the original figurine

for i in range(n):
    s = input()
    cnt += s.count('#')
    origin.append(list(s))

# Read the K broken pieces
for j in range(k):
    p = []
    for m in range(n):
        p.append(list(input()))
    pieces.append(p)

def get_num(piece):
    """Count the number of '#' cells in a piece."""
    ret = 0
    for l in piece:
        ret += l.count('#')
    return ret


def shift(grid, di, dj):
    """
    Return a new grid shifted by di rows and dj columns.
    di, dj should be -1, 0, or 1 for a single-step shift.
    Only used internally for single-step directions.
    """
    new_grid = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_grid[ni][nj] = grid[i][j]
    return new_grid


def move_figurine(fig):
    """
    Generate all valid shifted configurations of a piece by recursively
    trying left, right, up, down one step at a time. A shift is valid only
    if no '#' falls outside the N x N grid — checked by verifying the '#'
    count stays the same. Uses a set of tuples for O(1) deduplication.

    Returns a list of all reachable shifted grids.
    """
    count = get_num(fig)      # number of '#' cells, used for validity check
    fs = []                   # all reachable configurations
    seen = set()              # visited states (hashable tuple representation)

    def dfs(f):
        key = tuple(tuple(row) for row in f)
        if key in seen:
            return
        seen.add(key)
        fs.append(f)

        # Try shifting in each of the 4 directions
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
            nxt = shift(f, di, dj)
            if get_num(nxt) == count:   # valid: no '#' fell off the grid
                dfs(nxt)

    dfs(fig)
    return fs


def check(p1, p2):
    """
    Check if two pieces can be shifted and superimposed to exactly form
    the original figurine. Generates all shifted versions of both pieces,
    then tries every combination to find a match.
    """
    l1 = move_figurine(p1)  # all shifted configurations of piece 1
    l2 = move_figurine(p2)  # all shifted configurations of piece 2

    for f1 in l1:
        for f2 in l2:
            # Superimpose the two shifted pieces onto an empty grid
            f = [['.'] * n for _ in range(n)]
            valid = True
            for i in range(n):
                for j in range(n):
                    if f1[i][j] == f2[i][j] == '#':
                        # Overlap detected — two '#' in the same cell, invalid
                        valid = False
                        break
                    elif f1[i][j] == '#':
                        f[i][j] = '#'
                    elif f2[i][j] == '#':
                        f[i][j] = '#'
                if not valid:
                    break
            if valid and f == origin:
                return True
    return False


# Try every pair of pieces
for x in range(k - 1):
    for y in range(x + 1, k):
        piece1 = pieces[x]
        piece2 = pieces[y]
        # Quick pruning: the two pieces must together have the same number
        # of '#' cells as the original figurine
        if get_num(piece1) + get_num(piece2) == cnt:
            if check(piece1, piece2):
                # Output 1-indexed piece numbers in sorted order
                print(x + 1, y + 1)
                break


# ====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python translation
# ====================================================================
# This is the official brute-force approach. Instead of pre-generating
# shifted configurations, it directly iterates over all possible shift
# offsets in range [-(N-1), N-1] for both pieces. For each combination,
# it maps every cell (x, y) back to the original piece position
# (x + offset_row, y + offset_col) and checks:
#   1. No two '#' cells overlap.
#   2. The combined result exactly matches the original figurine.
# Time Complexity: O(K^2 * N^6) — acceptable for N <= 8, K <= 10.

import sys
sys.stdin = open('bcs.in', 'r')
sys.stdout = open('bcs.out', 'w')

n, k = map(int, input().split())

# Read the original figurine as a 2D boolean grid (True = '#', False = '.')
goal = [[False] * n for _ in range(n)]
for i in range(n):
    line = input().strip()
    for j in range(n):
        goal[i][j] = (line[j] == '#')

# Read the K broken pieces as 2D boolean grids
pieces = []
for _ in range(k):
    piece = [[False] * n for _ in range(n)]
    for i in range(n):
        line = input().strip()
        for j in range(n):
            piece[i][j] = (line[j] == '#')
    pieces.append(piece)

# Brute-force over all pairs of pieces and all possible shift offsets
for i in range(k):
    for j in range(i + 1, k):
        # Shift offsets for piece i: row offset idx, column offset idy
        for idx in range(-n + 1, n):
            for idy in range(-n + 1, n):
                # Shift offsets for piece j: row offset jdx, column offset jdy
                for jdx in range(-n + 1, n):
                    for jdy in range(-n + 1, n):
                        good = True
                        for x in range(n):
                            if not good:
                                break
                            for y in range(n):
                                # Check if piece i has '#' at (idx+x, idy+y) after shift
                                i_has = (0 <= idx + x < n and 0 <= idy + y < n
                                         and pieces[i][idx + x][idy + y])
                                # Check if piece j has '#' at (jdx+x, jdy+y) after shift
                                j_has = (0 <= jdx + x < n and 0 <= jdy + y < n
                                         and pieces[j][jdx + x][jdy + y])

                                # Condition 1: No overlap — two '#' in the same cell
                                if i_has and j_has:
                                    good = False
                                    break
                                # Condition 2: Combined result must match the original
                                if goal[x][y] != (i_has or j_has):
                                    good = False
                                    break
                        if good:
                            print(i + 1, j + 1)
                            exit()
