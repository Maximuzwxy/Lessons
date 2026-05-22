# =============================================================================
# USACO 2016 February Contest, Bronze
# Problem 1. Milk Pails
# https://usaco.org/index.php?page=viewproblem2&cpid=615
# =============================================================================

# [Problem Summary]
# Farmer John needs to fill an order of exactly M units of milk.
# He has two pails of sizes X and Y (X < Y < M).
# He can fill each pail any number of times and pour into the M pail,
# as long as it doesn't overflow.
# Find the maximum amount of milk he can add to the M pail.

# [Input Format]
#   - Single line: X, Y, M (1 ≤ X < Y < M ≤ 1000)

# [Output Format]
#   - Maximum milk that can be added to the M pail (without exceeding M)

# [Sample]
#   Input:  17 25 77
#   Output: 76  (3 × 17 + 1 × 25 = 76)

# [Approach]
# This is a bounded knapsack problem variant.
# We need to find non-negative integers i, j such that:
#   X * i + Y * j ≤ M
# and X * i + Y * j is maximized.

# Solution 1: Brute Force Enumeration
#   Try all combinations of i (0 to m//x) and j (0 to m//y)
#   Time: O((m/x) * (m/y)) ≈ O(m^2)

# Solution 2: Dynamic Programming (DP = Dynamic Programming) on Reachable States
#   Use boolean array to mark all achievable milk amounts
#   Iterate from 0 to M, if state i is reachable, mark i+x and i+y as reachable
#   Time: O(m), Space: O(m)

# =============================================================================
# Solution 1: Brute Force Enumeration
# Time: O(m^2), Space: O(1)
# =============================================================================
# import sys
# sys.stdin = open('pails.in', 'r')
# sys.stdout = open('pails.out', 'w')

# x, y, m = map(int, input().split())

# a = m // x  # maximum times we can use pail X
# b = m // y  # maximum times we can use pail Y

# max_v = 0

# for i in range(0, a + 1):
#     for j in range(0, b + 1):
#         p = x * i + y * j  # total milk from using i of X and j of Y
#         if p <= m:
#             max_v = max(max_v, p)

# # Optimization: for each i, compute max j directly (O(n) instead of O(n^2))
# # for i in range(0, a + 1):
# #     j = (m - x * i) // y  # maximum j such that x*i + y*j <= m
# #     max_v = max(max_v, x * i + y * j)

# print(max_v)

# =============================================================================
# Solution 2: DP (Dynamic Programming) on Reachable States
# Time: O(m), Space: O(m)
#
# Algorithm:
#   1. Create boolean array `pail` of size m+1, mark pail[0] = True (empty state)
#   2. Iterate i from 0 to m: if pail[i] is True, then i+x and i+y are reachable
#   3. Track maximum reachable value during iteration
#
# This is DP because we process states in topological order (0 to m).
# Since all transitions add positive values (x, y), smaller states are always
# processed before larger ones, ensuring correctness.
# =============================================================================
import sys
sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

x, y, m = map(int, input().split())

pail = [False] * (m + 1)
pail[0] = True  # starting state: 0 milk in the pail
max_v = 0

for i in range(m + 1):
    if pail[i]:
        # from state i, we can reach i+x and i+y
        if i + x <= m:
            pail[i + x] = True
        if i + y <= m:
            pail[i + y] = True
        # update maximum reachable value
        max_v = max(max_v, i)

print(max_v)