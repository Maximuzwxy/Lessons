"""
USACO 2016 December Contest, Bronze - Problem 2: Block Game
==============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=664

Tags: Ad Hoc, String Processing, Brute Force

Problem Description:
-------------------
N boards (1 ≤ N ≤ 100), each with two words (one per side, each ≤ 10 lowercase
letters). When placed on the ground, one word per board is visible — 2^N
possible configurations. FJ wants to make letter blocks so that ALL 2^N
configurations can be spelled using the blocks.

For each letter a–z, determine the minimum number of blocks needed.

Sample Input:              Sample Output (first few lines):
3                          2 (a)
fox box                    2 (b)
dog cat                    2 (c)
car bus                    1 (d)
                           0 (e)
                           ...

Explanation:
  3 boards → 8 possible configurations. E.g. 'fox dog car', 'box cat bus', etc.
  Need max('a' in any config) = 2, max('b' in any config) = 2, etc.


====================================================================
Solution 1: DFS Enumeration of All Configurations (Timeout)
====================================================================
Recursively generate all 2^N combinations of (which side per board), build the
concatenated string for each, count letter frequencies of the whole string,
and track the max frequency per letter across all configurations.

This times out because it explores 2^N cases (N ≤ 100 → up to 2^100 ≈ 10^30).

Time Complexity: O(2^N × total_letters), Space Complexity: O(2^N) recursion depth.
This approach does NOT pass.
"""

# Solution 1 — commented out (timeout)
# import sys
# sys.stdin = open('blocks.in', 'r')
# sys.stdout = open('blocks.out', 'w')
#
# final = [0] * 26
# board = []
#
# n = int(input())
# for i in range(n):
#     board.append(input().split())
#
# def refresh(ss):
#     tmp = [0] * 26
#     for c in ss:
#         index = ord(c) - ord('a')
#         tmp[index] += 1
#     for x in range(26):
#         final[x] = max(final[x], tmp[x])
#
# def get_list(l, d):
#     if d == 0:
#         s = ''
#         for q in range(n):
#             s += board[q][l[q]]
#         refresh(s)
#         l.pop()
#         return
#     for j in range(2):
#         l.append(j)
#         get_list(l, d - 1)
#     if l:
#         l.pop()
#
# get_list([], n)
#
# for _ in final:
#     print(_)


# =====================================================================
# Solution 2: Per-Board Max Direct Accumulation (User's Solution)
# =====================================================================
# Key insight: each board contributes independently. For a given letter, the
# worst-case number of times it appears is the max of its count in word A vs
# word B on that board. Accumulate directly into the answer.
#
#   1. For each board's two words, count letter frequencies separately.
#   2. For each letter, take max(count_in_A, count_in_B) and add directly to
#      the running total.
#
# This avoids enumerating all 2^N combinations.
#
# Time Complexity: O(N), Space Complexity: O(1) beyond input.

import sys

# sys.stdin = open('blocks.in', 'r')
# sys.stdout = open('blocks.out', 'w')

final = [0] * 26    # total blocks needed for each letter
board = []

n = int(input())
for i in range(n):
    board.append(input().split())

for j in range(n):
    # Count frequencies for word A (first side)
    tmp1 = [0] * 26
    for c in board[j][0]:
        index = ord(c) - ord('a')
        tmp1[index] += 1

    # Count frequencies for word B (second side)
    tmp2 = [0] * 26
    for c in board[j][1]:
        index = ord(c) - ord('a')
        tmp2[index] += 1

    # Per-board: take max of the two sides, accumulate directly into final
    for k in range(26):
        final[k] += max(tmp1[k], tmp2[k])

for z in final:
    print(z)


# =====================================================================
# Solution 3: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same algorithm but accumulates directly into the answer array instead of
# building an intermediate 2D array. Processes each board in one pass.
#
# Time Complexity: O(N), Space Complexity: O(1) beyond input.

# import sys
# sys.stdin = open('blocks.in', 'r')
# sys.stdout = open('blocks.out', 'w')
#
# blocks_needed = [0] * 26   # a->0, b->1, ..., z->25
#
# n = int(input())
#
# for _ in range(n):
#     first_word, second_word = input().split()
#
#     # Count letter frequencies for each word
#     first_freq = [0] * 26
#     for ch in first_word:
#         first_freq[ord(ch) - ord('a')] += 1
#
#     second_freq = [0] * 26
#     for ch in second_word:
#         second_freq[ord(ch) - ord('a')] += 1
#
#     # For each letter, take the max of the two words and add to total
#     for j in range(26):
#         blocks_needed[j] += max(first_freq[j], second_freq[j])
#
# for count in blocks_needed:
#     print(count)
