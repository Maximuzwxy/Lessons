"""
USACO 2017 December Contest, Bronze - Problem 2: The Bovine Shuffle
====================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=760

Tags: Simulation

Difficulty: easy

Problem Description:
-------------------
FJ's N cows (1 ≤ N ≤ 100) line up in positions 1..N and perform 3 "shuffles"
in a row. A shuffle is defined by N numbers a₁...a_N: the cow at position i
moves to position a_i. All a_i are distinct (each position gets exactly one cow).

Given the order of cows after 3 shuffles (by their 7-digit IDs), determine
the original order before any shuffling.

Input:  Line 1: N
        Line 2: N integers a₁...a_N (the shuffle pattern)
        Line 3: N integers — cow IDs in order after 3 shuffles
Output: N lines — cow IDs in the original order.

Sample Input:              Sample Output:
5                          1234567
1 3 4 5 2                  5555555
1234567 2222222 3333333    2222222
4444444 5555555            3333333
                           4444444

Explanation:
Shuffle: position 1→1, 2→3, 3→4, 4→5, 5→2 (a cycle).
Tracking a cow from position 2 after 3 shuffles:
  After shuffle: 2→3, then 3→4, then 4→5. So the cow at position 5 after
  3 shuffles (ID 5555555) was originally at position 2.
Reversing 3 shuffles for each position recovers the initial order.

====================================================================
Solution 1: Reverse Shuffle via Index Lookup (User's Solution)
====================================================================
Reverse each shuffle: if cow at position j now came from position i one shuffle
ago (where a_i = j), then shuffle.index(j) finds that i. Repeat 3 times.

Time Complexity: O(N²) — each .index() call is O(N), with N ≤ 100 it's fine.
"""

import sys

sys.stdin = open('shuffle.in', 'r')
sys.stdout = open('shuffle.out', 'w')

n = int(input())
shuffle = [0] + list(map(int, input().split()))    # 1-indexed shuffle pattern
current = ['NA'] + input().split()                  # cow IDs after 3 shuffles

# Reverse 3 shuffles to recover original order
for i in range(3):
    l = [''] * (n + 1)
    for j in shuffle[1:]:                          # j = destination position
        l[shuffle.index(j)] = current[j]           # cow at j came from index(j)
    current = l

for k in range(1, n + 1):
    print(current[k])


# =====================================================================
# Solution 2: Precomputed Inverse Mapping (Official Nick Wu) — Python Translation
# =====================================================================
# Key optimization: precompute an inverse mapping `moveTo` where
#   moveTo[destination] = source (the position the cow came FROM one shuffle ago).
# Then reverse 3 shuffles with O(1) lookup per position instead of O(N).
#
# Time Complexity: O(N)
#
# import sys
#
# sys.stdin = open('shuffle.in', 'r')
# sys.stdout = open('shuffle.out', 'w')
#
# n = int(input())
# a = [0] + list(map(int, input().split()))
# ids = [0] + list(map(int, input().split()))
#
# # Build inverse mapping: moveTo[destination] = source position
# moveTo = [0] * (n + 1)
# for i in range(1, n + 1):
#     moveTo[a[i]] = i
#
# original = [0] * (n + 1)
# for final_pos in range(1, n + 1):
#     cur = final_pos
#     for _ in range(3):
#         cur = moveTo[cur]           # reverse one shuffle
#     original[cur] = ids[final_pos]  # cow at final_pos came from cur
#
# for i in range(1, n + 1):
#     print(original[i])


# =====================================================================
# Solution 3: Reverse via Forward Indexing (Official Brian Dean) — Python Translation
# =====================================================================
# Even simpler: use the original shuffle array directly.
#   original[i] = order[a[i]] means: the cow now at position a[i] was
#   originally at position i one shuffle ago. Apply 3 times.
#
# This is mathematically identical to Solution 1, but expressed using forward
# indexing instead of .index() lookup — avoids the O(N) search.
#
# Comparison:
#   - Solution 1: uses shuffle.index(j) to find inverse each time, O(N²)
#   - Solution 2: precomputes inverse mapping (moveTo), O(N)
#   - Solution 3: applies forward shuffle array to reconstruct backwards, O(N)
#   - All three are reverse-shuffle approaches; 2 & 3 just eliminate .index()
#
# Time Complexity: O(N)
#
# import sys
#
# sys.stdin = open('shuffle.in', 'r')
# sys.stdout = open('shuffle.out', 'w')
#
# n = int(input())
# a = [0] + list(map(int, input().split()))
# order = [0] + list(map(int, input().split()))
#
# for _ in range(3):
#     original = [0] * (n + 1)
#     for i in range(1, n + 1):
#         original[i] = order[a[i]]   # cow at a[i] came from position i
#     order = original
#
# for i in range(1, n + 1):
#     print(order[i])
