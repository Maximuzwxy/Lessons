"""
USACO 2015 December Contest, Bronze - Problem 2: Speeding Ticket
===================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=568

Tags: Simulation

Problem Description:
-------------------
The road is exactly 100 miles long, divided into N segments. Each segment has
a positive integer length (in miles) and an integer speed limit (1..100 mph).
The lengths of all N segments sum to 100.

Bessie's journey is described by M segments: the length she travels and the
speed she drove during that segment. The lengths of all M segments also sum
to 100 miles.

Given the road speed limits and Bessie's driving speeds, determine the
maximum amount over the speed limit Bessie drove during any part of her
journey. If she never exceeded the speed limit, output 0.

Constraints:
  - 1 <= N, M <= 100
  - Speed limits and driving speeds are between 1 and 100.

Sample Input:              Sample Output:
3 3                        5
40 75
50 35
10 45
40 76
20 30
40 40

Explanation:
  Road: 40 miles @ 75mph, 50 miles @ 35mph, 10 miles @ 45mph
  Bessie: 40 miles @ 76mph, 20 miles @ 30mph, 40 miles @ 40mph
  In the first 40 miles, Bessie is 76 - 75 = 1 mph over.
  In the last 40 miles, max overspeed is 40 - 35 = 5 mph
    (she drives 40mph on a section where the limit drops to 35).
  Maximum over the speed limit = 5.


====================================================================
Solution 1: 1-Mile Segment Expansion (User's Solution)
====================================================================
Break the 100-mile road into 100 individual 1-mile sections:
  1. Read N road segments, expand each length into 1-mile chunks with
     the corresponding speed limit.
  2. Read M journey segments, similarly expand Bessie's speed per mile.
  3. Compare mile by mile: for each mile, compute bessie_speed - limit.
  4. Track the maximum overage; if never exceeding, answer is 0.

This is the same approach as the official USACO solution by Nick Wu.

Time Complexity: O(100) = O(1) — constant, since the road is always 100 miles.
"""

import sys

# sys.stdin = open('speeding.in', 'r')
# sys.stdout = open('speeding.out', 'w')

# Read N (road segments) and M (Bessie's journey segments)
n, m = map(int, input().split())

seg_limit = []   # road speed limit segments (raw strings)
seg_bessie = []  # Bessie's journey segments (raw strings)

# Read road speed limit segments
for i in range(n):
    seg_limit.append(input())

# Read Bessie's journey segments
for i in range(m):
    seg_bessie.append(input())


def set_speed(dest, origin, num):
    """
    Expand segment descriptions into a 1-mile-per-element speed list.

    For each segment (length, speed), append 'speed' to 'dest'
    'length' times — effectively creating a mile-by-mile speed mapping.
    """
    for j in range(num):
        dis, speed = map(int, origin[j].split())
        for k in range(dis):
            dest.append(speed)


# Build mile-by-mile arrays (each will have exactly 100 elements)
limit = []   # speed limit for each of the 100 miles
bessie = []  # Bessie's speed for each of the 100 miles

set_speed(limit, seg_limit, n)
set_speed(bessie, seg_bessie, m)

# Compare mile by mile to find the maximum overspeed
max_v = 0
for x in range(100):                     # 100 miles, 0-indexed
    max_v = max(max_v, bessie[x] - limit[x])

print(max_v)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# The official solution uses the same 1-mile expansion approach.
# Key difference: uses fixed-size arrays [0]*100, and processes segments
# with a currentMile pointer that increments as each mile is filled.
#
# Time Complexity: O(100) = O(1).

# import sys
#
# sys.stdin = open('speeding.in', 'r')
# sys.stdout = open('speeding.out', 'w')
#
# n, m = map(int, input().split())
#
# # speedLimits[i] = speed limit for mile i to i+1
# speedLimits = [0] * 100
# currentMile = 0
# for _ in range(n):
#     length, limit = map(int, input().split())
#     for _ in range(length):
#         speedLimits[currentMile] = limit
#         currentMile += 1
#
# # travelSpeed[i] = Bessie's speed for mile i to i+1
# travelSpeed = [0] * 100
# currentMile = 0
# for _ in range(m):
#     length, speed = map(int, input().split())
#     for _ in range(length):
#         travelSpeed[currentMile] = speed
#         currentMile += 1
#
# # Find max overspeed across all 100 miles
# maxOver = 0
# for i in range(100):
#     exceeded = travelSpeed[i] - speedLimits[i]
#     if exceeded > maxOver:
#         maxOver = exceeded
#
# print(maxOver)


# =====================================================================
# Solution 3: Two-Pointer Segment Walk (Alternative Solution)
# =====================================================================
# Instead of expanding into 100 individual miles, process segments directly
# using two pointers. This avoids building the 100-element arrays and works
# in O(N+M) time with O(N+M) space.
#
# Algorithm:
#   1. Read N road segments and M journey segments into lists.
#   2. Use two indices x (road) and y (journey).
#   3. Compare the current overlapping segment: compute overage.
#   4. Whichever segment is shorter gets consumed; the longer one keeps the
#      remaining length for the next comparison.
#   5. Continue until all segments are processed.
#
# Time Complexity: O(N + M), Space Complexity: O(N + M).

# import sys
#
# sys.stdin = open('speeding.in', 'r')
# sys.stdout = open('speeding.out', 'w')
#
# n, m = map(int, input().split())
#
# limit = []
# bessie = []
#
# for i in range(n):
#     limit.append(list(map(int, input().split())))
#
# for j in range(m):
#     bessie.append(list(map(int, input().split())))
#
# x = y = 0          # indices for road and journey segments
# max_v = 0
#
# while x < n and y < m:
#     # Over-speed in the overlapping portion of current segments
#     max_v = max(max_v, bessie[y][1] - limit[x][1])
#
#     # Consume the shorter segment and advance the pointer
#     if limit[x][0] > bessie[y][0]:
#         limit[x][0] -= bessie[y][0]   # road segment still has remaining length
#         y += 1
#     elif limit[x][0] < bessie[y][0]:
#         bessie[y][0] -= limit[x][0]   # journey segment still has remaining length
#         x += 1
#     else:
#         x += 1                         # equal lengths: both consumed
#         y += 1
#
# print(max_v)
