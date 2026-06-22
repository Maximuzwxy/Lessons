"""
USACO 2017 US Open Contest, Bronze - Problem 3: Modern Art
===========================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=737

Tags: Ad Hoc, Dependency Graph, Bounding Box
      — Pure brute-force permutation enumeration O(N!) is insufficient:
        you must discover the "minimal bounding box + dependency" insight
        to reduce the problem to counting colors with no dependencies.

Problem Description:
-------------------
The great bovine artist Picowso has created a modern masterpiece. She
painted an N x N canvas (1 <= N <= 10) using exactly one brush stroke per
color. Each brush stroke is an axis-aligned rectangle painted in one of
9 colors (digits 1-9). The canvas starts completely blank (color 0).

Because some rectangles may be painted on top of others, later rectangles
can completely or partially cover earlier ones. Given the final appearance
of the painting, determine how many colors could have been the first one
painted (i.e., which colors could have been painted first in some valid
ordering of the rectangles).

Sample Input:              Sample Output:
4                          1
2230
2737
2777
0000

Explanation: The painting has colors 2, 3, 7. Color 3 appears within the
bounding box of color 2, so 3 must have been painted after 2. Color 7 also
appears within color 2's box. So only color 2 could have been first.

Key Insight:
------------
A color C could have been the first painted if and only if there is NO other
color S whose bounding box contains a cell of color C. If C appears inside
S's bounding box, then S must have been painted before C (otherwise S would
have covered C in that cell).


====================================================================
Solution 1: Dependency Graph Counting (Most Elegant)
====================================================================
Step 1: For each color, find its minimal bounding box (top/bottom/left/right
        based on where that color's cells appear in the final painting).

Step 2: Build a dependency graph: for each color x, look inside x's bounding
        box. Any OTHER color y that appears inside x's box must have been
        painted AFTER x (because y covers x in that spot). So x → y means
        "x must be painted before y".

        Equivalently, `before[y]` = set of all colors that must come before y.

Step 3: A color can be the FIRST one painted ⟺ `before[color]` is empty
        (no other color needs to be painted before it).

        Simply count how many colors have an empty dependency set.

This is much more elegant than both the permutation enumeration (Solution 1b)
and the official USACO solution (Solution 2) because it reuses the dependency
graph already built for free, avoiding both O(N!) permutation loops and
redundant pairwise bounding box scans.

Time Complexity: O(C * N^2) where C ≤ 9, N ≤ 10.
"""

import sys
# sys.stdin = open('art.in', 'r')
# sys.stdout = open('art.out', 'w')

n = int(input())
colors = set()       # all colors that appear in the painting
paint = []           # 2D grid representing the final painting

for _ in range(n):
    s = input()
    for c in s:
        colors.add(c)
    paint.append(list(s))

colors.discard('0')  # 0 is the blank canvas, not a color


def get_boundary(m):
    """
    Find the bounding box of color m in the painting.
    Returns ((top_row, left_col), (bottom_row, right_col)).
    Initial values are inverted so the first match triggers min/max correctly.
    """
    i1 = j1 = n - 1    # min row, min col
    i2 = j2 = 0         # max row, max col

    for x in range(n):
        for y in range(n):
            if paint[x][y] == m:
                i1 = min(i1, x)
                j1 = min(j1, y)
                i2 = max(i2, x)
                j2 = max(j2, y)

    return (i1, j1), (i2, j2)


# Build dependency graph:
#   before[x] = set of colors that must be painted BEFORE x.
#   If color y appears inside color x's bounding box, then x was painted before y.
before = {x: set() for x in colors}
for x in colors:
    (x1, y1), (x2, y2) = get_boundary(x)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            after = paint[i][j]
            if after != x:
                before[after].add(x)  # x must be painted before `after`

# --- Solution 1: Count colors with no dependencies ---
# A color can be the first one painted iff nothing must come before it,
# i.e., its `before` set is empty.
cnt = 0
for k, v in before.items():
    if len(v) == 0:       # no color needs to be painted before k
        cnt += 1          # k is a candidate for being the first color
