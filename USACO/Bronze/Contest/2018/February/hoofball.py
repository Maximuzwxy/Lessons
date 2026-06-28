"""
USACO 2018 February Contest, Bronze - Problem 2: Hoofball
============================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=808

Tags: Graph, Greedy, Simulation

Difficulty: very_hard

Problem Description:
-------------------
N cows stand at distinct positions along a line. When a cow receives a
ball, she passes it to her nearest neighbor (left tiebreaker). FJ wants
every cow to hold the ball at least once. Find the minimum number of
initial balls needed.

Input:  Line 1: N (1 ≤ N ≤ 100)
        Line 2: N distinct positions xi (1 ≤ xi ≤ 1000)
Output: A single integer — minimum initial balls.

Sample Input:              Sample Output:
5                          2
7 1 3 11 4

Explanation:
  Sorted: [1, 3, 4, 7, 11]
  Pass to nearest: 1→3, 3→4, 4→3, 7→4, 11→7
  Two balls: one at 1 (covers 1→3↔4), one at 11 (covers 11→7→4→3↔4).
  No single starting cow covers all.

====================================================================
Solution 1: Greedy by Nearest-Neighbor Distance (User's Solution)
====================================================================
Idea: cows with a large nearest-neighbor distance are "isolated" — nobody
will pass to them. So always pick the unvisited cow with the largest
nearest-neighbor gap as the next starting point.

  1. Compute diff[i] = distance to nearest neighbor for each cow.
  2. While not all cows visited:
       - Among unvisited cows, pick the one with largest diff.
       - Simulate ball passing from that cow until a cycle is hit.
  3. Count = number of times we picked a starting cow.

This is a greedy constructive approach. It avoids the full DFS search
(which would be 2^N worst case) by a useful observation: outlier cows
need their own ball because nobody near them will pass to them.

Time Complexity: O(N²) — each ball simulates at most N passes.
"""

import sys

sys.stdin = open('hoofball.in', 'r')
sys.stdout = open('hoofball.out', 'w')

n = int(input())
line = list(map(int, input().split()))
line.sort()
hold = [0] * n

# Precompute nearest-neighbor distance for each cow
diff = []
for i in range(n):
    if i == 0:
        diff.append(line[1] - line[0])
    elif i == n - 1:
        diff.append(line[n - 1] - line[n - 2])
    else:
        diff.append(min(line[i + 1] - line[i], line[i] - line[i - 1]))

def kick(l, start):
    """Simulate ball from cow 'start'. Mark visited cows in l[]. Returns 1."""
    p = start

    while True:
        l[p] = 1

        if p == 0:                    # leftmost cow
            if l[1] == 1:
                break
            else:
                p += 1
        elif p == n - 1:              # rightmost cow
            if l[p - 1] == 1:
                break
            else:
                p -= 1
        else:                         # middle: pass to nearer neighbor
            if line[p + 1] - line[p] < line[p] - line[p - 1]:
                p += 1
            else:
                p -= 1

            if l[p] == 1:             # cycle detected — stop
                break

    return 1

cnt = 0
while sum(hold) != n:
    a = 0
    index = -1
    for i in range(n):
        if hold[i] == 0:
            if diff[i] >= a:
                a = diff[i]
                index = i

    cnt += kick(hold, index)

print(cnt)


# =====================================================================
# Solution 2: DFS Exhaustive Search (User's — Too Slow, Preserved)
# =====================================================================
# Recursively tries every possible starting cow combination to find the
# minimum number of balls. Each recursion picks an unvisited cow, kicks
# from there, and recurses. Exponential: ~2^N worst case. For N=100,
# this is infeasible — kept for reference only.
#
# Time Complexity: O(2^N) — exponential, too slow for N > ~20.
#
# n = int(input())
# line = list(map(int, input().split()))
# line.sort()
# hold = [0] * n
#
# def kick(l, start):
#     p = start
#     while True:
#         l[p] = 1
#         if p == 0:
#             if l[1] == 1:
#                 break
#             else:
#                 p += 1
#         elif p == n - 1:
#             if l[p - 1] == 1:
#                 break
#             else:
#                 p -= 1
#         else:
#             if line[p + 1] - line[p] < line[p] - line[p - 1]:
#                 p += 1
#             else:
#                 p -= 1
#             if l[p] == 1:
#                 break
#     return 1
#
# cnt = 100
# def dfs(h, count):
#     global cnt
#     if count >= cnt:
#         return
#     if sum(h) == n:
#         cnt = min(cnt, count)
#         return
#     for j in range(n):
#         if h[j] == 0:
#             hh = h.copy()
#             kick(hh, j)
#             dfs(hh, count + 1)
#
# dfs(hold, 0)
# print(cnt)


# =====================================================================
# Solution 3: Official USACO Solution (Brian Dean) — Python Translation
# =====================================================================
# Elegant in-degree approach:
#   1. For each cow i, compute target(i) — the cow she passes to.
#   2. Count passto[i] = number of cows that pass to cow i (in-degree).
#   3. Answer = count of cows with passto[i] == 0
#             + count of isolated 2-cycles (i↔j, both passto[i]=passto[j]=1).
#
# Rationale:
#   - A cow with passto=0 is a "source" — nobody passes to her, so she
#     MUST receive an initial ball from FJ.
#   - A pair of adjacent cows passing only to each other (cycle of 2)
#     that no one else passes to also needs its own ball, because no
#     ball from outside can reach it.
#   - All other cows will be reached when balls reach a cycle or from
#     a source flowing through them.
#
# Comparison:
#   - Solution 1 (greedy by gap): picks the most isolated cow first,
#     simulates the entire path, repeats. Intuitive — "start from
#     outliers." O(N²) with simulation.
#   - Official Solution 3: pure in-degree analysis, no simulation.
#     Counts how many sources + isolated pairs. O(N²) but much simpler
#     code. The key insight: a ball can only start at a source or in
#     an isolated 2-cycle. Everything else is reached transitively.
#   - The user's greedy approach is equivalent in result — picking by
#     largest gap ends up picking exactly the sources and isolated
#     pairs, just in a different order. Both are correct.
#
# Time Complexity: O(N²) for computing targets.
#
# import sys
#
# sys.stdin = open('hoofball.in', 'r')
# sys.stdout = open('hoofball.out', 'w')
#
# n = int(input())
# x = list(map(int, input().split()))
# x.sort()
#
# passto = [0] * n
#
# # Compute target for each cow
# target = [0] * n
# for i in range(n):
#     left_nbr, left_dist = -1, 1000
#     right_nbr, right_dist = -1, 1000
#     for j in range(n):
#         if x[j] < x[i] and x[i] - x[j] < left_dist:
#             left_nbr = j
#             left_dist = x[i] - x[j]
#         if x[j] > x[i] and x[j] - x[i] < right_dist:
#             right_nbr = j
#             right_dist = x[j] - x[i]
#     if left_dist <= right_dist:
#         target[i] = left_nbr
#     else:
#         target[i] = right_nbr
#
# # Count in-degrees
# for i in range(n):
#     passto[target[i]] += 1
#
# answer = 0
# for i in range(n):
#     if passto[i] == 0:
#         answer += 1
#     if (i < target[i]
#             and target[target[i]] == i
#             and passto[i] == 1
#             and passto[target[i]] == 1):
#         answer += 1
#
# print(answer)
