# =============================================================================
# USACO 2016 US Open Contest, Bronze
# Problem 1. Diamond Collector
# https://usaco.org/index.php?page=viewproblem2&cpid=639
# Difficulty: easy
# =============================================================================

# [Problem Summary]
# Bessie has N diamonds of different sizes. She wants to display some of them
# in a case where any two diamonds differ in size by at most K.
# Given N and K, find the maximum number of diamonds that can be displayed.

# [Input Format]
#   - Line 1: N (1 ≤ N ≤ 1000) and K (0 ≤ K ≤ 10,000)
#   - Lines 2~N+1: Size of each diamond (1 ~ 10,000)

# [Output Format]
#   - Single integer: maximum number of diamonds in the display case

# [Approach]
# Both solutions use a "sliding window" approach:
# For each diamond as the left boundary of a window, count how many diamonds
# have size within [size[i], size[i] + K]. Take the maximum count.

# Solution 1: Brute Force O(n^2)
#   For each diamond, check all other diamonds and count those within K

# Solution 2: Sort + Early Termination O(n^2)
#   Sort the sizes first. Since the array is sorted, once the difference
#   exceeds K, we can break early (no need to check remaining diamonds).
#   This reduces unnecessary comparisons.

# =============================================================================
# Solution 1: Brute Force
# Time: O(n^2), Space: O(n)
# =============================================================================
# import sys
# sys.stdin = open('diamond.in', 'r')
# sys.stdout = open('diamond.out', 'w')
#
# n, k = map(int, input().split())
# diamonds = []
#
# for _ in range(n):
#     diamonds.append(int(input()))
#
# max_v = 0
# for i in range(n):
#     count = 1  # window includes diamond i itself
#     for j in range(n):
#         if i == j:
#             continue
#         # check if diamond j is within [diamonds[i], diamonds[i] + K]
#         if 0 <= diamonds[j] - diamonds[i] <= k:
#             count += 1
#     max_v = max(max_v, count)
#
# print(max_v)

# =============================================================================
# Solution 2: Sort + Sliding Window (Two-Pointer Concept)
# Time: O(n^2), Space: O(n)
#
# NOTE: "Two-pointer" is an algorithm concept, not a Python feature.
# In Python, we use indices to simulate pointer behavior.
# Here, i acts as the left boundary and j advances forward as the right boundary.
# Since the array is sorted, once diamonds[j] - diamonds[i] > K,
# all subsequent elements will also be > K, so we can break early.
# =============================================================================
import sys
sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')

n, k = map(int, input().split())
diamonds = []

for _ in range(n):
    diamonds.append(int(input()))

diamonds.sort()

max_v = 0
for i in range(n):
    count = 1  # window includes diamond at index i
    # j starts from i+1 and moves forward (right pointer)
    for j in range(i + 1, n):
        if diamonds[j] - diamonds[i] <= k:
            count += 1
        else:
            # since array is sorted, once diff > K, all later diffs will be > K
            break
    max_v = max(max_v, count)

print(max_v)