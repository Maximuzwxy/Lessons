# =============================================================================
# USACO 2020 February Contest, Bronze
# Problem 1. Triangles
# https://usaco.org/index.php?page=viewproblem2&cpid=1011
# =============================================================================

"""
【Problem Description】
- There are N fence posts at distinct points (X_i, Y_i)
- Choose 3 posts to form a triangle where:
  - One side is parallel to the x-axis
  - Another side is parallel to the y-axis
- Find the maximum area of such a triangle

【Input】
- First line: N (3 ≤ N ≤ 100)
- Next N lines: X_i, Y_i (-10^4 ≤ X_i, Y_i ≤ 10^4)

【Output】
- 2 × maximum area (to avoid fractions)
- It's guaranteed at least one valid triangle exists

【Example】
Input:
4
0 0
0 1
1 0
1 2
Output:
2

Explanation:
- Triangle (0,0), (1,0), (1,2) has area = 1
- Output is 2 × 1 = 2

【Solution】
Key Insight: For a triangle with one side parallel to x-axis and another to y-axis,
two of the three vertices must share the same x-coordinate, and two must share
the same y-coordinate.

The area formula for such a triangle:
- area = |x_diff| × |y_diff| / 2
- where x_diff is the distance between two points with same y
- and y_diff is the distance between two points with same x

Algorithm:
- Enumerate all triples of points
- For each triple, find which pair shares x and which shares y
- Calculate area = |x1 - x2| × |y1 - y2| / 2
- Keep track of maximum area

Time: O(N^3)   Space: O(N)
- There are O(N^3) triples to check
- Each check is O(1)
- With N ≤ 100, this is fast enough
"""

from itertools import combinations
import sys
sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')

n = int(input())
posts = []
triangles = []

for _ in range(n):
    posts.append(list(map(int, input().split())))

# Generate all possible triangles (combinations of 3 points)
triangles = combinations(posts, 3)

def get_area(a, b, c):
    """
    Calculate area of triangle where one side is horizontal, one is vertical.
    The triangle's base is horizontal (same y) and height is vertical (same x).
    """
    x = y = 0

    # Find the horizontal distance (two points with same y-coordinate)
    if a[1] == b[1]:
        x = abs(a[0] - b[0])
    elif a[1] == c[1]:
        x = abs(a[0] - c[0])
    elif b[1] == c[1]:
        x = abs(b[0] - c[0])

    # Find the vertical distance (two points with same x-coordinate)
    if a[0] == b[0]:
        y = abs(a[1] - b[1])
    elif a[0] == c[0]:
        y = abs(a[1] - c[1])
    elif b[0] == c[0]:
        y = abs(b[1] - c[1])

    # Area = base × height / 2, but we return 2 × area (to avoid fractions)
    return x * y

max_area = 0

# Check each triangle and keep track of maximum (2 × area)
for i, j, k in triangles:
    max_area = max(max_area, get_area(i, j, k))

print(max_area)