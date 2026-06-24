"""
USACO 2017 February Contest, Bronze - Problem 2: Why Did the Cow Cross the Road II
==================================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=712

Tags: Simulation

Difficulty: normal

Problem Description:
-------------------
FJ's farm has a circular road. 26 cows (A-Z) cross the road twice a day
— once into the field (entry) and once out (exit). Each cow enters and exits
at different points, and all 52 crossing points are distinct.

FJ walks clockwise around the circle and records the cow name at each crossing
point, producing a 52-character string where every letter A-Z appears exactly
twice. He does not record which points are entries and which are exits.

A pair of cows (a, b) is called a "crossing pair" if the path of cow a from
entry to exit must intersect the path of cow b from entry to exit (i.e., the
line segments connecting each cow's two points would cross inside the circle).

Given the 52-character string, count the total number of crossing pairs.

Input:  A single line containing a 52-character string of uppercase letters
        A-Z, each appearing exactly twice.
Output: A single integer — the number of crossing pairs.

Sample Input:              Sample Output:
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
                          1

Explanation:
Only cows A and B are a crossing pair: A appears at positions 1 and 4,
B at positions 2 and 5 → ABAB pattern, the paths cross.

====================================================================
Solution 1: Stack + Counter (User's Solution)
====================================================================
Scan the string left to right, maintaining a stack of "active" cows (cows
whose first occurrence has been seen but second not yet closed). When a cow's
second occurrence is found, count how many other cows between its two
occurrences appear exactly once (these are cows that cross with it).

The stack naturally removes adjacent pairs (AA) which cannot cross with
anything. Each crossing pair is counted twice (once from each cow's
perspective), so divide by 2 at the end.

Time Complexity: O(52 * N) ≈ O(26 * 52) = constant
"""

import sys
from collections import Counter

sys.stdin = open('circlecross.in', 'r')
sys.stdout = open('circlecross.out', 'w')

s = input()
stack = []
cnt = 0


def check_cross(cow):
    """Count how many cows between the two occurrences of `cow` appear
    exactly once (i.e., their two occurrences straddle `cow`'s interval)."""
    index_in = stack.index(cow)
    index_out = stack.index(cow, index_in + 1)

    d = Counter(stack[index_in + 1:index_out])
    num = 0
    for k, v in d.items():
        if v == 1:                     # appears exactly once → crosses
            num += 1
    return num


for c in s:
    if stack:
        if stack[-1] == c:             # adjacent pair, no crossing possible
            stack.pop()
        else:
            if c not in stack:
                stack.append(c)         # first occurrence
            else:
                stack.append(c)         # second occurrence (not adjacent)
                cnt += check_cross(c)   # count cows that cross with c
    else:
        stack.append(c)

print(cnt // 2)                         # each pair counted twice


# =====================================================================
# Solution 2: Brute Force over All Cow Pairs (User's Solution)
# =====================================================================
# Enumerate all C(26,2) = 325 unordered pairs of cows. For each pair, find
# their two occurrences in the string. The pair crosses if their indices are
# interleaved in an ABAB or BABA pattern:
#   A ... B ... A ... B   or   B ... A ... B ... A
#
# This is the most direct brute-force approach: check every pair explicitly.
#
# Time Complexity: O(26^2 * 52) = O(1) (constant, at most ~35000 operations)
#
# import sys
# sys.stdin = open('circlecross.in', 'r')
# sys.stdout = open('circlecross.out', 'w')
#
# cross = list(input())
# cows = [chr(ord('A') + i) for i in range(26)]
# cnt = 0
#
# for i in range(26):
#     for j in range(i + 1, 26):
#         index_i = [k for k in range(len(cross)) if cross[k] == cows[i]]
#         index_j = [k for k in range(len(cross)) if cross[k] == cows[j]]
#
#         if index_i[0] < index_j[0] < index_i[1] < index_j[1] \
#                 or index_j[0] < index_i[0] < index_j[1] < index_i[1]:
#             cnt += 1
#
# print(cnt)


# =====================================================================
# Solution 3: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Key insight: Two paths cross iff travelling around the circle, the letters
# alternate — ABAB or BABA. Non-crossing patterns are AABB, ABBA, BAAB, BBAA.
#
# The official approach: for each cow, find its first and last occurrence
# in the string, then count how many *other* cows appear exactly once between
# those two positions. A single appearance inside the interval means the other
# cow's two occurrences straddle this interval → they cross.
#
# Note: The official solution only considers cows with ID greater than the
# current one (to avoid double-counting), so no need to divide by 2.
#
# Comparison:
#   - Solution 1: stack-based, counts singles inside each interval, divides by 2
#   - Solution 2: checks ABAB/BABA pattern directly for every pair
#   - Solution 3: same idea as Solution 1 but cleaner — no stack, direct
#     first/last lookup, avoids double-counting by restricting to higher IDs
#
# Time Complexity: O(26 * 52) = O(1)
#
# import sys
#
# sys.stdin = open('circlecross.in', 'r')
# sys.stdout = open('circlecross.out', 'w')
#
# crosses = input()
# # Convert string to array of integers (A=0, B=1, ..., Z=25)
# crossArray = [ord(c) - ord('A') for c in crosses]
#
# numPairs = 0
#
# for i in range(26):
#     # Find first and last occurrence of cow i
#     first = crossArray.index(i)
#     last = len(crossArray) - 1 - crossArray[::-1].index(i)
#
#     # Count how many cows with ID > i appear exactly once in (first, last)
#     appearances = [0] * 26
#     for k in range(first + 1, last):
#         appearances[crossArray[k]] += 1
#
#     for j in range(i + 1, 26):
#         if appearances[j] == 1:       # exactly one occurrence → crosses
#             numPairs += 1
#
# print(numPairs)
