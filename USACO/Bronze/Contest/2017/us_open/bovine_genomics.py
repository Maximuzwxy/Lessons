"""
USACO 2017 US Open Contest, Bronze - Problem 2: Bovine Genomics
================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=736

Tags: Brute Force, String

Difficulty: easy

Problem Description:
-------------------
FJ owns N spotty cows and N plain cows. He sequences their genomes — each
genome is a string of length M built from characters A, C, G, T.

He believes spots are caused by a mutation at a single genome position.
A position "potentially explains spottiness" if, by looking at just that one
position, FJ can perfectly distinguish spotty from plain cows (i.e., no
character appears at that position in both a spotty and a plain cow).

Given N spotty genomes and N plain genomes (both length M, 1 ≤ N, M ≤ 100),
count how many positions potentially explain spottiness.

Input:  Line 1: N M
        Next N lines: spotty cow genomes (each length M)
        Next N lines: plain cow genomes (each length M)
Output: A single integer — number of positions that can explain spottiness.

Sample Input:              Sample Output:
3 8                        1
AATCCCAT
GATTGCAA
GGTCGCAA
ACTCCCAG
ACTCGCAT
ACTTCCAT

Explanation:
Only position 2 works: spotty cows have A or G, plain cows have C.
No character appears in both groups at position 2.

====================================================================
Solution 1: Set Intersection (User's Solution)
====================================================================
For each position i (0 to M-1):
  1. Build a set of all characters appearing in spotty cows at position i.
  2. For each plain cow, check if its character at position i is in the set.
     If yes → position fails (not distinguishable), break.
  3. If no overlap found → position is valid, increment count.

Time Complexity: O(N × M), Space Complexity: O(1) (set size ≤ 4).
"""

import sys

sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')

n, m = map(int, input().split())
spotty = []
plain = []
num = 0

# Read spotty cow genomes
for _ in range(n):
    spotty.append(list(input()))

# Read plain cow genomes
for _ in range(n):
    plain.append(list(input()))

# Check each position independently
for i in range(m):
    gen = set()          # characters appearing in spotty cows at position i
    flag = True          # assume position works until proven otherwise

    # Collect all spotty cow characters at position i
    for j in range(n):
        gen.add(spotty[j][i])

    # Check if any plain cow shares a character at position i
    for k in range(n):
        if plain[k][i] in gen:
            flag = False  # overlap found → position cannot explain spottiness
            break

    if flag:
        num += 1

print(num)


# =====================================================================
# Solution 2: Official USACO Solution (by Nathan Pinsker) — Python Translation
# =====================================================================
# Same idea but uses boolean arrays for the 4 possible characters (A, C, G, T)
# instead of a set. For each position:
#   - Record which of {A,C,G,T} appear in spotty cows (found_cow[0][0..3])
#   - Record which of {A,C,G,T} appear in plain cows (found_cow[1][0..3])
#   - If any character appears in both → position fails
#   - Otherwise → position works
#
# Comparison with Solution 1:
#   - Solution 1: uses a Python set, checks membership directly → cleaner
#   - Solution 2: uses fixed-size boolean arrays (C++ style) → more verbose
#   - Both are O(N × M), logic identical
#
# Time Complexity: O(N × M), Space Complexity: O(1)
#
# import sys
#
# sys.stdin = open('cownomics.in', 'r')
# sys.stdout = open('cownomics.out', 'w')
#
# n, m = map(int, input().split())
# spotty = [input().strip() for _ in range(n)]
# plain = [input().strip() for _ in range(n)]
#
# answer = 0
#
# def test_location(j):
#     """Return True if position j can explain spottiness."""
#     # found_cow[0] = spotty, found_cow[1] = plain
#     # Index: 0=A, 1=C, 2=G, 3=T
#     found_cow = [[False] * 4 for _ in range(2)]
#
#     for i in range(n):
#         if spotty[i][j] == 'A':
#             found_cow[0][0] = True
#         if spotty[i][j] == 'C':
#             found_cow[0][1] = True
#         if spotty[i][j] == 'G':
#             found_cow[0][2] = True
#         if spotty[i][j] == 'T':
#             found_cow[0][3] = True
#
#     for i in range(n):
#         if plain[i][j] == 'A':
#             found_cow[1][0] = True
#         if plain[i][j] == 'C':
#             found_cow[1][1] = True
#         if plain[i][j] == 'G':
#             found_cow[1][2] = True
#         if plain[i][j] == 'T':
#             found_cow[1][3] = True
#
#     for i in range(4):
#         if found_cow[0][i] and found_cow[1][i]:
#             return False       # same character appears in both groups
#     return True
#
# for j in range(m):
#     if test_location(j):
#         answer += 1
#
# print(answer)
