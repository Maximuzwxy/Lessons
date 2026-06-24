"""
USACO 2017 December Contest, Bronze - Problem 1: Blocked Billboard
===================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=759

Tags: Geometry, 2D Grid, Rectangle Intersection

Difficulty: very_easy

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
# We only use the max to size the array (assumes all coordinates >= 0,
# which holds for the official USACO test cases).
x1 = min(alex_x1, greg_x1, truck_x1)
x2 = max(alex_x2, greg_x2, truck_x2)
y1 = min(alex_y1, greg_y1, truck_y1)
y2 = max(alex_y2, greg_y2, truck_y2)

# Step 2: Create a 2D grid — area[y][x], intially all 0
area = [[0] * (x2 + 1) for _ in range(y2 + 1)]

# Step 3: Paint billboard 1 (Alex) onto the grid
# Note: range goes up to (but not including) the upper edge,
#       because coordinates mark the edges, and the area lies between them.
for i in range(alex_y1, alex_y2):     # i = y-coordinate (row)
    for j in range(alex_x1, alex_x2): # j = x-coordinate (column)
        area[i][j] = 1

# Step 3 (cont.): Paint billboard 2 (Greg) onto the grid
# The two billboards don't overlap, so we can just paint over without conflicts.
for i in range(greg_y1, greg_y2):
    for j in range(greg_x1, greg_x2):
        area[i][j] = 1

# Step 4: Erase the truck — any cell under the truck gets set to 0
for i in range(truck_y1, truck_y2):
    for j in range(truck_x1, truck_x2):
        area[i][j] = 0

# Step 5: Count all remaining visible pixels (cells still marked 1)
cnt = 0
for l in area:
    cnt += sum(l)       # sum of each row = visible pixels in that row
print(cnt)


# =====================================================================
# Solution 2: Official USACO Solution (by Brian Dean) — Python Translation
# =====================================================================
# A much more efficient approach using rectangle intersection math:
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
# This is cleaner, faster O(1), and works for negative coordinates too.
# It's recommended over the pixel-counting approach for general use.
#
# Time Complexity: O(1), purely mathematical.

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
