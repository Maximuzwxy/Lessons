"""
USACO 2018 December Contest, Bronze - Problem 2: The Bucket List
==================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=856

Tags: Simulation

Difficulty: very_easy

Problem Description:
-------------------
FJ has N cows (1 ≤ N ≤ 100). Cow i needs milking from time si to ti
and requires bi buckets during that interval. Buckets are
interchangeable but cannot be shared simultaneously. All si and ti are
distinct (no two events at the same time). Determine the minimum number
of buckets needed.

Input:  Line 1: N
        Next N lines: si ti bi (1 ≤ si, ti ≤ 1000, 1 ≤ bi ≤ 10)
Output: A single integer — total buckets needed.

Sample Input:              Sample Output:
3                          4
4 10 1
8 13 3
2 6 2

Explanation:
  t=2: cow 3 starts, needs 2 buckets → 2 in use
  t=4: cow 1 starts, needs 1 bucket → 3 in use
  t=6: cow 3 ends, releases 2 buckets → 1 in use
  t=8: cow 2 starts, needs 3 buckets (only 1 free → need new) → 4 in use
  Peak = 4 buckets needed.

====================================================================
Solution 1: Timeline Accumulation (User's Solution)
====================================================================
Create a time_line array of size 1001 (times 1 to 1000). For each cow,
add bi to every time point from si to ti (inclusive). The answer is the
maximum value in the array — the peak concurrent bucket usage.

Sorting by start time is not strictly needed (timeline accumulation is
order-independent), but harmless.

Time Complexity: O(N × T) where T = 1000, about 10^5 operations.
"""

import sys

sys.stdin = open('blist.in', 'r')
sys.stdout = open('blist.out', 'w')

n = int(input())
lines = []
time_line = [0] * 1001

for i in range(n):
    lines.append(list(map(int, input().split())))

lines.sort(key=lambda x: x[0])

for s, t, b in lines:
    for i in range(s, t + 1):
        time_line[i] += b

print(max(time_line))


# =====================================================================
# Solution 2: Official Solution #1 — Naive Per-Time Scan (Nathan Pinsker)
# =====================================================================
# For each time point 1..1000, iterate all cows and sum the buckets of
# those covering this time. Take max.
#
# Time Complexity: O(N × T) — same class as Solution 1, just loops
#                  swapped (time outer, cows inner).
#
# import sys
#
# sys.stdin = open('blist.in', 'r')
# sys.stdout = open('blist.out', 'w')
#
# n = int(input())
# S = [0] * n
# T = [0] * n
# B = [0] * n
# for i in range(n):
#     S[i], T[i], B[i] = map(int, input().split())
#
# max_buckets = 0
# for time in range(1, 1001):
#     buckets_at_time = 0
#     for i in range(n):
#         if S[i] <= time <= T[i]:
#             buckets_at_time += B[i]
#     max_buckets = max(max_buckets, buckets_at_time)
#
# print(max_buckets)


# =====================================================================
# Solution 3: Official Solution #2 — Sweep Line (Brian Dean)
# =====================================================================
# More efficient: only process start and end events. Uses two arrays
# start[t] and finish[t] to record which cow starts/ends at time t.
# Sweeps through times 1..1000:
#   - At start[t], add that cow's buckets
#   - Update max
#   - At finish[t], subtract that cow's buckets
#
# Still O(N + T) because the arrays are indexed directly by time (no
# sorting needed since times ≤ 1000).
#
# Comparison:
#   - Solution 1: accumulate per-cow ranges onto timeline, one pass.
#                 Intuitive — "paint the usage over time."
#   - Solution 2: for each time, ask "which cows are active?" Reversed
#                 perspective from Solution 1.
#   - Solution 3: event-based sweep. Only touches start/end times
#                 rather than all T points × N cows. If T were large
#                 (e.g., 10^9), this would be O(N log N) with sorting.
#   - For N=100, T=1000, all three are instant. Solution 3 is the
#     scalable approach.
#
# Time Complexity: O(N + T)
#
# import sys
#
# sys.stdin = open('blist.in', 'r')
# sys.stdout = open('blist.out', 'w')
#
# n = int(input())
# S = [0] * (n + 1)
# T = [0] * (n + 1)
# B = [0] * (n + 1)
# start = [0] * 1001
# finish = [0] * 1001
#
# for i in range(1, n + 1):
#     S[i], T[i], B[i] = map(int, input().split())
#     start[S[i]] = i
#     finish[T[i]] = i
#
# buckets_needed = 0
# b = 0
# for t in range(1, 1001):
#     if start[t]:
#         b += B[start[t]]
#     buckets_needed = max(buckets_needed, b)
#     if finish[t]:
#         b -= B[finish[t]]
#
# print(buckets_needed)
