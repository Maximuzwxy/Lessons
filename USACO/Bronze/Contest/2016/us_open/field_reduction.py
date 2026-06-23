"""
USACO 2016 US Open Contest, Bronze - Problem 3: Field Reduction
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=641

Tags: Brute Force, Ad Hoc, Geometry

Difficulty: hard

Problem Description:
-------------------
N cows (3 ≤ N ≤ 50,000) are at distinct positions in a 2D field. FJ wants to
enclose all cows with the smallest axis-aligned rectangle. He can sell exactly
one cow to make the enclosure even smaller.

Find the minimum possible area of the enclosing rectangle after removing one
carefully chosen cow. Cows are treated as points (not unit squares), and the
answer can be 0 if all remaining cows are on the same line.

Cow coordinates are in [1, 40,000].

Sample Input:              Sample Output:
4                          12
2 4
1 1
5 2
17 25

Explanation:
  Original: min_x=1, max_x=17, min_y=1, max_y=25 → area = 16 × 24 = 384
  Remove cow at (17, 25): min_x=1, max_x=5, min_y=1, max_y=4 → area = 4 × 3 = 12


====================================================================
Solution 1: Boundary-Essential Filtering (User's Solution)
====================================================================
Key insight: only removing a cow on the boundary can shrink the area, and
among those, only cows that are the SOLE cow at a boundary coordinate can
actually reduce the bounding box.

  1. Read all cows, tracking min/max x/y and frequency of each coordinate.
  2. Filter to boundary cows that are NOT strictly interior:
     a cow is a "boundary cow" if it sits on at least one of the 4 edges.
  3. Among boundary cows, only consider those that are essential — i.e.,
     the ONLY cow at that x- or y-edge (freq == 1). If multiple cows share
     the same min_x, removing one doesn't change the bounding box.
  4. For each essential boundary cow, temporarily remove it (list slicing)
     and recompute the area of the remaining cows via get_area().
  5. Take the minimum.

Unlike the old corner-only approach, this correctly handles ALL boundary
cows (e.g., a cow at (min_x, mid_y) that is the sole min_x cow).

Time Complexity: O(N) to read and filter, O(B × N) where B ≤ 4 is the
number of essential boundary cows (at most one per edge, so O(N)).
Space Complexity: O(40001) for frequency arrays.
"""

import sys

sys.stdin = open('reduce.in', 'r')
sys.stdout = open('reduce.out', 'w')

n = int(input())
cows = []                 # list of all cow positions
l_x = [0] * 40001         # frequency of each x coordinate
l_y = [0] * 40001         # frequency of each y coordinate
min_x = min_y = 40000
max_x = max_y = 0

# Read all cows and track coordinate frequencies
for i in range(n):
    x, y = map(int, input().split())
    cows.append([x, y])
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    l_x[x] += 1
    l_y[y] += 1

# Area with ALL cows (no removal)
min_area = (max_x - min_x) * (max_y - min_y)


def get_area(lst):
    """Compute the bounding-rectangle area for a list of cow positions."""
    x1 = y1 = 40000
    x2 = y2 = 0

    for x, y in lst:
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)

    return (x2 - x1) * (y2 - y1)


# Try removing each essential boundary cow
index = 0
for x, y in cows:
    # Only consider cows on the boundary (not strictly interior)
    if not (min_x < x < max_x and min_y < y < max_y):
        # Only consider if this cow is the SOLE occupant of its boundary edge
        if x == min_x and l_x[x] == 1 \
                or x == max_x and l_x[x] == 1 \
                or y == min_y and l_y[y] == 1 \
                or y == max_y and l_y[y] == 1:
            # Temporarily remove this cow and recompute area
            area = get_area(cows[:index] + cows[index + 1:])
            min_area = min(min_area, area)

    index += 1

print(min_area)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# The official C++ solution uses multiset<int> to store all x and y values.
# For each cow, temporarily erase its coordinates from the multisets, query
# the new min/max in O(log N), compute area, then re-insert.
#
# Python doesn't have a built-in multiset, so we emulate it by tracking the
# two smallest and two largest x and y coordinates, AND the frequency of
# each boundary value. When removing a cow, if it was the ONLY cow at a
# boundary, we fall back to the second-most extreme; otherwise the boundary
# stays the same.
#
# Time Complexity: O(N), Space Complexity: O(N).

# import sys
# sys.stdin = open('reduce.in', 'r')
# sys.stdout = open('reduce.out', 'w')
#
# n = int(input())
#
# # Track the two smallest and two largest x and y coordinates
# INF = 10**9
# x1 = x2 = INF       # smallest, second smallest x
# x3 = x4 = 0         # second largest, largest x
# y1 = y2 = INF
# y3 = y4 = 0
#
# x_freq = {}         # count of cows at each x coordinate
# y_freq = {}         # count of cows at each y coordinate
# x = [0] * n
# y = [0] * n
#
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
#     x_freq[x[i]] = x_freq.get(x[i], 0) + 1
#     y_freq[y[i]] = y_freq.get(y[i], 0) + 1
#
#     # Update two smallest x
#     if x[i] < x1:
#         x2 = x1; x1 = x[i]
#     elif x[i] < x2:
#         x2 = x[i]
#
#     # Update two largest x
#     if x[i] > x4:
#         x3 = x4; x4 = x[i]
#     elif x[i] > x3:
#         x3 = x[i]
#
#     # Same for y
#     if y[i] < y1:
#         y2 = y1; y1 = y[i]
#     elif y[i] < y2:
#         y2 = y[i]
#
#     if y[i] > y4:
#         y3 = y4; y4 = y[i]
#     elif y[i] > y3:
#         y3 = y[i]
#
# # Original area
# ans = (x4 - x1) * (y4 - y1)
#
# # Try removing each cow
# for i in range(n):
#     # If the cow is the ONLY one at this boundary, fall back to second-most
#     x_min = x2 if x[i] == x1 and x_freq[x1] == 1 else x1
#     x_max = x3 if x[i] == x4 and x_freq[x4] == 1 else x4
#     y_min = y2 if y[i] == y1 and y_freq[y1] == 1 else y1
#     y_max = y3 if y[i] == y4 and y_freq[y4] == 1 else y4
#     ans = min(ans, (x_max - x_min) * (y_max - y_min))
#
# print(ans)
