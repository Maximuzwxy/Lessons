"""
USACO 2017 February Contest, Bronze - Problem 1: Why Did the Cow Cross the Road
===============================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=711

Tags: Simulation

Difficulty: very_easy

Problem Description:
-------------------
FJ logs N observations (1 ≤ N ≤ 100) of his 10 cows crossing a road.
Each observation records a cow ID (1..10) and which side of the road the cow
is on (0 or 1).

A confirmed crossing happens when consecutive sightings of the same cow show
it on different sides of the road. Count the total number of confirmed
crossings across all cows.

Input:  Line 1: N
        Next N lines: cow_id side (cow_id in 1..10, side is 0 or 1)
Output: A single integer — total number of confirmed crossings.

Sample Input:              Sample Output:
8                          3
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1

Explanation:
Cow 3 crosses twice (side 1→0→1). Cow 4 crosses once (side 1→0).
Cows 2 and 6 do not cross.
Total confirmed crossings = 3.

====================================================================
Solution 1: List / Array Tracking (User's Solution)
====================================================================
Use a fixed-size array (length 11, indices 1..10) to store each cow's last
known side. Initialize all entries to -1 (unseen). For each observation:
  - If this is the cow's first sighting, record its side.
  - If the cow was seen before and the side changed, increment the crossing
    count and update the stored side.
  - If the side stayed the same, do nothing.

Time Complexity: O(N), Space Complexity: O(1) (fixed 11 slots).
"""

import sys

sys.stdin = open('crossroad.in', 'r')
sys.stdout = open('crossroad.out', 'w')

n = int(input())
lst = []
for i in range(n):
    lst.append(input().strip())


def cross(nums):
    count = 0
    a = [-1] * 11                    # a[cow_id] = last known side, -1 = unseen
    for line in nums:
        index, side = list(map(int, line.split()))
        if a[index] == -1:           # first time seeing this cow
            a[index] = side
        elif a[index] != side:       # side changed → confirmed crossing
            a[index] = side
            count += 1
    return count


ret = cross(lst)
print(ret)


# =====================================================================
# Solution 2: Dictionary Tracking (User's Solution)
# =====================================================================
# Same logic as Solution 1, but uses a dict instead of a fixed-size list.
# The dict automatically grows as new cow IDs are encountered (no need to
# pre-allocate 11 slots). The core algorithm is identical.
#
# Time Complexity: O(N), Space Complexity: O(1) (at most 10 keys).
#
# import sys
#
# sys.stdin = open('crossroad.in', 'r')
# sys.stdout = open('crossroad.out', 'w')
#
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(input().strip())
#
#
# def cross(nums):
#     count = 0
#     d = {}
#     for line in nums:
#         index, side = list(map(int, line.split()))
#         if index not in d:          # first time seeing this cow
#             d[index] = side
#         elif d[index] != side:      # side changed → confirmed crossing
#             d[index] = side
#             count += 1
#     return count
#
#
# ret = cross(lst)
# print(ret)


# =====================================================================
# Solution 3: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same idea: track each cow's last seen side in an array.
# Key difference: uses +1 to shift side values (0→1, 1→2) so that 0 means
# "not seen yet", avoiding the need for a separate sentinel value.
# Counts a crossing whenever lastSeen[index] > 0 and differs from current.
#
# Comparison with user's solutions:
#   - User's list:  uses -1 as sentinel, checks whether side changed
#   - User's dict:  same logic, just uses a dict instead of array
#   - Official:     uses +1 shift so 0 = unseen (no sentinel needed),
#                   otherwise identical in algorithm
# All three are O(N) and essentially the same approach.
#
# Time Complexity: O(N), Space Complexity: O(1)
#
# import sys
#
# sys.stdin = open('crossroad.in', 'r')
# sys.stdout = open('crossroad.out', 'w')
#
# n = int(input())
#
# # lastSeen[cow] = 0 (unseen), 1 (left side), 2 (right side)
# lastSeen = [0] * 11
# crossings = 0
#
# for _ in range(n):
#     cow_id, side = map(int, input().split())
#     current = side + 1            # shift: 0→1, 1→2, so 0 = unseen
#
#     if lastSeen[cow_id] > 0 and lastSeen[cow_id] != current:
#         crossings += 1            # side changed → confirmed crossing
#
#     lastSeen[cow_id] = current    # update last known side
#
# print(crossings)