print(cnt)


# =====================================================================
# Solution 1b: Permutation-based Brute Force Enumeration (commented out)
# =====================================================================
# Range: line ~115 to ~145
#
# This is an alternative approach: generate ALL permutations of the colors
# and check each one against the dependency constraints in `before`.
# The first color in any valid permutation is counted as a candidate.
#
# This method also simulates painting the canvas in that order and verifies
# the result matches the original. It's more intuitive but much slower
# (O(C! * N^2)), useful for understanding the problem but unwieldy compared
# to the dependency counting approach above.

# from itertools import permutations

# # Precompute boundaries for all 9 possible colors (needed by paint_canvas)
# boundry = [((0, 0), (0, 0))]  # dummy at index 0
# for i in range(1, 10):
#     boundry.append(get_boundry(str(i)))
#
# def paint_canvas(col, c):
#     begin, end = boundry[int(col)]
#     for i in range(begin[0], end[0] + 1):
#         for j in range(begin[1], end[1] + 1):
#             c[i][j] = col
#
# possible = set()
#
# # Try all permutations of colors
# for seq in permutations(colors, len(colors)):
#     # Check if this permutation respects all dependency constraints
#     flag = False  # becomes True if a constraint is violated
#     for e in seq:
#         for d in before[e]:
#             # d must come before e, so if d appears after e in seq, invalid
#             if seq.index(d) > seq.index(e):
#                 flag = True
#                 break
#         if flag:
#             break
#
#     if flag:
#         continue
#
#     # This permutation is valid. Simulate painting in this order
#     # and verify it matches the original painting.
#     canvas = [['0'] * n for _ in range(n)]
#     if seq[0] not in possible:  # optimization: only check if not yet found
#         for color in seq:
#             paint_canvas(color, canvas)
#
#         if canvas == paint:
#             possible.add(seq[0])
#
# print(len(possible))


# =====================================================================
# Solution 2: Official USACO Solution (by Brian Dean) — Python Translation
# =====================================================================
# Range: line ~165 to ~250
#
# The official O(N^3) approach: for each color i, check whether any other
# color j's bounding box contains a cell of color i. If so, j must be
# painted before i, so i cannot be first. Otherwise i is a candidate.
#
# Compared to Solution 1 above, this method finds bounding boxes for EACH
# pairwise check (no precomputed dependency graph), leading to redundant
# O(N^2) scans per pair.

# import sys
# sys.stdin = open('art.in', 'r')
# sys.stdout = open('art.out', 'w')
#
# n = int(input())
# B = []  # 2D grid of integers 0-9
#
# for _ in range(n):
#     s = input().strip()
#     B.append([int(ch) for ch in s])
#
#
# def color_appears(c):
#     """Return True if color c appears anywhere in the painting."""
#     for i in range(n):
#         for j in range(n):
#             if B[i][j] == c:
#                 return True
#     return False
#
#
# def on_top_of(c1, c2):
#     """
#     Is c1 "on top of" c2? Returns True if any cell of color c1 falls within
#     the bounding box of c2. If so, c2 must have been painted before c1.
#     """
#     # Step 1: Find c2's bounding box
#     top, bottom = n, 0
#     left, right = n, 0
#     for i in range(n):
#         for j in range(n):
#             if B[i][j] == c2:
#                 top = min(top, i)
#                 bottom = max(bottom, i)
#                 left = min(left, j)
#                 right = max(right, j)
#
#     # Step 2: Check if any c1 cell falls within this bounding box
#     for i in range(top, bottom + 1):
#         for j in range(left, right + 1):
#             if B[i][j] == c1:
#                 return True
#     return False
#
#
# answer = 0
# for i in range(1, 10):
#     if not color_appears(i):
#         continue
#
#     could_be_first = True
#     for j in range(1, 10):
#         if j != i and color_appears(j) and on_top_of(i, j):
#             # i appears inside j's bounding box, so j must be before i
#             # Therefore i cannot be first
#             could_be_first = False
#             break
#
#     if could_be_first:
#         answer += 1
#
# print(answer)
