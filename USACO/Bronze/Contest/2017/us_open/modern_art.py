"""
USACO 2017 US Open Contest, Bronze - Problem 3: Modern Art
===========================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=737

Tags: Ad Hoc, Brute Force, 2D Grid

Difficulty: hard

Problem Description:
-------------------
The great bovine artist Picowso paints on an N x N canvas (1 ≤ N ≤ 10).
She starts with a blank canvas (all 0s) and paints exactly 9 axis-aligned
rectangles, one in each color 1..9. Each rectangle can be as small as a
single cell or as large as the whole canvas. Later rectangles can cover
earlier ones, so some colors may be partially or completely hidden.

Given the final painting, count how many colors still visible on the canvas
could possibly have been painted FIRST in some valid painting order.

Key insight: A color C could have been the first painted if and only if
no other visible color S has a bounding box that contains a cell of color C.
If C appears inside S's bounding box, S must have been painted before C.

Sample Input:              Sample Output:
4                          1
2230
2737
2777
0000

Explanation: Colors 2, 3, 7 are visible. Color 3 appears within color 2's
bounding box → 2 must be before 3. Color 7 also appears within 2's box.
Only color 2 could have been painted first.

====================================================================
Solution 1: Dependency Graph Counting (User's Solution)
====================================================================
Step 1: For each color, compute its minimal bounding box (top/bottom/left/right
        based on where that color's cells appear in the final painting).

Step 2: Build a dependency graph: for each color x, look inside x's bounding
        box. Any OTHER color y that appears inside x's box must have been
        painted AFTER x. So x → y means "x must be painted before y".
        Equivalently, `before[y]` = set of all colors that must come before y.

Step 3: A color can be the first painted iff `before[color]` is empty.
        Count how many colors have an empty dependency set.

Time Complexity: O(C × N²) where C ≤ 9, N ≤ 10.
"""

import sys

sys.stdin = open('art.in', 'r')
sys.stdout = open('art.out', 'w')

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
#   If color y appears inside color x's bounding box, x was painted before y.
before = {x: set() for x in colors}
for x in colors:
    (x1, y1), (x2, y2) = get_boundary(x)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            after = paint[i][j]
            if after != x:
                before[after].add(x)  # x must be painted before `after`

# Count colors with no dependencies — these can be painted first
cnt = 0
for k, v in before.items():
    if len(v) == 0:       # no color needs to be painted before k
        cnt += 1          # k is a candidate for first color
print(cnt)


# =====================================================================
# Solution 2: Permutation Brute Force Enumeration (User's Solution)
# =====================================================================
# Generate ALL permutations of the visible colors and check each one against
# the dependency constraints built in Solution 1. The first color in any
# valid permutation is counted as a candidate.
#
# This method is more intuitive — it directly simulates painting orders —
# but slower (O(C! × N²)). Useful for brute-force verification.
#
# Time Complexity: O(C! × N²)
#
# from itertools import permutations
#
# # Precompute bounding boxes for all colors 1..9 (needed by paint_canvas)
# boundaries = [((0, 0), (0, 0))]  # dummy at index 0
# for i in range(1, 10):
#     boundaries.append(get_boundary(str(i)))
#
#
# def paint_canvas(col, c):
#     """Paint a rectangle of color `col` onto canvas `c`."""
#     begin, end = boundaries[int(col)]
#     for i in range(begin[0], end[0] + 1):
#         for j in range(begin[1], end[1] + 1):
#             c[i][j] = col
#
#
# possible = set()
#
# for seq in permutations(colors, len(colors)):
#     # Check if this permutation respects all dependency constraints
#     valid = True
#     for e in seq:
#         for d in before[e]:
#             if seq.index(d) > seq.index(e):  # d must come before e
#                 valid = False
#                 break
#         if not valid:
#             break
#
#     if not valid:
#         continue
#
#     # Simulate painting in this order and verify it matches the original
#     if seq[0] not in possible:
#         canvas = [['0'] * n for _ in range(n)]
#         for color in seq:
#             paint_canvas(color, canvas)
#         if canvas == paint:
#             possible.add(seq[0])
#
# print(len(possible))


# =====================================================================
# Solution 3: Official USACO Solution (by Brian Dean) — Python Translation
# =====================================================================
# For each visible color i, check whether any other visible color j has a
# bounding box that contains a cell of color i. If so, j must be painted
# before i → i cannot be first. Otherwise i is a candidate.
#
# Comparison with user's solutions:
#   - Solution 1: precomputes bounding boxes and builds a dependency graph
#                 once, then counts colors with no dependencies. O(C × N²).
#   - Solution 2: generates all permutations and simulates painting.
#                 O(C! × N²), intuitive but slower.
#   - Solution 3: for each pair of colors, computes bounding boxes on the
#                 fly and checks containment. O(C² × N²), more verbose
#                 because bounding boxes are recomputed per pair instead
#                 of cached.
#
# Time Complexity: O(C² × N²)
#
# import sys
#
# sys.stdin = open('art.in', 'r')
# sys.stdout = open('art.out', 'w')
#
# n = int(input())
# B = [list(map(int, list(input().strip()))) for _ in range(n)]
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
#     Is c1 "on top of" c2? Returns True if any cell of color c1 falls
#     within the bounding box of c2. If so, c2 must have been painted
#     before c1 → c1 cannot be first.
#     """
#     # Find c2's bounding box
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
#     # Check if any c1 cell falls within this bounding box
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
#             could_be_first = False
#             break
#
#     if could_be_first:
#         answer += 1
#
# print(answer)
