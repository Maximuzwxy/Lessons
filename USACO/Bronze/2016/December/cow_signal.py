# =============================================================================
# USACO 2016 December Contest, Bronze
# Problem 3. The Cow-Signal
# https://usaco.org/index.php?page=viewproblem2&cpid=665
# =============================================================================

"""
【Problem Description】
- Bessie has drawn a signal on an M × N grid using '.' and 'X' characters
- She wants to enlarge the signal by a factor of K in both dimensions
- Each cell becomes a K × K block of the same character

【Input】
- First line: M, N, K (1 ≤ M, N ≤ 10, 1 ≤ K ≤ 10)
- Next M lines: N-character strings describing the signal

【Output】
- KM lines, each with KN characters, giving the enlarged signal

【Example】
Input:
5 4 2
XXX.
X..X
XXX.
X..X
XXX.
Output:
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..

【Solution - Simulation】
For each original row:
  1. Expand each character K times horizontally
  2. Repeat this expanded row K times vertically

Time: O(M × N × K²)   Space: O(M × N × K²)
- Simple simulation, directly follow the problem description
"""

import sys

sys.stdin = open('cowsignal.in', 'r')
sys.stdout = open('cowsignal.out', 'w')

m, n, k = map(int, input().split())
origin = []
amplify = []

# Read the original M×N signal
for i in range(m):
    origin.append(input())

# For each row, expand characters horizontally, then repeat K times vertically
for line in origin:
    s = ''
    for c in line:
        # Each character becomes K copies
        s += c * k
    # Repeat this expanded row K times
    for i in range(k):
        amplify.append(s)

# Output the enlarged signal
for i in amplify:
    print(i)