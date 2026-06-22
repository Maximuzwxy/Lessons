"""
USACO 2015 December Contest, Bronze - Problem 1: Fence Painting
https://usaco.org/index.php?page=viewproblem2&cpid=567

Problem Description:
  Farmer John and Bessie each paint a segment of a fence.
  The fence is a 1D number line: John paints [a, b), Bessie paints [c, d).
  The two segments may overlap. Find the total length of fence painted.

  Example: a=7, b=10  means John paints units x=7, 8, 9 (length 3).
           c=4, d=8   means Bessie paints units x=4, 5, 6, 7 (length 4).
           Total coverage: x=4 through x=10, which is 6 units.

Input (paint.in):
  Line 1: a b  (a < b)
  Line 2: c d  (c < d)
  0 ≤ a,b,c,d ≤ 100

Output (paint.out):
  A single integer: total length of fence covered with paint.
"""

import sys

# ============================================================
# Solution 1: Simulation (array marking) — your approach
# Idea: Use a boolean array of length 101 to mark each unit as
#       painted, then count how many units are marked.
# Time: O(max(b, d)), fine since range ≤ 100.
# ============================================================

sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out', 'w')

a, b = map(int, input().split())  # John's interval [a, b)
c, d = map(int, input().split())  # Bessie's interval [c, d)

# paint[i] == 1 means unit [i, i+1) is painted
paint = [0] * 101  # max value of a,b,c,d is 100

for i in range(a, b):  # John's segment, exclusive b (unit is [i, i+1))
    paint[i] = 1

for j in range(c, d):  # Bessie's segment
    paint[j] = 1

print(sum(paint))  # total number of painted units


# ============================================================
# Solution 2: Math (official solution's second method)
# Idea: Classify by overlap, no dependency on interval length.
#       Ensure a ≤ c (swap if needed), then two cases:
#
#   Case 1: c ≥ b  → No overlap
#     Total = (b-a) + (d-c)
#
#   Case 2: c < b  → Overlap
#     - If d > b → covers [a, d), length = d-a
#     - If d ≤ b → covers [a, b), length = b-a  (Bessie is inside John)
#
# Time: O(1)
# ============================================================

def solve_math(a: int, b: int, c: int, d: int) -> int:
    """Math solution (official method 2, O(1))"""
    # Ensure the first interval starts earlier (a ≤ c) for simpler logic
    if c < a:
        a, c = c, a  # swap left endpoints
        b, d = d, b  # swap right endpoints

    if c >= b:
        # Case 1: no overlap, sum both lengths
        return (b - a) + (d - c)
    else:
        # Case 2: overlap, coverage from a to max(b, d)
        if d > b:
            return d - a  # Bessie extends farther
        else:
            return b - a  # John already covers everything


# To use the math solution instead, uncomment below and comment out print(sum(paint)) above
# print(solve_math(a, b, c, d))
