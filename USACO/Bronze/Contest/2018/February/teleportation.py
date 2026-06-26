"""
USACO 2018 February Contest, Bronze - Problem 1: Teleportation
================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=807

Tags: Ad Hoc

Difficulty: very_easy

Problem Description:
-------------------
FJ wants to haul manure from location a to b along a straight road.
He has a teleporter at (x ↔ y): from x can instantly jump to y, or
y to x. Determine the minimum total distance he must haul with his
tractor (can choose not to use the teleporter).

Input:  One line: a b x y (integers 0..100)
Output: Minimum haul distance.

Sample Input:              Sample Output:
3 10 8 2                   3

Explanation:
  Best: haul 3→2 (distance 1), teleport 2→8, haul 8→10 (distance 2).
  Total = 1 + 2 = 3. Direct would be |10-3| = 7.

====================================================================
Solution 1: Min of Distances to Closer Endpoints (User's Solution)
====================================================================
Idea: for the teleporter to help, a must go to one endpoint and b to
the other. So find:
  n = distance from a to the closer teleporter endpoint
  m = distance from b to the closer teleporter endpoint
Then min(direct, n + m) is the answer.

Note: n and m could come from the same endpoint (e.g., x is closer to
both a and b), giving n+m = |a-x|+|b-x|, which is NOT a valid teleporter
path (both go to x, no teleport). However, by the triangle inequality:
  |a-b| ≤ |a-x|+|x-b| = n+m
So whenever n and m come from the same endpoint, the direct path is
already shorter, and min(direct, n+m) = direct, which is correct.

Time Complexity: O(1)
"""

import sys

sys.stdin = open('teleport.in', 'r')
sys.stdout = open('teleport.out', 'w')

a, b, x, y = map(int, input().split())

dis = abs(b - a)

n = min(abs(a - x), abs(a - y))   # closer teleporter to a
m = min(abs(b - x), abs(b - y))   # closer teleporter to b

print(min(dis, n + m))


# =====================================================================
# Solution 2: Official USACO Solution (Brian Dean) — Python Translation
# =====================================================================
# Explicitly enumerates all three options and takes the minimum:
#   1. Direct: |a - b|
#   2. a → x → teleport → y → b: |a-x| + |b-y|
#   3. a → y → teleport → x → b: |a-y| + |b-x|
#
# This is clearer because each option represents an actually valid path.
# No need for the triangle inequality justification — the three cases
# are exhaustive and correct by construction.
#
# Comparison:
#   - Solution 1 collapses the two teleporter paths into n+m by picking
#     the closer endpoint for a and b independently. It's shorter code
#     but the reasoning is less direct: it relies on the triangle
#     inequality to handle the case where both endpoints pick the same
#     side (which gives an invalid path but a value ≥ direct).
#   - Official Solution 2 explicitly writes out the two valid teleporter
#     paths. No subtlety, no invalid paths — just enumerate and min.
#   - For this problem size (O(1) always), both are fine. Solution 2
#     is easier to explain and verify.
#
# Time Complexity: O(1)
#
# import sys
#
# sys.stdin = open('teleport.in', 'r')
# sys.stdout = open('teleport.out', 'w')
#
# a, b, x, y = map(int, input().split())
#
# answer = abs(a - b)                        # no teleporter
# answer = min(answer, abs(a - x) + abs(b - y))  # use x→y
# answer = min(answer, abs(a - y) + abs(b - x))  # use y→x
#
# print(answer)
