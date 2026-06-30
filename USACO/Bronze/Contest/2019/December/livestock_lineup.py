"""
USACO 2019 December Contest, Bronze - Problem 3. Livestock Lineup
==================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=965

Tags: Brute Force, Ad Hoc

Difficulty: easy

Problem Description:
-------------------
There are exactly 8 cows: Bessie, Buttercup, Belinda, Beatrice, Bella, Blue,
Betsy, and Sue. Given N constraints (1 ≤ N ≤ 7) of the form "X must be milked
beside Y" (meaning X must appear directly before or after Y in the order),
find a valid milking order.

If multiple orderings satisfy all constraints, output the alphabetically
earliest one (lexicographically smallest).

It is guaranteed that at least one valid ordering exists.

Sample Input:                     Sample Output:
3                                  Beatrice
Buttercup must be milked beside    Sue
Bella                              Belinda
Blue must be milked beside Bella   Bessie
Sue must be milked beside Beatrice Betsy
                                   Blue
                                   Bella
                                   Buttercup

Explanation:
There are multiple valid orderings (e.g., Beatrice→Sue→Belinda→...) and
the alphabetically earliest is the one starting with Beatrice.

====================================================================
Solution 1: Brute Force All Permutations (8! = 40,320)
====================================================================
Generate all 8! = 40,320 permutations of the 8 cow names using
itertools.permutations. Since the cows list is already sorted
alphabetically, the permutations will be generated in lexicographic order.

For each permutation, check if all constraints are satisfied: for each pair
(X, Y) that must be beside each other, their positions in the current
ordering must differ by exactly 1 (abs(index(X) - index(Y)) == 1).

Since the permutations are generated in order, the first valid one is
guaranteed to be alphabetically earliest.

Time Complexity: O(8! × N) ≈ 40,320 × 7 ≈ 280,000 — trivial for N=7.
"""

import sys
from itertools import permutations

sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

n = int(input())
beside = []  # list of (cow1, cow2) pairs that must be adjacent

# Parse constraints: "X must be milked beside Y" → first word and last word
for _ in range(n):
    l = input().split()
    beside.append([l[0], l[-1]])

# 8 cows sorted alphabetically → permutations will be in lexicographic order
cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
cows.sort()

p = list(permutations(cows, 8))


def check(s, b):
    """Check if ordering `s` satisfies all beside constraints in `b`."""
    for x, y in b:
        if abs(s.index(x) - s.index(y)) != 1:
            return False   # x and y must be adjacent in the ordering
    return True


def lineup():
    """Return the first valid permutation (alphabetically earliest)."""
    for line in p:
        if check(line, beside):
            return line
    return []


for i in lineup():
    print(i)


# =====================================================================
# Solution 2: Analytic Construction One Cow at a Time (Official Method 2)
# =====================================================================
# Approach: Build the ordering cow by cow. At each step, ask: "Which cow
# can legally go next?" A cow can go first if:
#   - It hasn't been placed yet
#   - It has AT MOST one unplaced neighbor (if it has 2, one must come first)
#   - If there is already a cow at the end of the line that MUST be beside
#     another specific cow, then that specific cow MUST go next (forced).
#
# Algorithm:
# 1. Loop 8 times to determine the next cow to place.
# 2. `can_go_first(c)`: checks if cow c can legally be the next one placed.
#    - If c already placed → no
#    - If c has 2 unplaced neighbors → no (one must precede it)
#    - If the last-placed cow is forced to be beside a specific unplaced cow
#      that is NOT c → no (forced adjacency overrides alphabetic order)
# 3. Try cows in alphabetic order, pick first that passes.
#
# Time Complexity: O(N × 8) = O(56), but requires careful reasoning.
#
# Key differences from Solution 1:
# - Solution 1: enumerate ALL 40,320 permutations, check each — simple
#   but brute-force. Official solution 1 (next_permutation) is identical.
# - Solution 2: analytically construct the answer one cow at a time without
#   generating all permutations. More efficient but harder to implement.
#
# import sys
# sys.stdin = open('lineup.in', 'r')
# sys.stdout = open('lineup.out', 'w')
#
# n = int(input())
# beside_a = []  # first cow of each constraint pair
# beside_b = []  # second cow of each constraint pair
#
# for _ in range(n):
#     l = input().split()
#     beside_a.append(l[0])
#     beside_b.append(l[-1])
#
# cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
# cows.sort()  # already sorted, but explicit
# answer = []
#
#
# def where(c):
#     """Return index of cow c in answer, or large number if not placed."""
#     for i in range(len(answer)):
#         if answer[i] == c:
#             return i
#     return 999
#
#
# def can_go_first(c):
#     """Check if cow c can be the next cow in the ordering."""
#     if where(c) != 999:
#         return False  # already placed
#
#     # Count unplaced neighbors
#     nbrs = 0
#     for i in range(n):
#         if beside_a[i] == c and where(beside_b[i]) == 999:
#             nbrs += 1
#         if beside_b[i] == c and where(beside_a[i]) == 999:
#             nbrs += 1
#
#     # If cow must be beside 2 unplaced cows, it can't be at either end
#     if nbrs == 2:
#         return False
#
#     # If there's already a last cow, check if it forces a specific next cow
#     if len(answer) > 0:
#         last_cow = answer[-1]
#         for i in range(n):
#             # last cow is forced to be beside some unplaced cow that isn't c
#             if beside_a[i] == last_cow and where(beside_b[i]) == 999 and beside_b[i] != c:
#                 return False
#             if beside_b[i] == last_cow and where(beside_a[i]) == 999 and beside_a[i] != c:
#                 return False
#
#     return True
#
#
# # Build ordering one by one
# for i in range(8):
#     next_cow = 0
#     while not can_go_first(cows[next_cow]):
#         next_cow += 1
#     answer.append(cows[next_cow])
#     print(cows[next_cow])
