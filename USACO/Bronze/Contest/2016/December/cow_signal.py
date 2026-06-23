"""
USACO 2016 December Contest, Bronze - Problem 3: The Cow-Signal
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=665

Tags: Simulation, 2D Grid

Difficulty: easy

Problem Description:
-------------------
Bessie has drawn a signal on an M × N grid using '.' and 'X' characters. She
wants to enlarge the signal by a factor of K in both dimensions: each original
cell becomes a K × K block of the same character.

Constraints: 1 ≤ M, N ≤ 10, 1 ≤ K ≤ 10

Sample Input:              Sample Output:
5 4 2                      XXXXXX..
XXX.                       XXXXXX..
X..X                       XX....XX
XXX.                       XX....XX
X..X                       XXXXXX..
XXX.                       XXXXXX..
                           XX....XX
                           XX....XX
                           XXXXXX..
                           XXXXXX..


====================================================================
Solution 1: Row-by-Row Expansion (User's Solution)
====================================================================
For each original row:
  1. Expand horizontally: each character is repeated K times (e.g., 'X' → 'XX')
  2. Expand vertically: the expanded row is appended K times to the output.

Time Complexity: O(M × N × K²), Space Complexity: O(M × K × N × K).
"""

import sys

sys.stdin = open('cowsignal.in', 'r')
sys.stdout = open('cowsignal.out', 'w')

m, n, k = map(int, input().split())    # M rows, N columns, K enlargement factor
origin = []
amplify = []

# Read the original M×N signal
for i in range(m):
    origin.append(input())

# For each row, expand characters horizontally, then repeat K times vertically
for line in origin:
    # Step 1: Horizontal expansion — repeat each character K times
    s = ''
    for c in line:
        s += c * k                     # each char → K copies

    # Step 2: Vertical expansion — repeat the expanded row K times
    for i in range(k):
        amplify.append(s)

# Output the enlarged signal
for i in amplify:
    print(i)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same approach but prints directly without building the entire output
# list in memory. For each input row, generate K copies of the same row
# where each character is printed K times.
#
# Time Complexity: O(M × N × K²), Space Complexity: O(1) beyond input.

# import sys
# sys.stdin = open('cowsignal.in', 'r')
# sys.stdout = open('cowsignal.out', 'w')
#
# m, n, k = map(int, input().split())
#
# for i in range(m):
#     curr_row = input().strip()
#     # Repeat this row K times vertically
#     for _ in range(k):
#         # Expand each character K times horizontally, print the row
#         expanded = ''.join(ch * k for ch in curr_row)
#         print(expanded)
