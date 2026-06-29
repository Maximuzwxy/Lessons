"""
USACO 2018 US Open Contest, Bronze - Problem 2. Milking Order
=============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=832

Tags: Greedy, Simulation, Brute Force

Difficulty: easy

Problem Description:
-------------------
Farmer John's N cows (2 ≤ N ≤ 100), numbered 1…N, have a complex social
structure determining the milking order. Two kinds of constraints exist:

1. Hierarchy: A sequence of M distinct cows (1 ≤ M < N) that must be milked
   in the exact relative order given (e.g., 4,5,6 means cow 4 before cow 5
   before cow 6).
2. Position demands: K cows (1 ≤ K < N) each insist on being milked at a
   specific position (e.g., cow 3 must be at position 1).

Cow 1 is sick — determine the earliest position cow 1 can appear in a valid
milking order satisfying all constraints.

It is guaranteed that at least one valid ordering exists.

Sample Input:              Sample Output:
6 3 2                      4
4 5 6
5 3
3 1

Explanation:
Cow 3 must be position 1, cow 5 must be position 3. Since cow 4 must come
before cow 5 (hierarchy 4,5,6), cow 4 goes to position 2, cow 5 at 3,
and cow 6 at the earliest available position after cow 5. Cow 1 can go at
position 4 at earliest.

====================================================================
Solution 1: Greedy Single-Pass Placement (User's O(N) Solution)
====================================================================
Key insight: Whether cow 1 appears in the hierarchy determines the strategy.

Case 1 (1 in hierarchy): Greedily place the entire hierarchy as early as
possible from left to right. This guarantees cow 1 gets the earliest valid
spot, since squeezing the hierarchy left minimizes everyone's positions.
When encountering a hierarchy cow already fixed at a position, skip it
(its fixed position will be handled naturally when we reach it).

Case 2 (1 not in hierarchy): Greedily place the hierarchy as far right as
possible from right to left. This leaves the earliest free spots available
for cow 1. Then scan left-to-right for the first empty position.

When placing in empty slots, always check that the current hierarchy cow
is not already fixed elsewhere (to avoid ghost duplicates that cause the
algorithm to skip the real fixed cow).

Time Complexity: O(N)
"""

import sys

sys.stdin = open('milkorder.in', 'r')
sys.stdout = open('milkorder.out', 'w')

n, m, k = map(int, input().split())
seq = list(map(int, input().split()))
order = [0] * (n + 1)

for _ in range(k):
    c, p = map(int, input().split())
    order[p] = c

def check_seq(o):
    for a in range(len(seq) - 1):
        if seq[a] in o and seq[a + 1] in o:
            if o.index(seq[a]) > o.index(seq[a + 1]):
                return False

    return True

def check(o):
    cur = 1
    for x in range(len(seq)):
        for y in range(cur, n + 1):
            if o[y] == 0:
                o[y] = seq[x]

                if not check_seq(o):
                    return False
                break
            if o[y] == seq[x]:
                break

    return True

for i in range(1, n + 1):
    if order[i] == 0:
        oo = order.copy()
        oo[i] = 1

        if not check_seq(oo):
            continue

        if check(oo):
            print(oo.index(1))
            break





import sys

sys.stdin = open('milkorder.in', 'r')
sys.stdout = open('milkorder.out', 'w')

n, m, k = map(int, input().split())
seq = list(map(int, input().split()))          # hierarchy sequence (length m)
order = [0] * (n + 1)                          # order[i] = cow at position i, 0 if empty

# Read K fixed-position constraints
for _ in range(k):
    c, p = map(int, input().split())
    order[p] = c

if 1 in seq:
    # --- Case 1: Cow 1 is in the hierarchy ---
    # Place the hierarchy as early as possible (left to right)
    cur_seq = 0
    for i in range(1, n + 1):
        if cur_seq == len(seq):
            break
        if order[i] == seq[cur_seq]:
            cur_seq += 1
        elif order[i] == 0:
            # Don't place a hierarchy cow that's already fixed elsewhere
            if seq[cur_seq] not in order:
                order[i] = seq[cur_seq]
                cur_seq += 1
    # After placing hierarchy, cow 1 is already at its position
    print(order.index(1))
