"""
USACO 2017 January Contest, Bronze - Problem 2: Hoof, Paper, Scissors
=====================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=688

Tags: Brute Force, Simulation

Difficulty: very_easy

Problem Description:
-------------------
The cows play "Hoof, Paper, Scissors" (same rules as Rock, Paper, Scissors):
Hoof beats Scissors, Scissors beats Paper, Paper beats Hoof.

FJ watches two cows play N games (1 ≤ N ≤ 100). He can tell the gestures
apart but doesn't know which is which, so he labels them 1, 2, and 3.

Given the gesture pairs for all N games (first cow's gesture, second cow's
gesture), determine the maximum number of games the first cow could have won
under an optimal assignment of numbers to gestures.

Input:  Line 1: N
        Next N lines: two integers a b (each 1, 2, or 3) — gestures of
        the first and second cow.
Output: A single integer — the maximum possible wins for the first cow.

Sample Input:              Sample Output:
5                          2
1 2
2 2
1 3
1 1
3 2

Explanation:
One optimal assignment: 1 = scissors, 2 = hoof, 3 = paper.
This gives 2 wins ("1 3" and "3 2"). No other assignment yields more.

====================================================================
Solution 1: Brute Force over All Permutations
====================================================================
Since there are only 3! = 6 possible mappings from numbers to gestures,
we can enumerate all permutations of (1, 2, 3) as the mapping for
(hoof, paper, scissors), and count wins for the first cow under each
mapping. Take the maximum across all 6 permutations.

Time Complexity: O(6 * N) = O(N)
"""

import sys
from itertools import permutations

sys.stdin = open('hps.in', 'r')
sys.stdout = open('hps.out', 'w')

# Read number of games
n = int(input())
series = []

# Read each game's two gestures
for i in range(n):
    series.append(input().split())

# Generate all 6 permutations of '1','2','3'
# Each permutation maps positions to (hoof, paper, scissors)
per = list(permutations('123', 3))


def judge(l, a, b):
    """
    Under mapping l, check if first cow (a) beats second cow (b).
    l = (hoof, paper, scissors) — the number assigned to each gesture.
    Rules: hoof > scissors, scissors > paper, paper > hoof.
    """
    hoof, paper, scissors = l

    if a == hoof and b == scissors \
            or a == scissors and b == paper \
            or a == paper and b == hoof:
        return 1
    else:
        return 0


max_num = 0
# Try all 6 mappings
for p in per:
    num = 0
    for x, y in series:
        num += judge(p, x, y)
    max_num = max(max_num, num)

print(max_num)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Key insight: Only two possible win-direction cycles exist in RPS:
#   Cycle A: 1 > 2 > 3 > 1  (1 beats 2, 2 beats 3, 3 beats 1)
#   Cycle B: 2 > 1 > 3 > 2  (2 beats 1, 1 beats 3, 3 beats 2)
#
# Use a 4x4 frequency matrix to count each (first, second) pair.
# Then compute wins for both cycles in O(1) and take the max.
#
# Comparison with Solution 1:
#   - Solution 1 iterates over 6 permutations × N games
#   - Solution 2 counts frequencies in O(N), then O(1) for both cycles
#   - Same asymptotic O(N), but Solution 2 has a smaller constant factor
#
# Time Complexity: O(N)
#
# import sys
#
# sys.stdin = open('hps.in', 'r')
# sys.stdout = open('hps.out', 'w')
#
# n = int(input())
#
# # 4x4 frequency matrix for (first, second) gesture pairs
# matches = [[0] * 4 for _ in range(4)]
# for _ in range(n):
#     a, b = map(int, input().split())
#     matches[a][b] += 1
#
# # Cycle A: 1 beats 2, 2 beats 3, 3 beats 1
# max_wins = matches[1][2] + matches[2][3] + matches[3][1]
# # Cycle B: 1 beats 3, 3 beats 2, 2 beats 1
# alt_wins = matches[1][3] + matches[3][2] + matches[2][1]
# if alt_wins > max_wins:
#     max_wins = alt_wins
#
# print(max_wins)
