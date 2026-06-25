"""
USACO 2018 January Contest, Bronze - Problem 1: Blocked Billboard II
=====================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=783

Tags: Geometry, Ad Hoc

Difficulty: hard

Problem Description:
-------------------
Two rectangular billboards: a lawnmower billboard (bad) and a cow feed
billboard (good). The cow feed billboard is in front and may partially
obscure the lawnmower one.

Bessie wants to cover the remaining visible portion of the lawnmower
billboard with a rectangular tarp (axis-aligned). Find the minimum area
of the tarp needed. The tarp may need to be larger than the exposed area
if the exposed region is not a single rectangle.

Input:  Line 1: x1 y1 x2 y2 — lawnmower billboard (lower-left, upper-right)
        Line 2: x3 y3 x4 y4 — cow feed billboard
        All coordinates in [-1000, 1000].
Output: A single integer — minimum tarp area.

Sample Input:              Sample Output:
2 1 7 4                   15
5 -1 10 3

Explanation:
The cow feed billboard covers the lower-right corner of the lawnmower
billboard. The exposed portion forms an L-shape, so the tarp must
cover the entire lawnmower billboard (area = 5×3 = 15).

====================================================================
Solution 1: Pixel Marking + Bounding Box (User's Solution)
====================================================================
Use a 2001×2001 grid (offset by 1000 to handle negative coordinates).
  1. Mark all cells covered by the lawnmower billboard as 1.
  2. Zero out all cells covered by the cow feed billboard.
  3. Compute the max number of 1s in any row (width) and any column
     (height).
  4. Special case: if the cow feed is fully inside the lawnmower in
     one dimension → must cover the full lawnmower area. Otherwise,
     the remaining 1s form a single rectangle, and height × width
     gives the minimal tarp area.

This is a brute-force "pixel drawing" approach. The grid has at most
4 million cells, well within limits.

Time Complexity: O(R²) where R = 2000 (coordinate range).
"""

import sys

sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')

x1, y1, x2, y2 = map(int, input().split())   # lawnmower billboard
x3, y3, x4, y4 = map(int, input().split())   # cow feed billboard

# Create a 2001×2001 grid to handle coordinates from -1000 to 1000
b = [[0] * 2001 for _ in range(2001)]
offset = 1000

# Step 1: Paint the lawnmower billboard onto the grid
for i in range(y1 + offset, y2 + offset):
    for j in range(x1 + offset, x2 + offset):
        b[i][j] = 1

# Step 2: Erase the cow feed billboard (cover → set to 0)
for i in range(y3 + offset, y4 + offset):
    for j in range(x3 + offset, x4 + offset):
        b[i][j] = 0

width = 0
height = 0

# Step 3: Find max column sum → height of exposed region
for i in range(2001):
    h = 0
    for j in range(2001):
        if b[j][i] == 1:
            h += b[j][i]
    height = max(height, h)

# Step 4: Find max row sum → width of exposed region
for i in range(2001):
    w = 0
    for j in range(2001):
        w += b[i][j]
    width = max(width, w)

# If cow feed is completely inside the lawnmower in one dimension,
# the exposed area is not a single rectangle → need full tarp.
if x1 <= x3 < x4 <= x2 or y1 <= y3 < y4 <= y2:
    print((x2 - x1) * (y2 - y1))
else:
    print(height * width)


