"""
USACO 2016 February Contest, Bronze - Problem 2: Circular Barn
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=616

Tags: Brute Force, Simulation

Problem Description:
-------------------
A circular barn has n rooms (3 ≤ n ≤ 1,000) arranged clockwise. Each room i
needs exactly r_i cows (1 ≤ r_i ≤ 100). Cows enter through a single unlocked
exterior door, then walk clockwise until they find a room to settle in. All
cows enter through the same unlocked door.

Determine which door to unlock to minimize the total distance walked by all
cows. Distance = number of interior doors passed through.

Sample Input:              Sample Output:
5                          48
4
7
8
6
4

Explanation:
  Unlock the room needing 7 cows. Starting from that room, cows for the next
  4 rooms walk 1,2,3,4 doors respectively: 8*1 + 6*2 + 4*3 + 4*4 = 48.


====================================================================
Solution 1: Array Rotation + Distance Sum (User's Solution)
====================================================================
Try each room as the unlock door. For each candidate, rotate the circular
array so the unlocked room is first (skipped for distance calculation), and
compute the total distance: sum of r_i × distance_traveled for each room.

  1. Read all room requirements into a list.
  2. For each room i as the unlock point, create a rotated list where the
     unlocked room is skipped (excluded), and the remaining rooms follow in
     clockwise order.
  3. get_distance(): for rooms at positions 0..n-2 (meaning doors 1..n-1 away),
     add cows[j] × (j+1) to total.
  4. Track the minimum across all candidates.

Time Complexity: O(N²), Space Complexity: O(N).
"""

import sys
sys.stdin = open('cbarn.in', 'r')
sys.stdout = open('cbarn.out', 'w')

n = int(input())

circle = []    # r_i: number of cows needed in each room
min_dis = 0


def get_distance(rooms):
    """
    Compute total travel distance for cows in the given ordered rooms.
    rooms[0] is 1 door away from the unlock room, rooms[1] is 2 doors, etc.
    """
    dis = 0
    for j in range(n - 1):           # last room is n-1 doors away
        dis += rooms[j] * (j + 1)
    return dis


# Read room requirements
for i in range(n):
    circle.append(int(input()))

# Try each room as the unlock door
for i in range(n):
    # Rotate: skip room i, start from i+1 going clockwise
    tmp_circle = circle[i + 1:] + circle[:i]

    if min_dis == 0:
        min_dis = get_distance(tmp_circle)
    else:
        min_dis = min(get_distance(tmp_circle), min_dis)

print(min_dis)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same approach but uses modular arithmetic instead of array rotation:
# cows[(unlock+offset)%n] gives the number of cows offset doors away from
# the unlocked room, avoiding O(N) array copies.
#
# Time Complexity: O(N²), Space Complexity: O(1) extra.

# import sys
# sys.stdin = open('cbarn.in', 'r')
# sys.stdout = open('cbarn.out', 'w')
#
# n = int(input())
# cows = [int(input()) for _ in range(n)]
#
# ans = n * n * 100   # upper bound: 100N cows × N max distance each
#
# for unlock in range(n):
#     current_distance = 0
#     for offset in range(n):
#         # Room at distance "offset" clockwise from unlocked door
#         current_distance += offset * cows[(unlock + offset) % n]
#     if current_distance < ans:
#         ans = current_distance
#
# print(ans)
