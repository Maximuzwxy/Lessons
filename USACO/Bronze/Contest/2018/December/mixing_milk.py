"""
USACO 2018 December Contest, Bronze - Problem 1: Mixing Milk
==============================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=855

Tags: Simulation

Difficulty: very_easy

Problem Description:
-------------------
Three buckets with different capacities and initial amounts of milk.
Pour cyclically: bucket 1 → 2, 2 → 3, 3 → 1, 1 → 2, ... for a total
of 100 pours. Each pour transfers as much milk as possible until either
the source is empty or the destination is full.

Input:  Three lines, each: capacity amount (positive, ≤ 1 billion, capacity ≥ amount)
Output: Three lines — final amount of milk in each bucket.

Sample Input:              Sample Output:
10 3                       0
11 4                       10
12 5                       2

Explanation:
  Initial: 3 4 5
  Pour 1→2: 0 7 5
  Pour 2→3: 0 0 12
  Pour 3→1: 10 0 2
  Pour 1→2: 0 10 2
  Pour 2→3: 0 0 12
  (states repeat every 3 pours after the first few...)

====================================================================
Solution 1: Modulo-based Simulation (User's Solution)
====================================================================
Simulate 100 pours, using i % 3 to determine who pours to whom:
  i % 3 == 1 → pour 0→1,  i % 3 == 2 → pour 1→2,  i % 3 == 0 → pour 2→0

The pour itself is straightforward: if source + dest ≤ dest capacity,
empty source into dest; otherwise fill dest and keep remainder in source.

Time Complexity: O(100) = O(1) — constant number of iterations.
"""

import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

c = [0] * 3
m = [0] * 3

for i in range(3):
    c[i], m[i] = map(int, input().split())

origin = dest = 0

for i in range(1, 101):
    if i % 3 == 1:                  # pour 1→2
        origin = 0
        dest = 1
    elif i % 3 == 2:                # pour 2→3
        origin = 1
        dest = 2
    else:                           # pour 3→1
        origin = 2
        dest = 0

    if m[origin] + m[dest] <= c[dest]:
        m[dest] += m[origin]
        m[origin] = 0
    else:
        m[origin] = m[origin] + m[dest] - c[dest]
        m[dest] = c[dest]

for j in m:
    print(j)


# =====================================================================
# Solution 2: Official USACO Solution (Travis Hance) — Python Translation
# =====================================================================
# Recognizes the cyclic pattern: 100 pours = 33 full cycles of (1→2, 2→3, 3→1)
# + 1 extra pour (1→2). Loops 33 times executing all 3 pours per iteration,
# then does the final 1→2 pour separately.
#
# Uses a clean pour() helper that computes:
#   amt = min(source_amount, dest_capacity - dest_amount)
#   source_amount -= amt
#   dest_amount += amt
#
# This is functionally identical to Solution 1's if/else but more concise.
#
# Comparison:
#   - Both simulate the same 100 pours. No algorithmic difference.
#   - Solution 1 uses modulo on the pour number (i % 3) to decide the
#     direction per iteration. It's 100 iterations with a branch each.
#   - Solution 2 uses the cyclic pattern to batch 3 pours per loop
#     iteration (33 loops), then adds the final pour. Slightly fewer
#     loop iterations and no modulo/branching inside the loop body.
#   - Solution 2's pour() helper with min() is cleaner than the if/else
#     — it directly expresses "pour as much as possible" as min().
#   - Both are O(1) — 100 pours is trivial.
#
# Time Complexity: O(1)
#
# import sys
#
# sys.stdin = open('mixmilk.in', 'r')
# sys.stdout = open('mixmilk.out', 'w')
#
#
# def pour(c1, m1, c2, m2):
#     """Pour from bucket 1 into bucket 2, return new (m1, m2)."""
#     amt = min(m1, c2 - m2)
#     return m1 - amt, m2 + amt
#
#
# c1, m1 = map(int, input().split())
# c2, m2 = map(int, input().split())
# c3, m3 = map(int, input().split())
#
# for i in range(33):
#     m1, m2 = pour(c1, m1, c2, m2)   # 1 → 2
#     m2, m3 = pour(c2, m2, c3, m3)   # 2 → 3
#     m3, m1 = pour(c3, m3, c1, m1)   # 3 → 1
#
# m1, m2 = pour(c1, m1, c2, m2)       # 100th pour: 1 → 2
#
# print(f'{m1}\n{m2}\n{m3}')
