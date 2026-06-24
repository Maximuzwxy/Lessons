"""
USACO 2017 January Contest, Bronze - Problem 3: Cow Tipping
===========================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=689

Tags: Greedy, 2D Grid

Difficulty: normal

Problem Description:
-------------------
FJ's N × N cows (1 ≤ N ≤ 10) start in a grid. Some are tipped over (1) and
some are upright (0). He has a machine that can flip (toggle) all cows in any
"upper-left rectangle" — a rectangle whose top-left corner is (0, 0).

Toggling turns 0 → 1 and 1 → 0. Find the minimum number of toggles needed to
make all cows upright (all 0s).

Note: toggling the same rectangle twice is pointless (undoes itself).

Input:  Line 1: N
        Next N lines: string of N characters each, 0 or 1
Output: A single integer — minimum number of toggles.

Sample Input:              Sample Output:
3                          2
001
111
111

Explanation:
Toggle entire grid (upper-left rect covering all) → becomes:
  110
  000
  000
Then toggle the upper-left 1×2 rect containing the two 1s → all 0s.
Total: 2 toggles.

====================================================================
Solution 1: Greedy from Bottom-Right (User's Solution)
====================================================================
Key insight: the cell at (N-1, N-1) can only be toggled by the full-grid
rectangle. If it's 1, we must toggle it. After fixing the bottom-right, the
cell to its left can now only be toggled by one rectangle, and so on.

Process from bottom row to top, right to left within each row. Whenever a cell
is 1, toggle the upper-left rectangle ending at that cell. This is guaranteed
to be optimal because each decision is forced (the current cell can only be
affected by rectangles whose bottom-right corner is at or below-right of it,
and we've already fixed all cells below-right).

Time Complexity: O(N^4) — each toggle flips up to N^2 cells, and we may toggle
up to N^2 times. For N ≤ 10 this is at most 10,000 operations, well within limits.
"""

import sys

sys.stdin = open('cowtip.in', 'r')
sys.stdout = open('cowtip.out', 'w')

n = int(input())
cows = []

for i in range(n):
    cows.append(list(map(int, list(input()))))


def toggle(a, b):
    """Toggle all cells in the upper-left rectangle (0..a-1, 0..b-1)."""
    for x in range(a):
        for y in range(b):
            if cows[x][y] == 0:
                cows[x][y] = 1
            else:
                cows[x][y] = 0

cnt = 0
# Process from bottom-right to top-left
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if cows[i][j] == 1:              # must toggle this cell back to 0
            toggle(i + 1, j + 1)         # toggle rectangle (0,0) to (i,j)
            cnt += 1

print(cnt)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Identical algorithm: scan from bottom-right to top-left, toggle the
# upper-left rectangle whenever a 1 is found.
#
# The only difference from Solution 1 is implementation style — the official
# solution uses char comparison ('1'/'0') and toggles in-place with a
# double-nested loop. The core greedy logic is exactly the same.
#
# Time Complexity: O(N^4)
#
# import sys
#
# sys.stdin = open('cowtip.in', 'r')
# sys.stdout = open('cowtip.out', 'w')
#
# n = int(input())
# grid = [list(input().strip()) for _ in range(n)]
#
# numTips = 0
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         if grid[i][j] == '1':
#             numTips += 1
#             # Toggle the upper-left rectangle ending at (i, j)
#             for a in range(i + 1):
#                 for b in range(j + 1):
#                     if grid[a][b] == '1':
#                         grid[a][b] = '0'
#                     else:
#                         grid[a][b] = '1'
#
# print(numTips)
