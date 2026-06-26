"""
USACO 2018 December Contest, Bronze - Problem 3: Back and Forth
=================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=857

Tags: Brute Force, DFS, Recursion

Difficulty: hard

Problem Description:
-------------------
Two barns, each starting with 1000 gallons of milk and 10 buckets
(sizes 1..100). FJ carries milk back and forth 4 times:

  Tuesday:   pick a bucket from barn 1, fill, pour into barn 2,
             leave bucket at barn 2.
  Wednesday: pick a bucket from barn 2, fill, pour into barn 1,
             leave bucket at barn 1.
  Thursday:  pick a bucket from barn 1, fill, pour into barn 2,
             leave bucket at barn 2.
  Friday:    pick a bucket from barn 2, fill, pour into barn 1,
             leave bucket at barn 1.

After Friday, measure milk in barn 1. How many possible different
readings could there be?

Input:  Line 1: 10 integers — bucket sizes initially at barn 1
        Line 2: 10 integers — bucket sizes initially at barn 2
Output: A single integer — number of distinct possible final readings.

Sample Input:              Sample Output:
1 1 1 1 1 1 1 1 1 2        5
5 5 5 5 5 5 5 5 5 5

Explanation:
  Net change to barn1 = (Wed bucket + Fri bucket) - (Tue bucket + Thu bucket).
  Start at 1000, try all possible bucket choices across 4 days.
  Resulting possible final amounts: 1000, 1003, 1004, 1007, 1008 → 5 values.

====================================================================
Solution 1: Generic DFS with List Swap (User's Solution)
====================================================================
A single recursive DFS function that explores all 4 days. The key trick:
swap the two barn lists on each recursive call — l1 is always the source
barn, l2 is always the destination. So the same function handles all 4
days without distinguishing them.

  1. Pick each bucket from l1 (source), remove it, add to l2 (dest).
  2. Recurse with swapped l1, l2 (next day, roles reverse).
  3. After 4 picks, record the sequence.
  4. After DFS, compute net change for each sequence:
     net = (Wed + Fri) - (Tue + Thu)
  5. Count unique change values → distinct final readings.

Upper bound: 10 × 11⁴ ≈ 146,410 paths, well within limits.

Time Complexity: O(choices) ≈ 10 × 11^4, very fast.
"""

import sys

sys.stdin = open('backforth.in', 'r')
sys.stdout = open('backforth.out', 'w')

b1 = list(map(int, input().split()))
b2 = list(map(int, input().split()))

res = []
def bf(l1, l2, b):
    """DFS: l1=source barn, l2=dest barn, b=chosen buckets so far."""
    if len(b) == 4:
        res.append(b.copy())
        return

    for i in range(len(l1)):
        s1 = l1.copy()
        s2 = l2.copy()
        t = s1.pop(i)           # take bucket t from source barn
        b.append(t)
        s2.append(t)            # leave it at destination barn
        bf(s2, s1, b)           # next day: swap source/dest roles
        b.pop()

bf(b1, b2, [])

s = set()
for l in res:
    # Net change in barn 1 = (Wed + Fri) - (Tue + Thu)
    s.add(l[1] + l[3] - l[0] - l[2])

print(len(s))


# =====================================================================
# Solution 2: Official USACO Solution (Brian Dean) — Python Translation
# =====================================================================
# Models each day as a separate named function (tuesday, wednesday,
# thursday, friday), matching the problem structure literally.
# The final function (friday) records the possible ending amount
# in a boolean array indexed by total milk in barn 1 (0..2000).
#
# This is more verbose but mirrors the problem description exactly,
# making it easy to read and debug day-by-day.
#
# Time Complexity: O(choices), same as Solution 1.
#
# import sys
#
# sys.stdin = open('backforth.in', 'r')
# sys.stdout = open('backforth.out', 'w')
#
# possible_answers = [0] * 2000
#
#
# def friday(b1milk, B1, B2):
#     """Friday: pick bucket from B2, pour into B1, record result."""
#     for i in range(len(B2)):
#         x = B2[i]
#         possible_answers[b1milk + x] = 1
#
#
# def thursday(b1milk, B1, B2):
#     """Thursday: pick bucket from B1, pour into B2."""
#     for i in range(len(B1)):
#         x = B1[i]
#         new_B2 = B2 + [x]
#         new_B1 = B1[:i] + B1[i+1:]
#         friday(b1milk - x, new_B1, new_B2)
#
#
# def wednesday(b1milk, B1, B2):
#     """Wednesday: pick bucket from B2, pour into B1."""
#     for i in range(len(B2)):
#         x = B2[i]
#         new_B1 = B1 + [x]
#         new_B2 = B2[:i] + B2[i+1:]
#         thursday(b1milk + x, new_B1, new_B2)
#
#
# def tuesday(b1milk, B1, B2):
#     """Tuesday: pick bucket from B1, pour into B2."""
#     for i in range(len(B1)):
#         x = B1[i]
#         new_B2 = B2 + [x]
#         new_B1 = B1[:i] + B1[i+1:]
#         wednesday(b1milk - x, new_B1, new_B2)
#
#
# B1 = list(map(int, input().split()))
# B2 = list(map(int, input().split()))
#
# tuesday(1000, B1, B2)
#
# print(sum(possible_answers))


# =====================================================================
# Solution 3: Official USACO Solution (Dhruv Rohatgi) — Python Translation
# =====================================================================
# Generic DFS with a day parameter (2..6, representing Tue..Fri).
# Uses a boolean array pos[] to track possible final amounts.
# The direction (add or subtract from barn 1) depends on whether
# day is even (Tue/Thu: take from barn 1) or odd (Wed/Fri: take from
# barn 2).
#
# Comparison of all three:
#   - Solution 1: single generic DFS + swap trick. Shortest, cleverest,
#                 but the swap-and-record-then-compute pattern is
#                 slightly indirect.
#   - Solution 2: 4 named functions matching the problem structure.
#                 Most readable for beginners — each day is a function.
#                 Records the FINAL milk amount directly (no post-
#                 processing needed).
#   - Solution 3: generic DFS with day parameter. Mid-level abstraction.
#                 Uses multiset-like array manipulation.
#   - All three search the same space (~146K paths). The differences
#     are purely stylistic.
#   - Solution 1 is the most Pythonic (swap + set comprehension).
#   - Solution 2 is the most literal (each day = one function).
#
# Time Complexity: O(choices), same as Solution 1.
#
# import sys
#
# sys.stdin = open('backforth.in', 'r')
# sys.stdout = open('backforth.out', 'w')
#
# S = [list(map(int, input().split())), list(map(int, input().split()))]
# pos = [0] * 2001
# num_outcomes = 0
#
#
# def dfs(day, amount):
#     """
#     day: 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=done.
#     amount: milk in barn 1 (barn 2 = 2000 - amount).
#     """
#     global num_outcomes
#     if day == 6:
#         num_outcomes += 1 - pos[amount]
#         pos[amount] = 1
#         return
#     p = day % 2               # 0 for Tue/Thu (take from barn 0),
#                                # 1 for Wed/Fri (take from barn 1)
#     for i in range(len(S[p])):
#         v = S[p][i]
#         S[p].pop(i)
#         S[1-p].append(v)     # move bucket to other barn
#         if p == 0:
#             dfs(day + 1, amount - v)   # taking from barn 1 → lose v
#         else:
#             dfs(day + 1, amount + v)   # taking from barn 2 → gain v
#         S[1-p].pop()          # undo: remove from other barn
#         S[p].insert(i, v)
#
#
# dfs(2, 1000)
# print(num_outcomes)
