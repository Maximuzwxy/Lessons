"""
USACO 2018 January Contest, Bronze - Problem 2: Lifeguards
============================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=784

Tags: Brute Force, Simulation

Difficulty: normal

Problem Description:
-------------------
FJ hires N lifeguards (1 ≤ N ≤ 100), each covering a contiguous time
interval [start, end). The pool is open from t=0 to t=1000. All endpoints
are distinct. Shifts may overlap.

FJ must fire exactly one lifeguard. Find the maximum total time that
can still be covered by the remaining N-1 lifeguards.

Input:  Line 1: N
        Next N lines: start end (integers in [0, 1000], start < end)
Output: A single integer — maximum covered time after firing one lifeguard.

Sample Input:              Sample Output:
3                          7
5 9
1 4
3 7

Explanation:
Fire lifeguard [1,4]: coverage = [3,7] + [5,9] = [3,9] → length 6.
Fire lifeguard [3,7]: coverage = [1,4] + [5,9] = length 7.
Fire lifeguard [5,9]: coverage = [1,4] + [3,7] = length 6.
Max = 7.

====================================================================
Solution 1: Rebuild Coverage Array per Fired Lifeguard (User's Solution)
====================================================================
For each lifeguard i to be fired:
  1. Create a fresh 1001-length boolean array.
  2. Paint all remaining N-1 lifeguards' intervals.
  3. Sum the painted cells.
  4. Track the maximum.

Straightforward "fire one, rebuild" approach. Each iteration rebuilds from
scratch, which is simple but does redundant work.

Time Complexity: O(N² × T) where T = 1000, worst case ~10^7 operations.
"""

import sys

sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

n = int(input())
intervals = []

for i in range(n):
    intervals.append(list(map(int, input().split())))

max_interval = 0

for i in range(n):
    t = [0] * 1001                                 # fresh coverage array
    for begin, end in intervals[:i] + intervals[i + 1:]:
        for j in range(begin, end):
            t[j] = 1                               # mark covered

    max_interval = max(max_interval, sum(t))        # count covered time

print(max_interval)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Smarter approach: precompute a coverage count array ONCE, then for each
# lifeguard temporarily subtract their interval and count >0 cells.
#
# Step 1: numCover[t] = how many lifeguards cover time t.
# Step 2: For each lifeguard i:
#           - Subtract 1 from numCover for their entire interval.
#           - Count how many time points still have numCover[t] > 0.
#           - Add 1 back to restore.
# Step 3: Track the maximum.
#
# Comparison with Solution 1:
#   - Solution 1: rebuilds the entire array from N-1 intervals each time.
#                 O(N) × O(T) × O(N) = O(N²T).
#   - Solution 2: builds once, toggles one interval per iteration.
#                 O(N × T) + O(N × T) = O(N × T). Much faster for larger N.
#   - For N ≤ 100 and T ≤ 1000, both are well within limits.
#
# Time Complexity: O(N × T), Space Complexity: O(T).
#
# import sys
#
# sys.stdin = open('lifeguards.in', 'r')
# sys.stdout = open('lifeguards.out', 'w')
#
# n = int(input())
# start = [0] * n
# end = [0] * n
# for i in range(n):
#     start[i], end[i] = map(int, input().split())
#
# # Step 1: Precompute coverage count for every time point
# numCover = [0] * 1000
# for i in range(n):
#     for t in range(start[i], end[i]):
#         numCover[t] += 1
#
# maxCover = 0
# for i in range(n):
#     # Temporarily fire lifeguard i
#     for t in range(start[i], end[i]):
#         numCover[t] -= 1
#
#     # Count how much time is still covered
#     covered = 0
#     for t in range(1000):
#         if numCover[t] > 0:
#             covered += 1
#     maxCover = max(maxCover, covered)
#
#     # Rehire lifeguard i
#     for t in range(start[i], end[i]):
#         numCover[t] += 1
#
# print(maxCover)
