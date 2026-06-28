"""
USACO 2017 December Contest, Bronze - Problem 1: Blocked Billboard
===================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=759

Tags: Geometry, 2D Grid, Rectangle Intersection

Difficulty: easy

Problem Description:
-------------------
Two rectangular billboards (Alex's and Greg's) are visible in Bessie's
field of view. The two billboards are guaranteed NOT to overlap.

A truck parks and may block part of one or both billboards. Given the
lower-left (x1, y1) and upper-right (x2, y2) coordinates of each billboard
and the truck, compute the total visible area of both billboards.

All coordinates are in the range [-1000, 1000].

Sample Input:              Sample Output:
1 2 3 5                    17
6 0 10 4
2 1 8 3

Explanation:
  Billboard 1 (Alex): (1,2) to (3,5) → area = 2 * 3 = 6
  Billboard 2 (Greg): (6,0) to (10,4) → area = 4 * 4 = 16
  Truck: (2,1) to (8,3)
  Billboard 1 ∩ Truck = (2,2) to (3,3) → blocked area = 1
  Billboard 2 ∩ Truck = (6,1) to (8,3) → blocked area = 4
  Visible = 6 - 1 + 16 - 4 = 17


====================================================================
Solution 1: 2D Grid Pixel Marking (User's Solution)
====================================================================
The idea is to draw the entire scene onto a 2D grid:

  1. Find the bounding rectangle that contains both billboards and the truck.
  2. Create a 2D array (grid[y][x]) covering this range.
  3. Mark all cells covered by each billboard as 1.
  4. Mark all cells covered by the truck as 0 (overwriting billboard cells).
  5. Count all remaining 1 cells — that's the total visible area.

This is a brute-force "pixel counting" approach. Since N ≤ 2000, the grid
has at most 4 million cells, well within time/memory limits for Bronze.

Time Complexity: O(N^2) where N = max coordinate range (≤ 2000).
"""

import sys

sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')

# Read coordinates of the two billboards and the truck
# Each: (x1, y1) = lower-left, (x2, y2) = upper-right
alex_x1, alex_y1, alex_x2, alex_y2 = map(int, input().split())
greg_x1, greg_y1, greg_x2, greg_y2 = map(int, input().split())
truck_x1, truck_y1, truck_x2, truck_y2 = map(int, input().split())

# Step 1: Find the overall bounding rectangle containing everything
# x1 = min(alex_x1, greg_x1, truck_x1)
# x2 = max(alex_x2, greg_x2, truck_x2)
# y1 = min(alex_y1, greg_y1, truck_y1)
# y2 = max(alex_y2, greg_y2, truck_y2)

# Step 2: Create a 2D grid — area[y][x], initially all 0
# area = [[0] * (x2 + 1) for _ in range(y2 + 1)]
area = [[0] * 2000 for _ in range(2000)]
offset = 1000
# Step 3: Paint billboard 1 (Alex) onto the grid
for i in range(alex_y1 + offset, alex_y2 + offset):     # i = y-coordinate (row)
    for j in range(alex_x1 + offset, alex_x2 + offset): # j = x-coordinate (column)
        area[i][j] = 1

# Step 3 (cont.): Paint billboard 2 (Greg) onto the grid
for i in range(greg_y1 + offset, greg_y2 + offset):
    for j in range(greg_x1 + offset, greg_x2 + offset):
        area[i][j] = 1

# Step 4: Erase the truck — any cell under the truck gets set to 0
for i in range(truck_y1 + offset, truck_y2 + offset):
    for j in range(truck_x1 + offset, truck_x2 + offset):
        area[i][j] = 0

# Step 5: Count all remaining visible pixels (cells still marked 1)
cnt = 0
for l in area:
    cnt += sum(l)       # sum of each row = visible pixels in that row
print(cnt)


