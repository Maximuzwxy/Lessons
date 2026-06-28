"""
USACO 2023 February Contest, Bronze - Problem 3: Watching Mooloo
==================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=1301

Tags: Greedy

Difficulty: easy

Problem Description:
-------------------
Bessie wants to watch Mooloo on N specific days (sorted). Each
subscription costs d + K moonies to cover d consecutive days. She can
start as many subscriptions as needed. Find the minimum total cost.

Key insight: for the first watched day, a subscription is unavoidable
(cost = 1 + K for a 1-day sub to start). For each subsequent day:
  - Extend current subscription: cost = gap (days between current and
    previous day). E.g., if days are 1 and 5, extending costs 4 (days
    2,3,4,5 — wait, no: to cover day 5 from a sub that already covers
    day 1, you need d=5 days, so the INCREMENTAL cost over covering
    just day 1 is 4 extra days = gap).
  - Or start a new subscription: cost = 1 + K (1 day + base fee).

Pick the cheaper for each gap: min(gap, 1 + K).

Since all gaps are evaluated independently, the greedy choice is optimal.

Input:  Line 1: N K (1 ≤ N ≤ 10^5, 1 ≤ K ≤ 10^9)
        Line 2: N integers d1 < d2 < ... < dN (1 ≤ di ≤ 10^14)
Output: Minimum total moonies.

Sample Input:              Sample Output:
2 4                        7
7 9

Explanation: gap = 9-7=2 ≤ 1+K=5 → extend. d=3, cost=3+4=7.

Sample Input:              Sample Output:
2 3                        8
1 10

Explanation: gap = 10-1=9 > 1+K=4 → new sub. Two 1-day subs: 4+4=8.

====================================================================
Solution 1: Greedy Gap Comparison (Correct Approach)
====================================================================
For each adjacent pair of watched days, compare the gap with 1+K:
  - If gap ≤ 1+K → extend the current subscription (cheaper than a new K).
  - If gap > 1+K → start a new subscription.
The answer = first segment cost (1+K) + sum of min(gap, 1+K) for each gap.

Time Complexity: O(N)
"""

import sys

# sys.stdin = open('', 'r')   # stdin/stdout — no file I/O for this problem
# sys.stdout = open('', 'w')

n, k = map(int, input().split())
days = list(map(int, input().split()))

start = 0
spend = 0

for i in range(n - 1):
    if days[i + 1] - days[i] > k + 1:
        spend += days[i] - days[start] + 1 + k
        start = i + 1

spend += days[n - 1] - days[start] + 1 + k

print(spend)


# =====================================================================
# Solution 2: Even Simpler Gap Summation (Equivalent)
# =====================================================================
# The same greedy logic in a more concise form: first subscription always
# costs 1+K, then for each gap, add min(gap, 1+K). This directly models
# the "extend or start new" decision per gap without tracking segments.
#
# time Complexity: O(N)
#
# import sys
#
# n, k = map(int, input().split())
# days = list(map(int, input().split()))
#
# ans = 1 + k
# for i in range(n - 1):
#     gap = days[i + 1] - days[i]
#     ans += min(gap, 1 + k)
#
# print(ans)


# =====================================================================
# Wrong Solution (Preserved for Reference)
# =====================================================================
# This approach incorrectly checks total span from segment start instead
# of adjacent gap. Bug: if total span > K+1 but each individual gap is
# ≤ K+1, it wrongly splits the segment, overcounting K.
#
# n, k = map(int, input().split())
# days = list(map(int, input().split()))
#
# start = cur = 0
# spend = 0
#
# while True:
#     cur += 1
#     if cur == n:
#         spend += days[cur - 1] - days[start] + 1 + k
#         start = cur
#         break
#     if days[cur] - days[start] <= k + 1:
#         continue
#     else:
#         spend += days[cur - 1] - days[start] + 1 + k
#         start = cur
#
# print(spend)
