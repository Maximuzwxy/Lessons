"""
USACO 2018 February Contest, Bronze - Problem 3: Taming the Herd
==================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=809

Tags: Ad Hoc, Simulation

Difficulty: hard

Problem Description:
-------------------
FJ logs a counter that indicates days since the last breakout. Some
entries may be -1 (missing). He knows day 1 was a breakout (counter=0).
Determine min and max possible breakouts consistent with the log.

Input:  Line 1: N (1 ≤ N ≤ 100)
        Line 2: N integers — counter values or -1
Output: Two integers — min breakouts, max breakouts. Or -1 if impossible.

Sample Input:              Sample Output:
4                          2 3
-1 -1 -1 1

Explanation:
  Day 1 must be 0 (breakout). Day 4 counter=1 means day 3 was breakout (0).
  Day 2 could be 0 (another breakout, max) or 1 (after day 1 breakout, min).
  So min=2, max=3 breakouts.

====================================================================
Solution 1: Backward Fill + Count (User's Solution)
====================================================================
Scan from right to left: if day i has counter > 0, then day i-1 must
be counter-1. Fill in missing (-1) entries accordingly. Report -1 on
contradiction.

Then day 1 must be 0 (breakout). Count 0s = minimum breakouts.
Count remaining -1s = extra possible breakouts → add to max.

Time Complexity: O(N)
"""

import sys

sys.stdin = open('taming.in', 'r')
sys.stdout = open('taming.out', 'w')

n = int(input())
log = list(map(int, input().split()))

# Edge case: all entries are -1
if log.count(-1) == n:
    print(1, n)
    exit(0)

# Scan backward: propagate counter values
for i in range(n - 1, 0, -1):
    if log[i] > 0:
        pre = log[i] - 1
        if log[i - 1] == -1:
            log[i - 1] = pre
        elif log[i - 1] != pre:
            print(-1)
            exit(0)

# Day 1 must be 0
if log[0] != -1:
    if log[0] > 0:
        print(-1)
        exit(0)
log[0] = 0

# Minimum breakouts = number of 0s in filled log
# Maximum = 0s + remaining -1s (each -1 could be a new breakout)
b = log.count(0)
print(b, b + log.count(-1))


# =====================================================================
# Solution 2: Official USACO Solution (Dhruv Rohatgi) — Python Translation
# =====================================================================
# Same backward-fill approach, but in a single backward pass with a
# running variable t (expected counter value).
#
#   t = -1 initially (not in a streak). Scan from right to left:
#     - If t != -1 and A[i] is not matching → contradiction.
#     - If A[i] != -1, set t = A[i] (enter/update streak).
#     - If A[i] == -1, fill with t.
#     - If A[i] == 0, count as required breakout (req++).
#     - If A[i] still -1 (t was -1), count as optional (pos++).
#     - Decrement t (next day left should be t-1).
#
#   Finally: req = min breakouts, req + pos = max breakouts.
#
# Comparison:
#   - Both are O(N) backward fill. The logic is identical — propagate
#     known counter values backward to infer missing entries.
#   - Solution 1 uses two passes (fill, then count). More explicit
#     step-by-step, easier to follow.
#   - Official Solution 2 does everything in one pass with a running t
#     variable. More compact but slightly more state to track.
#   - The edge case "all -1" is handled differently: Solution 1 has an
#     explicit guard at the start; Official handles it naturally in the
#     single pass.
#
# Time Complexity: O(N)
#
# import sys
#
# sys.stdin = open('taming.in', 'r')
# sys.stdout = open('taming.out', 'w')
#
# n = int(input())
# A = list(map(int, input().split()))
#
# if A[0] > 0:
#     print(-1)
#     exit(0)
# A[0] = 0
#
# t = -1
# req = 0
# pos = 0
# for i in range(n - 1, -1, -1):
#     if t != -1 and A[i] != -1 and A[i] != t:
#         print(-1)
#         exit(0)
#     if t == -1:
#         t = A[i]
#     if A[i] == -1:
#         A[i] = t
#     if A[i] == 0:
#         req += 1
#     if A[i] == -1:
#         pos += 1
#     if t > -1:
#         t -= 1
#
# print(req, req + pos)