# =====================================================================
# Solution 2: Set-based Range Intersection (User's Solution)
# =====================================================================
# Builds X and Y coordinate sets for each billboard and the truck, then
# uses Python set intersection (&) to find overlapping X/Y ranges.
#
#   visible = area(b1) + area(b2) − overlap(b1, truck) − overlap(b2, truck)
#
# This is geometric but uses set operations instead of the max/min formula.
# The set approach feels like "find common elements in two ranges" — very
# intuitive, especially for beginners.
#
# Time Complexity: O(R) where R = coordinate range (creating full integer
#                  sets). Fine for this problem's limits but less efficient
#                  than O(1) max/min for larger ranges.
#
# import sys
# sys.stdin = open('billboard.in', 'r')
# sys.stdout = open('billboard.out', 'w')
#
# x1, y1, x2, y2 = map(int, input().split())   # billboard 1
# x3, y3, x4, y4 = map(int, input().split())   # billboard 2
# x5, y5, x6, y6 = map(int, input().split())   # truck
#
#
# def overlap_area(bx1, by1, bx2, by2, tx1, ty1, tx2, ty2):
#     """
#     Compute overlap area between a billboard and the truck using set
#     intersection. Build integer range sets for both X and Y, take
#     intersection, and if both are non-empty, compute area from sorted
#     endpoints.
#     """
#     bx = set(range(bx1, bx2 + 1))
#     by = set(range(by1, by2 + 1))
#     tx = set(range(tx1, tx2 + 1))
#     ty = set(range(ty1, ty2 + 1))
#
#     cx = sorted(bx & tx)
#     cy = sorted(by & ty)
#
#     if cx and cy:
#         return (cx[-1] - cx[0]) * (cy[-1] - cy[0])
#     return 0
#
#
# total = (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3)
# covered = (overlap_area(x1, y1, x2, y2, x5, y5, x6, y6)
#          + overlap_area(x3, y3, x4, y4, x5, y5, x6, y6))
# print(total - covered)


# =====================================================================
# Solution 3: Official USACO Solution (by Brian Dean) — Python Translation
# =====================================================================
# Uses rectangle intersection math with max/min formulas:
#
#   visible = area(billboard1) + area(billboard2)
#             - overlap(billboard1, truck)
#             - overlap(billboard2, truck)
#
# The overlap of two axis-aligned rectangles is:
#   x_overlap = max(0, min(r1.x2, r2.x2) - max(r1.x1, r2.x1))
#   y_overlap = max(0, min(r1.y2, r2.y2) - max(r1.y1, r2.y1))
#   overlap_area = x_overlap * y_overlap
#
# Comparison of Solution 2 vs Solution 3:
#   - Both are geometric O(1) approaches: sum of billboard areas minus
#     the area blocked by the truck.
#   - Solution 2 uses Python set intersection to find overlapping X/Y
#     ranges. This is visual and explicit — you can see "X ranges
#     overlap" and "Y ranges overlap" as two separate checks. But it
#     creates full sets of all integer coordinates in each range,
#     which is O(R) time and memory where R = coordinate span.
#   - Solution 3 uses a single max/min formula per dimension. No sets,
#     no loops, no allocation — pure O(1) arithmetic. Much more compact
#     and the standard way to compute axis-aligned rectangle intersection.
#   - Solution 2 is more beginner-friendly (sets feel like "find common
#     elements"), while Solution 3 is the standard computational geometry
#     idiom.
#
# Time Complexity: O(1), purely mathematical.
#
# import sys
# sys.stdin = open('billboard.in', 'r')
# sys.stdout = open('billboard.out', 'w')
#
# def area(x1, y1, x2, y2):
#     """Compute the area of a rectangle given lower-left and upper-right corners."""
#     return (x2 - x1) * (y2 - y1)
#
# def overlap(x1, y1, x2, y2, p1, q1, p2, q2):
#     """
#     Compute the overlapping area between two rectangles.
#     Rectangle 1: (x1,y1) to (x2,y2), Rectangle 2: (p1,q1) to (p2,q2).
#     """
#     x_overlap = max(0, min(x2, p2) - max(x1, p1))
#     y_overlap = max(0, min(y2, q2) - max(y1, q1))
#     return x_overlap * y_overlap
#
# # Read input
# ax1, ay1, ax2, ay2 = map(int, input().split())
# gx1, gy1, gx2, gy2 = map(int, input().split())
# tx1, ty1, tx2, ty2 = map(int, input().split())
#
# # Total visible = sum of areas - overlaps with truck
# ans = (area(ax1, ay1, ax2, ay2) + area(gx1, gy1, gx2, gy2)
#        - overlap(ax1, ay1, ax2, ay2, tx1, ty1, tx2, ty2)
#        - overlap(gx1, gy1, gx2, gy2, tx1, ty1, tx2, ty2))
#
# print(ans)
