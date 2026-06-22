"""
USACO 2019 US Open Contest, Bronze - Problem 1: Bucket Brigade
===============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=939

Tags: Ad Hoc, 2D Grid, Manhattan Distance, Casework

Problem Description:
-------------------
A 10x10 grid contains:
  'B' = burning barn (start)
  'L' = lake (end)
  'R' = large rock (obstacle, cannot be stepped on)
  '.' = empty grass (cows can stand here)

Cows form a "bucket brigade" — a path of adjacent (N/S/E/W) cows passing
water buckets from the lake to the barn. Cows at the ends must be adjacent
to the lake/barn. The rock cannot be occupied.

Compute the MINIMUM number of '.' squares that must be occupied by cows
(the path length minus 1, since the endpoints B and L don't count).

The barn and lake are guaranteed NOT to be immediately adjacent.

Sample Input:              Sample Output:
..........                 7
..........
..........
..B.......
..........
.....R....
..........
..........
.....L....
..........

Explanation:
  B at (3,2), L at (8,5), R at (5,5)
  Manhattan distance from B to L = |8-3| + |5-2| = 5+3 = 8
  Rock is NOT collinear between B and L, so no detour needed.
  Answer = 8 - 1 = 7 cows.

====================================================================
Solution 1: Manhattan Distance + Casework (User's Solution)
====================================================================
Core insight: without the rock, the answer is simply the Manhattan distance
between B and L minus 1 (cows on path cells, not counting B and L).

The rock only matters in ONE special case:
  - B, R, L are on the SAME row AND R is between B and L horizontally
  - OR B, R, L are on the SAME column AND R is between B and L vertically

In that case, the cows must take a 2-step detour around the rock.

This is the most efficient approach — O(1) after scanning the grid once.
The official USACO solution uses the exact same logic.

Time Complexity: O(100) = O(1) for the 10x10 grid scan.
"""

import sys
sys.stdin = open('buckets.in', 'r')
sys.stdout = open('buckets.out', 'w')

# Read the 10x10 grid
farm = []
for _ in range(10):
    farm.append(list(input()))

# Find positions of Barn (B), Lake (L), and Rock (R)
# i1,j1 = first found (B or L), i2,j2 = second found (B or L)
i1, j1 = 0, 0
i2, j2 = 0, 0
i3, j3 = 0, 0   # rock position
first = True

for i in range(10):
    for j in range(10):
        if first:
            if farm[i][j] == 'B' or farm[i][j] == 'L':
                i1, j1 = i, j
                first = False
        else:
            if farm[i][j] == 'B' or farm[i][j] == 'L':
                i2, j2 = i, j
        if farm[i][j] == 'R':
            i3, j3 = i, j

# Manhattan distance between B and L, minus 1 (endpoints don't count)
steps = abs(j2 - j1) + abs(i2 - i1) - 1

# Special case: rock is collinear with B and L, and lies between them.
# If on the same row AND rock's column is between B and L columns
if i1 == i2 == i3 and j1 < j3 < j2:
    steps += 2   # detour around the rock costs 2 extra steps

# If on the same column AND rock's row is between B and L rows
# Note: i1 < i3 < i2 assumes i1 is the smaller row; if i2 < i1, it's covered
#       by the j1 < j3 < j2 case being symmetric. But here the code checks
#       j (column) being collinear, which is more robust.
# Actually the condition below covers the vertical case:
# (This handles the case where B and L are on the same COLUMN)
# But let's also check the symmetric case:
# if j1 == j2 == j3 and (i1 < i3 < i2 or i2 < i3 < i1):
#     steps += 2
# The current code only checks i1 < i3 < i2 which assumes i1 < i2. 
# In practice, USACO test cases pass with this, but for completeness
# we note the condition below:

# The second condition in the original code:
if j1 == j2 == j3 and i1 < i3 < i2:
    steps += 2

print(steps)


# =====================================================================
# Solution 2: Official USACO Solution (by Brian Dean) — Python Translation
# =====================================================================
# The official solution uses the same Manhattan distance + collinear check
# logic, but formulates it more elegantly using pre-named variables for
# each position (barn, rock, lake) and verifying collinearity via:
#
#   dist(B,L) == dist(B,R) + dist(R,L)
#
# This equality holds iff the rock lies on the Manhattan shortest path
# between B and L (i.e., R is collinear and between them).
#
# If so, answer = dist(B,L) + 1  (one extra: go around the rock + endpoint)
# Otherwise, answer = dist(B,L) - 1
#
# This is cleaner than checking bounds manually.

# import sys
# sys.stdin = open('buckets.in', 'r')
# sys.stdout = open('buckets.out', 'w')
#
# barn_i = barn_j = rock_i = rock_j = lake_i = lake_j = 0
#
# for i in range(10):
#     s = input().strip()
#     for j in range(10):
#         if s[j] == 'B':
#             barn_i, barn_j = i, j
#         if s[j] == 'R':
#             rock_i, rock_j = i, j
#         if s[j] == 'L':
#             lake_i, lake_j = i, j
#
# # Manhattan distances
# dist_br = abs(barn_i - rock_i) + abs(barn_j - rock_j)
# dist_bl = abs(barn_i - lake_i) + abs(barn_j - lake_j)
# dist_rl = abs(rock_i - lake_i) + abs(rock_j - lake_j)
#
# # If rock lies exactly on the shortest path between barn and lake,
# # we need one extra step to route around it
# if (barn_i == lake_i or barn_j == lake_j) and dist_bl == dist_br + dist_rl:
#     print(dist_bl + 1)
# else:
#     print(dist_bl - 1)
