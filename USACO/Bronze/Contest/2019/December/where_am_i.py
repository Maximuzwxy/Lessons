"""
USACO 2019 December Contest, Bronze - Problem 2. Where Am I?
=============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=964

Tags: Brute Force, String, Set

Difficulty: easy

Problem Description:
-------------------
There are N farms (1 ≤ N ≤ 100) in a row, each with a colorful mailbox labeled
by a letter A..Z. The sequence of mailboxes forms a string of length N.
Farmer John wants to find the smallest K such that every consecutive sequence
of K mailboxes uniquely identifies a position along the road.

In other words: find the smallest K where all substrings of length K in the
string are distinct.

Sample Input:              Sample Output:
7                          4
ABCDABC

Explanation:
For K=3, substring "ABC" appears at positions 1 and 5 → not unique.
For K=4, all length-4 substrings ("ABCD", "BCDA", "CDAB", "DABC") are unique.
Answer is 4.

====================================================================
Solution 1: Sliding Window with Custom Count Function
====================================================================
Iterate K from 1 to N. For each K, check all substrings of length K.
Use a custom `my_count()` function that counts how many times a substring
appears by repeatedly searching and slicing from the remaining string.
If any substring count > 1, K is invalid → skip to next K.
The first valid K is the answer.

Time Complexity: O(N³) — N values of K × O(N) substrings × O(N) counting per
substring via slicing.
"""

import sys

sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')

n = int(input())
mailbox = input()


def my_count(whole, sub):
    """Count occurrences of `sub` in `whole`, allowing overlapping matches."""
    cnt = 0
    tmp = whole
    while sub in tmp:
        cnt += 1
        idx = tmp.index(sub)          # find first occurrence
        tmp = tmp[idx + 1:]           # slice past it and continue searching
    return cnt


def find_k():
    """Find the smallest K where all substrings of length K are unique."""
    for i in range(n):                      # i+1 = current K being tested
        for j in range(0, n - i):           # starting positions for length i+1
            s = mailbox[j:j + i + 1]        # substring of length i+1
            if my_count(mailbox, s) > 1:    # appears more than once?
                break                        # → this K fails
        else:                                # inner loop completed without break
            return i + 1                     # → all substrings unique, found answer
    return 0


print(find_k())


# =====================================================================
# Solution 2: Official USACO Solution (Set-based, by Brian Dean) — Python Translation
# =====================================================================
# Approach: For each K from 1 to N, use a set to check if all substrings of
# length K are distinct. A set cannot store duplicates, so if a substring
# is already in the set before inserting, K is invalid.
#
# Time Complexity: O(N²) — N values of K × O(N) substrings per K × O(1) set ops.
#
# Key differences from Solution 1:
# - Uses Python `set` for O(1) duplicate detection vs. O(N) slicing count
# - The custom count function in Solution 1 does repeated slicing which is
#   O(N) per call, making it O(N³) overall. The set approach is O(N²).
# - Otherwise the logic is identical: brute-force K from 1 upward, first valid
#   K is the answer.
#
# import sys
# sys.stdin = open('whereami.in', 'r')
# sys.stdout = open('whereami.out', 'w')
#
# n = int(input())
# s = input()
#
# for k in range(1, n + 1):
#     seen = set()
#     ok = True
#     for i in range(n - k + 1):
#         sub = s[i:i + k]
#         if sub in seen:
#             ok = False
#             break
#         seen.add(sub)
#     if ok:
#         print(k)
#         break
