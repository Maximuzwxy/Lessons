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
Solution 1: Corner-Removal with Frequency Check (User's Solution)
====================================================================
Key insight: only removing a cow on the boundary (one of the 4 extreme edges)
can shrink the area. The approach:

  1. Build sets of unique x and y values, and frequency counts for each
     coordinate value.
  2. Sort the unique coordinates to get min/max/second-min/second-max.
  3. Check each of the 4 corners: if there is a cow at (min_x, min_y), remove
     it and recompute area using second-smallest x and/or y.
  4. If a corner has multiple cows on the same edge, removing just the corner
     cow may not change the bounds — use frequency counts to decide.

Note: This is a simplified version that only checks corner removals. The
official solution checks every cow on the boundary (not just corners).

Time Complexity: O(N) to build sets and frequency arrays, O(1) to evaluate.
Space Complexity: O(40001) for frequency arrays.
"""

import sys

sys.stdin = open('reduce.in', 'r')
sys.stdout = open('reduce.out', 'w')

n = int(input())
cows = []                 # list of all cow positions
s_x = set()               # unique x coordinates
s_y = set()               # unique y coordinates
l_x = [0] * 40001         # frequency of each x coordinate
l_y = [0] * 40001         # frequency of each y coordinate

# Read all cows and track coordinate frequencies
for i in range(n):
    x, y = map(int, input().split())
    cows.append([x, y])
    s_x.add(x)
    s_y.add(y)
    l_x[x] += 1
    l_y[y] += 1

# Get sorted unique coordinates
cows_x = list(s_x)
cows_x.sort()
cows_y = list(s_y)
cows_y.sort()

min_area = 40000 * 40000    # upper bound

# --- Case 1: Remove cow at bottom-left corner (min_x, min_y) ---
if [cows_x[0], cows_y[0]] in cows:
    min_area = min(min_area,
                   (cows_x[-1] - cows_x[1]) * (cows_y[-1] - cows_y[1]))
# --- Case 2: Remove cow at top-left corner (min_x, max_y) ---
elif [cows_x[0], cows_y[-1]] in cows:
    min_area = min(min_area,
                   (cows_x[-1] - cows_x[1]) * (cows_y[-2] - cows_y[0]))
# --- No distinct corner cow → check edge frequencies ---
else:
    # If multiple cows share min_x, removing one doesn't change x bounds
    if l_x[cows_x[0]] > 1:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[1]) * (cows_y[-1] - cows_y[0]))

    if l_y[cows_y[0]] > 1:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[1]))

# --- Case 3: Remove cow at top-right corner (max_x, max_y) ---
if [cows_x[-1], cows_y[-1]] in cows:
    min_area = min(min_area,
                   (cows_x[-2] - cows_x[0]) * (cows_y[-2] - cows_y[0]))
# --- Case 4: Remove cow at bottom-right corner (max_x, min_y) ---
elif [cows_x[-1], cows_y[0]] in cows:
    min_area = min(min_area,
                   (cows_x[-2] - cows_x[0]) * (cows_y[-1] - cows_y[1]))
# --- No distinct corner cow → check edge frequencies ---
else:
    if l_x[cows_x[-1]] > 1:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area,
                       (cows_x[-2] - cows_x[0]) * (cows_y[-1] - cows_y[0]))

    if l_y[cows_y[-1]] > 1:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area,
                       (cows_x[-1] - cows_x[0]) * (cows_y[-2] - cows_y[0]))

print(min_area)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# A more robust approach: find the 2 smallest and 2 largest x and y
# coordinates, then try removing EACH cow and see if the bounds change.
# If the removed cow was the sole cow on an edge, use the second-most
# extreme coordinate for that edge.
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
# x = [0] * n
# y = [0] * n
#
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
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
#     x_min = x2 if x[i] == x1 else x1
#     x_max = x3 if x[i] == x4 else x4
#     y_min = y2 if y[i] == y1 else y1
#     y_max = y3 if y[i] == y4 else y4
#     ans = min(ans, (x_max - x_min) * (y_max - y_min))
#
# print(ans)
