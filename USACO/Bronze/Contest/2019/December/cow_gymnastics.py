"""
USACO 2019 December Contest, Bronze - Problem 1. Cow Gymnastics
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=963

Tags: Brute Force

Difficulty: easy

Problem Description:
-------------------
K practice sessions (1 ≤ K ≤ 10), N cows (1 ≤ N ≤ 20). Each session ranks
the N cows in some order (cow numbers 1..N). A pair (A, B) is "consistent"
if cow A appears before cow B in all K sessions.

Find the total number of consistent ordered pairs.

Sample Input:            Sample Output:
3 4                      4
4 1 2 3
4 1 3 2
4 2 1 3

Explanation:
Consistent pairs: (1,4)、(2,4)、(3,4)、(1,3)
E.g., (1,4): 1 is before 4 in all 3 sessions → consistent.

====================================================================
Solution 1: Check All N×(N-1) Ordered Pairs via itertools
====================================================================
Generate all N×(N-1) ordered pairs using permutations(range(1, N+1), 2).
For each pair (i, j), check if it appears in every session's unordered
combinations. If (i, j) is in combinations(session, 2), it means i came
before j in that session. If true for all K sessions → count.

Time: O(N² × K × N) ≈ 400 × 10 × 20 = 80,000. Fine for N=20, K=10.
"""

import sys
from itertools import permutations, combinations

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
sessions = []
for _ in range(k):
    sessions.append(list(map(int, input().split())))

# All N×(N-1) ordered pairs (i, j) with i != j
per = list(permutations(range(1, n + 1), 2))

# Convert each session's ranking into a set of (A before B) combinations
pairs = [list(combinations(s, 2)) for s in sessions]

# Check each ordered pair: must be present in all sessions' combinations
num = 0
for c in per:
    flag = True
    for p in pairs:
        if c not in p:    # (i, j) not in session → i was not before j
            flag = False
            break
    if flag:
        num += 1

print(num)


# =====================================================================
# Solution 2: Only Check Pairs from the First Session
# =====================================================================
# Key optimization: if a pair doesn't appear in the right order in the
# FIRST session, it cannot possibly appear correctly in ALL sessions.
# So we only need to check the ~N²/2 unordered pairs from session 1,
# instead of all N×(N-1) ordered pairs.
#
# An unordered pair (a, b) from session 1 already tells us the only
# possible consistent ordering: a before b (since that's true in session 1,
# and to be consistent it must be true in all sessions).
#
# Time: same worst-case but about 2x faster. Still O(N² × K).
#
# import sys
# from itertools import combinations
# sys.stdin = open('gymnastics.in', 'r')
# sys.stdout = open('gymnastics.out', 'w')
#
# k, n = map(int, input().split())
# sessions = [list(map(int, input().split())) for _ in range(k)]
#
# # Extract unordered combinations from all sessions
# pairs = [list(combinations(s, 2)) for s in sessions]
#
# num = 0
# for c in pairs[0]:       # only pairs from FIRST session
#     ret = True
#     for p in pairs:
#         if c not in p:
#             ret = False
#             break
#     if ret:
#         num += 1
# print(num)


# =====================================================================
# Solution 3: Official USACO Solution — Compare Positions in Each Session
# =====================================================================
# Approach: Store all rankings in a 2D array data[K][N]. For each ordered
# pair (a, b), scan every session to find their positions. If a's position
# < b's position in all K sessions, count it.
#
# Better(a, b, session): find index of a and b in that session's ranking,
# return True if apos < bpos.
# Nbetter(a, b): call Better for all K sessions, return count of sessions
# where a is ahead. If count == K → consistent pair.
#
# Time: O(N² × K × N) — same as Solution 1 in complexity, but more direct
# (no itertools, just loops and index finding).
#
# Key differences:
# - Solution 1: uses itertools.permutations + combinations as a black box
#   to represent "did i come before j". More Pythonic but indirect.
# - Solution 2: cuts search space by 50% (only first session's combos).
#   The most efficient of the three.
# - Solution 3: manual position-finding in nested loops. Most verbose
#   but simplest to translate to any language (C++/Java style).
#
# import sys
# sys.stdin = open('gymnastics.in', 'r')
# sys.stdout = open('gymnastics.out', 'w')
#
# k, n = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(k)]
#
# def better(a, b, session):
#     """Check if a is ahead of b in the given session's ranking."""
#     apos = 0
#     bpos = 0
#     for i in range(n):
#         if data[session][i] == a:
#             apos = i
#         if data[session][i] == b:
#             bpos = i
#     return apos < bpos
#
# def n_better(a, b):
#     """Return number of sessions where a is ahead of b."""
#     total = 0
#     for session in range(k):
#         if better(a, b, session):
#             total += 1
#     return total
#
# ans = 0
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a != b and n_better(a, b) == k:
#             ans += 1
# print(ans)