else:
    # --- Case 2: Cow 1 is NOT in the hierarchy ---
    # Place the hierarchy as late as possible (right to left),
    # then cow 1 takes the first available spot.
    cur_seq = 0
    seq.append(1)  # temporarily add cow 1 to the end for placement logic
    for i in range(1, n + 1):
        if cur_seq == len(seq):
            break
        if order[i] == seq[cur_seq]:
            cur_seq += 1
        elif order[i] == 0:
            # Don't place a hierarchy cow that's already fixed elsewhere
            if seq[cur_seq] in order:
                continue
            # If the next cow is fixed right after this slot, don't put current here
            if i < n and cur_seq < len(seq) - 1 and order[i + 1] != seq[cur_seq + 1]:
                continue
            order[i] = seq[cur_seq]
            cur_seq += 1
    # Cow 1 was appended to seq and placed in the first available spot
    print(order[1:].index(0) + 1)

# =====================================================================
# Solution 2: Official USACO Solution (by Dhruv Rohatgi) — Python Translation
# =====================================================================
# Approach: Brute-force the answer. For each possible position i of cow 1,
# add a constraint "cow 1 must be at position i" and check if ALL constraints
# (hierarchy + fixed-positions + cow 1 at i) are satisfiable.
#
# Satisfiability check: Assign fixed-position cows first (reject if conflict).
# Then, for each cow in hierarchy order, greedily assign the earliest free
# position that comes after the previous assigned cow's position.
#
# Time Complexity: O(N × (N + M + K)) = O(N²)
#
# Key difference from Solution 1:
# - O(N²) brute-force with satisfiability check vs. O(N) greedy single-pass
# - More general: can handle any set of constraints, not just the two cases
# - Easier to reason about correctness at the cost of higher complexity
#
# import sys
# sys.stdin = open('milkorder.in', 'r')
# sys.stdout = open('milkorder.out', 'w')
#
# n, m, k = map(int, input().split())
# hierarchy = list(map(int, input().split()))
# for i in range(m):
#     hierarchy[i] -= 1  # convert to 0-indexed
#
# fixed_cow = [0] * (k + 1)  # last entry reserved for cow 1 trial
# fixed_pos = [0] * (k + 1)
#
# for i in range(k):
#     c, p = map(int, input().split())
#     fixed_cow[i] = c - 1
#     fixed_pos[i] = p - 1
#
# def works():
#     """Check if current set of k+1 constraints is satisfiable."""
#     used_cow = [False] * n
#     used_pos = [False] * n
#     pos = [0] * n  # pos[cow] = assigned position
#
#     # Assign fixed-position cows
#     for i in range(k + 1):
#         if used_cow[fixed_cow[i]] and pos[fixed_cow[i]] == fixed_pos[i]:
#             continue
#         if used_cow[fixed_cow[i]] or used_pos[fixed_pos[i]]:
#             return False
#         used_cow[fixed_cow[i]] = True
#         used_pos[fixed_pos[i]] = True
#         pos[fixed_cow[i]] = fixed_pos[i]
#
#     # Greedily place hierarchy cows
#     j = 0  # pointer to next free position
#     for i in range(m):
#         cow = hierarchy[i]
#         if used_cow[cow]:
#             if j > pos[cow]:
#                 return False  # previous cow placed after this one
#             j = pos[cow]
#             continue
#         while used_pos[j]:
#             j += 1
#             if j == n:
#                 return False
#         used_pos[j] = True
#         pos[cow] = j
#
#     return True
#
# # Try each position for cow 1 (0-indexed)
# for i in range(n):
#     fixed_cow[k] = 0       # cow 1 (0-indexed)
#     fixed_pos[k] = i       # try position i
#     if works():
#         print(i + 1)       # convert back to 1-indexed
#         break
