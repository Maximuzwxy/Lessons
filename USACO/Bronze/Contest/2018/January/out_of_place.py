"""
USACO 2018 January Contest, Bronze - Problem 3: Out of Place
==============================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=785

Tags: Sorting, Greedy

Difficulty: normal

Problem Description:
-------------------
Cows are lined up from shortest to tallest. Bessie steps out of line
and re-inserts herself at some other position. Given the resulting
lineup, find the minimum number of swaps to re-sort the cows. Swaps
can be between any two cows (not just adjacent).

Input:  Line 1: N (2 ≤ N ≤ 100)
        Next N lines: cow heights (1..1,000,000, duplicates possible)
Output: A single integer — minimum swaps needed.

Sample Input:              Sample Output:
6                          3
2
4
7
7
9
3

Explanation:
  Original (sorted): [2, 3, 4, 7, 7, 9]
  After Bessie (3) re-inserts at end: [2, 4, 7, 7, 9, 3]
  3 swaps needed: 9↔3, 7↔3, 4↔3 → sorted.

====================================================================
Solution 1: Simulate Swapping Bessie Back (User's Solution)
====================================================================
First identify Bessie — the cow that is out of place. Scan the line
to find the first position i where line[i] > line[i+1]. If i==0, Bessie
is at index 0 and needs to move right. Otherwise, compare line[i-1]
with line[i+1] to determine if Bessie is at i (too tall) or i+1 (too short).

Then simulate swapping Bessie step-by-step back to her correct position,
counting each swap. When there are duplicate heights, skip over equal
adjacent cows (swapping two identical heights doesn't progress anything).

Time Complexity: O(N²) — each swap may traverse the array.
#
# import sys
#
# sys.stdin = open('outofplace.in', 'r')
# sys.stdout = open('outofplace.out', 'w')
#
# n = int(input())
# line = []
#
# for i in range(n):
#     line.append(int(input()))
# bessie = 0
#
# left = True
# for i in range(n - 1):
#     if line[i] > line[i + 1]:
#         if i == 0:
#             bessie = 0
#             left = False
#         else:
#             if line[i - 1] < line[i + 1]:
#                 bessie = i
#                 left = False
#             else:
#                 bessie = i + 1
#         break
#
# cnt = 0
# if left:
#     for j in range(bessie, -1, -1):
#         target = j - 1
#         if line[target] > line[bessie]:
#             if line[target] == line[target - 1]:
#                 continue
#             line[bessie], line[target] = line[target], line[bessie]
#             bessie = target
#             cnt += 1
#         else:
#             break
# else:
#     for j in range(bessie, n - 1):
#         target = j + 1
#         if line[target] < line[bessie]:
#             if line[target] == line[target + 1]:
#                 continue
#             line[bessie], line[target] = line[target], line[bessie]
#             bessie = target
#             cnt += 1
#         else:
#             break
#
# print(cnt)


# =====================================================================
# Solution 2: Sorted Copy + Mismatch Range (User's Solution)
# =====================================================================
# Key insight: sort a copy of the line, then find the first and last
# positions where the original differs from sorted. These define the
# misaligned range.
#
#   swaps = (end - start) - (adjacent duplicates in range)
#
# Why subtract adjacent duplicates? If two adjacent cows are the same
# height, they are indistinguishable — swapping them doesn't count as
# a real fix. So each pair of adjacent equal cows in the original
# misaligned range reduces the swap count by 1.
#
# Time Complexity: O(N log N) for sorting.
"""

import sys

sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

n = int(input())
line = []

for i in range(n):
    line.append(int(input()))

new_line = sorted(line)

start = -1
end = -1

for i in range(n):
    if line[i] != new_line[i]:
        start = i
        break

for i in range(n - 1, -1, -1):
    if line[i] != new_line[i]:
        end = i
        break

cnt = end - start

for i in range(start, end):
    if line[i] == line[i + 1]:
        cnt -= 1

print(cnt)


# =====================================================================
# Solution 3: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Also sorts a copy and compares. The insight: if K positions differ
# between original and sorted, it takes K-1 swaps to fix them.
# Each swap fixes at most one element's position (the last swap fixes
# two). Duplicate heights are handled naturally — if two positions
# have the same value (e.g., two 7s), and one matches sorted while
# the other doesn't, only the mismatched one counts.
#
#   swaps = max(0, count_of_mismatches - 1)
#
# Comparison of Solution 2 vs Solution 3:
#   - Both sort a copy and compare with the original. Core idea is same.
#   - Solution 2 finds the first and last mismatch, computes the span,
#     then explicitly subtracts adjacent duplicate pairs. More explicit
#     about how duplicates reduce the answer.
#   - Official Solution 3 counts ALL mismatched positions globally, then
#     subtracts 1. More mathematically elegant — "K-1 swaps for K wrong
#     positions." Duplicates are handled automatically: when sorted[i]
#     equals line[i] (both 7s match), no mismatch is counted.
#   - Solution 2 could potentially miscount if there are gaps in the
#     mismatch range (but given the problem guarantee of "one cow out of
#     place," the mismatches form a contiguous block).
#   - Solution 3 is shorter, cleaner, and the standard approach.
#
# Time Complexity: O(N log N) for sorting.
#
# import sys
#
# sys.stdin = open('outofplace.in', 'r')
# sys.stdout = open('outofplace.out', 'w')
#
# n = int(input())
# height = [int(input()) for _ in range(n)]
# sorted_height = sorted(height)
#
# swaps = -1
# for i in range(n):
#     if sorted_height[i] != height[i]:
#         swaps += 1
#
# swaps = max(0, swaps)
# print(swaps)
