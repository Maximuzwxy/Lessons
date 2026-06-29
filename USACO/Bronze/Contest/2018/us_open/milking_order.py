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
Solution 1: Enumerate + Greedy Validate (Inspired by Official Solution)
====================================================================
Idea: Enumerate cow 1's position from 1 to N. For each candidate position,
add it as a fixed constraint and greedily validate whether the remaining
hierarchy cows can be legally placed.

- check_seq(o): Verify that for every adjacent pair (a, b) in the hierarchy
  that are both present in o, a's position < b's position.
- check(o): Greedily place each hierarchy cow from left to right. Maintain
  a cursor `cur` so that each cow is placed after the previous one. If a
  cow is already fixed at some position, skip empty slots until reaching it.

Time Complexity: O(N × (N + M × N)) = O(N² × M), which is fine for N,M ≤ 100.
"""

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


def check_seq(o):
    """
    Check if all hierarchy pairs already in `o` satisfy the relative order.
    For each adjacent pair (seq[a], seq[a+1]) that both appear in o:
        position of seq[a] must be < position of seq[a+1].
    """
    for a in range(len(seq) - 1):
        if seq[a] in o and seq[a + 1] in o:
            if o.index(seq[a]) > o.index(seq[a + 1]):
                return False
    return True


def check(o):
    """
    Greedily place hierarchy cows into `o` left-to-right.
    Returns True if a valid placement exists, False otherwise.

    For each cow in seq order:
      - If it already has a fixed position >= cur, skip to that position.
      - If it already has a fixed position < cur, impossible → return False.
      - Otherwise, try each empty slot >= cur. Place there only if the cow
        is not fixed elsewhere (avoids ghost duplicates), and check_seq
        passes. If the current slot fails, undo and try the next one.
    """
    cur = 1  # next hierarchy cow must be placed at or after this position
    for x in range(len(seq)):
        cow = seq[x]
        placed = False
        for y in range(cur, n + 1):
            if o[y] == cow:
                # Cow already fixed here → advance cursor past it
                cur = y + 1
                placed = True
                break
            if o[y] == 0:
                # Empty slot — only place if this cow isn't fixed elsewhere
                if cow in o:
                    continue
                o[y] = cow
                if check_seq(o):
                    cur = y + 1
                    placed = True
                    break
                else:
                    o[y] = 0  # undo and try next position
        if not placed:
            return False
    return True


# Try each possible position for cow 1 (1-indexed)
for i in range(1, n + 1):
    if order[i] == 0:
        oo = order.copy()
        oo[i] = 1

        # Quick check: do the fixed cows + cow 1 already violate hierarchy?
        if not check_seq(oo):
            continue

        if check(oo):
            print(oo.index(1))
            break


# =====================================================================
# Solution 2: Greedy Single-Pass Placement (User's O(N) Solution)
# =====================================================================
# Key insight: Whether cow 1 appears in the hierarchy determines the strategy.
#
# Case 1 (1 in hierarchy): Greedily place the entire hierarchy as early as
# possible from left to right. This guarantees cow 1 gets the earliest valid
# spot, since squeezing the hierarchy left minimizes everyone's positions.
#
# Case 2 (1 not in hierarchy): Greedily place the hierarchy as far right as
# possible. This leaves the earliest free spots available for cow 1.
#
# When placing in empty slots, always check that the current hierarchy cow
# is not already fixed elsewhere (to avoid ghost duplicates).
#
# Time Complexity: O(N)
#
# Key difference from Solution 1:
# - Solution 1: O(N²M) enumeration + validation, easy to prove correct
# - Solution 2: O(N) single pass with case analysis, faster but needs
#   more careful reasoning to prove optimality
#
# import sys
# sys.stdin = open('milkorder.in', 'r')
# sys.stdout = open('milkorder.out', 'w')
#
# n, m, k = map(int, input().split())
# seq = list(map(int, input().split()))
# order = [0] * (n + 1)
#
# for _ in range(k):
#     c, p = map(int, input().split())
#     order[p] = c
#
# if 1 in seq:
#     cur_seq = 0
#     for i in range(1, n + 1):
#         if cur_seq == len(seq):
#             break
#         if order[i] == seq[cur_seq]:
#             cur_seq += 1
#         elif order[i] == 0:
#             if seq[cur_seq] not in order:
#                 order[i] = seq[cur_seq]
#                 cur_seq += 1
#     print(order.index(1))
# else:
#     cur_seq = 0
#     seq.append(1)
#     for i in range(1, n + 1):
#         if cur_seq == len(seq):
#             break
#         if order[i] == seq[cur_seq]:
#             cur_seq += 1
#         elif order[i] == 0:
#             if seq[cur_seq] in order:
#                 continue
#             if i < n and cur_seq < len(seq) - 1 and order[i + 1] != seq[cur_seq + 1]:
#                 continue
#             order[i] = seq[cur_seq]
#             cur_seq += 1
#     print(order[1:].index(0) + 1)
#
#
# =====================================================================
# Solution 3: Official USACO Solution (by Dhruv Rohatgi) — Python Translation
# =====================================================================
# Approach: Brute-force cow 1's position from 1 to N. For each trial,
# call `works()` to check if all constraints (K fixed + hierarchy + cow1
# at trial position) are simultaneously satisfiable.
#
# `works()` works in two steps:
#   1. Assign all fixed-position cows. Reject if a cow is assigned to two
#      different positions, or a position is assigned to two different cows.
#   2. Greedily place hierarchy cows left-to-right: maintain a pointer `j`
#      to the earliest available position. For each hierarchy cow, either
#      skip to its fixed position (reject if it's behind `j`), or place it
#      at the first free position after `j`.
#
# Time Complexity: O(N × (N + M + K)) = O(N²)
#
# Key difference from Solution 1 & 2:
# - Uses 0-indexed arrays with separate tracking (used_cow, used_pos)
# - No `check_seq` needed — correctness is structural
# - The standard reference solution for this problem
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
#
# def works():
#     """Check if current set of k+1 constraints is satisfiable."""
#     used_cow = [False] * n
#     used_pos = [False] * n
#     pos = [0] * n  # pos[cow] = assigned position
#
#     # Step 1: Assign fixed-position cows
#     for i in range(k + 1):
#         if used_cow[fixed_cow[i]] and pos[fixed_cow[i]] == fixed_pos[i]:
#             continue            # same cow, same position — duplicate, skip
#         if used_cow[fixed_cow[i]] or used_pos[fixed_pos[i]]:
#             return False        # conflict: cow reused or position reused
#         used_cow[fixed_cow[i]] = True
#         used_pos[fixed_pos[i]] = True
#         pos[fixed_cow[i]] = fixed_pos[i]
#
#     # Step 2: Greedily place hierarchy cows left-to-right
#     j = 0  # earliest position the next hierarchy cow can take
#     for i in range(m):
#         cow = hierarchy[i]
#         if used_cow[cow]:
#             # Cow already has a fixed position
#             if j > pos[cow]:
#                 return False    # previous cow ended up after this one
#             j = pos[cow]
#             continue
#         # Cow has no fixed position — find first free slot >= j
#         while used_pos[j]:
#             j += 1
#             if j == n:
#                 return False    # ran out of positions
#         used_pos[j] = True
#         pos[cow] = j
#
#     return True
#
#
# # Try each position for cow 1 (0-indexed)
# for i in range(n):
#     fixed_cow[k] = 0       # cow 1 is 0 in 0-indexed
#     fixed_pos[k] = i       # try position i
#     if works():
#         print(i + 1)       # convert back to 1-indexed
#         break
