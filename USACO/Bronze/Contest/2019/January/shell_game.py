"""
USACO 2019 January Contest, Bronze - Problem 1. Shell Game
============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=891

Tags: Brute Force, Simulation

Difficulty: very_easy

Problem Description:
-------------------
Three shells (1, 2, 3), pebble under one of them. Bessie swaps pairs of
shells, Elsie guesses after each swap. Elsie does NOT know the initial
location of the pebble. Given N swaps and N guesses (1 ≤ N ≤ 100), find
the maximum possible number of correct guesses, assuming optimal initial
pebble placement.

Sample Input:        Sample Output:
3                    2
1 2 1
3 2 1
1 3 1

Explanation:
Start=1 → correct once (guess 3)
Start=2 → correct twice (guesses 1,2)  ← best
Start=3 → correct 0 times
Answer = 2.

====================================================================
Solution 1: Brute Force — Try Each Starting Pebble Position
====================================================================
Try each of the 3 possible starting positions (1, 2, 3). For each,
simulate all N swaps: maintain arr[shell] = 1 if pebble is under that
shell, swap arr[a] and arr[b] on each swap, then check if arr[g] == 1.
Count correct guesses, track max.

Time: O(3 × N) = O(N). N ≤ 100, trivial.
"""

import sys

sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

max_v = 0
for pebble in range(1, 4):           # try each starting position
    arr = [0] * 4
    arr[pebble] = 1                   # pebble starts under shell 'pebble'
    cnt = 0
    for a, b, g in lst:               # process each swap + guess
        arr[a], arr[b] = arr[b], arr[a]   # swap shells
        if arr[g] == 1:                   # is pebble under guessed shell?
            cnt += 1
    max_v = max(max_v, cnt)

print(max_v)


# =====================================================================
# Solution 2: Track Shell→Position Mapping — Single Pass O(N)
# =====================================================================
# Key insight: instead of iterating 3 times, we can do it in ONE pass.
# Maintain shells[i] = which original position shell i currently holds.
# Initialize shells[i] = i (shell i holds position i at start).
#
# When shells a and b swap, swap what they hold: shells[a] ↔ shells[b].
# After swap, shells[g] tells us WHICH original position was just guessed.
# Increment times[shells[g]].
#
# At the end, max(times) is the answer — because times[p] is how many
# correct guesses we'd get if pebble started under original position p.
#
# Time: O(N) — single pass, no outer loop ×3.
#
# import sys
# sys.stdin = open('shell.in', 'r')
# sys.stdout = open('shell.out', 'w')
#
# n = int(input())
# lst = [list(map(int, input().split())) for _ in range(n)]
#
# shells = [0, 1, 2, 3]     # shell i holds original position i
# times = [0] * 4            # times[p] = correct guesses if pebble started at p
#
# for a, b, g in lst:
#     shells[a], shells[b] = shells[b], shells[a]  # swap position assignments
#     times[shells[g]] += 1                        # count guess for this position
#
# print(max(times))


# =====================================================================
# Solution 3: Official USACO Solution — Track Pebble Directly
# =====================================================================
# Same idea as Solution 1 but tracks the pebble position directly with
# a variable current_shell instead of using an array.
#
# For each starting position (1, 2, 3):
#   current_shell = starting position
#   if a == current_shell → pebble moves to b
#   elif b == current_shell → pebble moves to a
#   if current_shell == guess → correct++
#
# Key differences:
# - Solution 1: uses arr[4] with 0/1 to track pebble. More visual.
# - Solution 2: most efficient, O(N) single pass via position-tracking.
#   Elegant mathematical insight — the three starting positions are just
#   parallel timelines, and we can track all three simultaneously via
#   the shell→position mapping.
# - Solution 3: tracks pebble position as a variable. Most C++-like.
#   Equivalent to Solution 1 in logic and complexity.
#
# import sys
# sys.stdin = open('shell.in', 'r')
# sys.stdout = open('shell.out', 'w')
#
# n = int(input())
# A, B, G = [], [], []
# for _ in range(n):
#     a, b, g = map(int, input().split())
#     A.append(a); B.append(b); G.append(g)
#
# def num_correct(start):
#     cur = start
#     correct = 0
#     for i in range(n):
#         if A[i] == cur:
#             cur = B[i]
#         elif B[i] == cur:
#             cur = A[i]
#         if cur == G[i]:
#             correct += 1
#     return correct
#
# best = max(num_correct(i) for i in range(1, 4))
# print(best)
