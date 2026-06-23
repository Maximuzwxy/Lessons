"""
USACO 2016 December Contest, Bronze - Problem 1: Square Pasture
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=663

Tags: Geometry, Ad Hoc

Difficulty: very_easy

Problem Description:
-------------------
Two axis-aligned rectangular pastures (non-overlapping, non-touching) need to
be replaced by a single axis-aligned square pasture that covers all the area
formerly enclosed by both rectangles. Find the minimum possible area of this
square.

Constraints: Coordinates are in [0, 10]. x2 > x1, y2 > y1 for each rectangle.

Sample Input:              Sample Output:
6 6 8 8                    49
1 8 4 9

Explanation:
  Rect 1: (6,6) to (8,8), Rect 2: (1,8) to (4,9)
  Bounding rectangle: x = [1, 8] → width 7, y = [6, 9] → height 3
  Square side = max(7, 3) = 7 → area = 49


====================================================================
Solution 1: Bounding Box (User's Solution)
====================================================================
Find the overall bounding rectangle of both pastures (min/max x and y), then
take the larger dimension as the square's side length and square it.

The key insight: the square must span from min_x to max_x (width) and from
min_y to max_y (height). Since it's a square, the side must be at least the
larger of these two spans. The square can be shifted within the other dimension
to cover the smaller span.

Time Complexity: O(1)
"""

import sys

sys.stdin = open('square.in', 'r')
sys.stdout = open('square.out', 'w')

# Read the two rectangles: (x1, y1) = lower-left, (x2, y2) = upper-right
f_x1, f_y1, f_x2, f_y2 = map(int, input().split())
s_x1, s_y1, s_x2, s_y2 = map(int, input().split())

# Find the overall bounding box containing both rectangles
x1 = min(f_x1, s_x1)    # leftmost x (always from lower-left corners)
x2 = max(f_x2, s_x2)    # rightmost x (always from upper-right corners)

y1 = min(f_y1, s_y1)    # bottommost y
y2 = max(f_y2, s_y2)    # topmost y

# Square side = larger of width and height
side = max((x2 - x1), (y2 - y1))
print(side ** 2)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same idea but tracks running min/max with conditional statements as it
# reads coordinates, instead of using Python's min/max over all values.
#
# Time Complexity: O(1)

# import sys
# sys.stdin = open('square.in', 'r')
# sys.stdout = open('square.out', 'w')
#
# smallest_x = 10
# largest_x = 0
# smallest_y = 10
# largest_y = 0
#
# for _ in range(2):
#     x_low, y_low, x_high, y_high = map(int, input().split())
#     if x_low < smallest_x:
#         smallest_x = x_low
#     if x_high > largest_x:
#         largest_x = x_high
#     if y_low < smallest_y:
#         smallest_y = y_low
#     if y_high > largest_y:
#         largest_y = y_high
#
# side = max(largest_x - smallest_x, largest_y - smallest_y)
# print(side * side)
