# =============================================================================
# USACO 2020 February Contest, Bronze
# Problem 2. Mad Scientist
# https://usaco.org/index.php?page=viewproblem2&cpid=1012
# =============================================================================

"""
【Problem Description】
- Farmer John ordered N cows (1 ≤ N ≤ 1000), each is H (Holstein) or G (Guernsey)
- String A = desired order, String B = actual order when cows arrived
- Ben's machine can flip any substring: all H→G and G→H in that substring
- Find the minimum number of substring flips to transform B into A

【Input】
- First line: N
- Next two lines: strings A and B, each of length N (only 'H' and 'G')

【Output】
- Minimum number of substring flips needed

【Example】
Input:
7
GHHHGHH
HHGGGHH
Output:
2

Explanation:
- Flip position 1 alone: GHGGGHH
- Flip positions 3-4: GHHHGHH = A
- Total: 2 flips

【Solution - Greedy】
Key Insight: Only flip contiguous segments where A[i] ≠ B[i].
- Find all maximal contiguous segments where A and B differ
- Each such segment requires exactly 1 flip

Why it works:
- If A[i] = B[i], position i is already correct, don't touch it
- If A[i] ≠ B[i], flip the entire mismatching segment at once
- Flipping a segment doesn't affect positions outside it, so
  we can process segments independently from left to right

Algorithm:
- Scan from left to right
- When we enter a mismatching region, count one flip
- When we exit a mismatching region (back to matching), reset

Time: O(N)   Space: O(N)
"""

# =============================================================================
# Solution 1 - For Loop with Flag
# =============================================================================
import sys
sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')

n = int(input())
a = input()
b = input()

count = 0
flag = True   # True = currently in "matching" state (A[i] == B[i])

for i in range(n):
    # If mismatch AND we just entered this mismatching segment
    if a[i] != b[i] and flag:
        count += 1       # Start a new flip for this segment
        flag = False     # Now we are inside a mismatching segment
    # If match, exit the mismatching segment
    elif a[i] == b[i]:
        flag = True      # Back to matching state

print(count)

# =============================================================================
# Solution 2 - While Loop with Segment Length Counter
# =============================================================================
import sys
# sys.stdin = open('breedflip.in', 'r')
# sys.stdout = open('breedflip.out', 'w')
#
# n = int(input())
# a = list(input())
# b = list(input())
#
# count = 0
#
# i = 0
# l = 0    # Length of current mismatching segment
#
# while i < n:
#     if a[i] != b[i]:
#         l += 1     # Extend the current mismatching segment
#     else:
#         if l > 0:  # We just exited a mismatching segment
#             count += 1   # One flip covers the entire segment
#         l = 0      # Reset segment length
#     i += 1
#
# # Handle the case where the string ends in a mismatching segment
# if i == n and l > 0:
#     count += 1
#
# print(count)