# =====================================================================
# Solution 2: Corner Counting + Edge-based Area (User's Solution)
# =====================================================================
# Also uses corner counting, but instead of subtracting intersection area,
# it directly computes the remaining tarp dimensions based on WHICH two
# corners are covered.
#
#   - 0 or 1 corners covered → need full lawnmower area (exposed region is
#     L-shaped or worse).
#   - 2 corners on the SAME SIDE (e.g., left edge: corners 0 and 1) →
#     the cow feed carves a rectangular notch. Compute the exposed rectangle
#     directly: e.g., left covered → width = x2 - x4, height = y2 - y1.
#   - 2 diagonally opposite corners → cann't carve a single rectangle,
#     but this case should not occur for axis-aligned rectangles actually.
#
# This is more explicit than the official solution — it names which edge
# is exposed rather than relying on a generic intersection formula.
#
# Time Complexity: O(1)
#
# import sys
#
# sys.stdin = open('billboard.in', 'r')
# sys.stdout = open('billboard.out', 'w')
#
# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())
#
#
# def covered(x, y):
#     """Check if point (x, y) is strictly inside the cow feed billboard."""
#     if x3 < x < x4 and y3 < y < y4:
#         return True
#     return False
#
#
# # corners: [bottom-left, top-left, top-right, bottom-right]
# corners = [1 if covered(x1, y1) else 0,   # bottom-left
#            1 if covered(x1, y2) else 0,   # top-left
#            1 if covered(x2, y2) else 0,   # top-right
#            1 if covered(x2, y1) else 0]   # bottom-right
#
# cnt = sum(corners)
# area = 0
# if cnt == 1 or cnt == 0:
#     area = (x2 - x1) * (y2 - y1)                     # full lawnmower area
# elif cnt == 2:
#     if corners[0] and corners[1]:                    # left edge covered
#         area = (y2 - y1) * (x2 - x4)
#     if corners[2] and corners[3]:                    # right edge covered
#         area = (y2 - y1) * (x3 - x1)
#     if corners[1] and corners[2]:                    # top edge covered
#         area = (x2 - x1) * (y3 - y1)
#     if corners[0] and corners[3]:                    # bottom edge covered
#         area = (x2 - x1) * (y2 - y4)
#
# print(area)


# =====================================================================
# Solution 3: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Also corner-counting, but uses a unified intersection formula instead
# of per-edge branching. After confirming exactly 2 corners are covered:
#   exposed = full_area - intersection_area
# This avoids enumerating which two corners — the intersection is always
# max/min of the four coordinates.
#
#  - 0 or 1 corners → full area
#  - 2 corners → full area − intersection area
#  - 4 corners → 0 (completely hidden)
#
# Comparison of Solution 2 vs Solution 3:
#   - Both are O(1) corner-counting geometry approaches.
#   - Solution 2 explicitly branches on which edge is covered, computing
#     the remaining rectangle's width/height directly. More verbose but
#     easier to visualize ("left edge covered → width = x2 - x4").
#   - Solution 3 uses a single unified formula: full_area - intersection.
#     More concise and requires no per-edge case analysis — the
#     intersection calculation naturally handles all 4 edge cases.
#   - Solution 2 enumerates 4 possible edge cases; Solution 3 collapses
#     them into one subtraction. Both are correct and O(1).
#
# Time Complexity: O(1)
#
# import sys
#
# sys.stdin = open('billboard.in', 'r')
# sys.stdout = open('billboard.out', 'w')
#
# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())
#
#
# def covered(x, y, x1, y1, x2, y2):
#     """Return True if point (x, y) is inside the rectangle
#     bounded by (x1, y1) and (x2, y2)."""
#     return x1 <= x <= x2 and y1 <= y <= y2
#
#
# # Count how many corners of the lawnmower billboard are covered
# cornerCover = 0
# if covered(x1, y1, x3, y3, x4, y4):
#     cornerCover += 1
# if covered(x1, y2, x3, y3, x4, y4):
#     cornerCover += 1
# if covered(x2, y1, x3, y3, x4, y4):
#     cornerCover += 1
# if covered(x2, y2, x3, y3, x4, y4):
#     cornerCover += 1
#
# if cornerCover < 2:
#     # Less than 2 corners covered → must cover the entire rectangle
#     print((x2 - x1) * (y2 - y1))
# elif cornerCover == 4:
#     # All 4 corners covered → completely hidden
#     print(0)
# else:
#     # Exactly 2 corners covered → subtract the intersection area
#     xL = max(x1, x3)
#     xR = min(x2, x4)
#     yL = max(y1, y3)
#     yR = min(y2, y4)
#     print((x2 - x1) * (y2 - y1) - (xR - xL) * (yR - yL))
