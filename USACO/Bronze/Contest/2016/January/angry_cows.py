"""
USACO 2016 January Contest, Bronze - Problem 2: Angry Cows
============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=592

Tags: Simulation, Brute Force

Difficulty: normal

Problem Description:
-------------------
N hay bales are placed at distinct integer positions on a number line. When a
cow is launched onto a hay bale at position x, it explodes with blast radius 1,
detonating any bales within 1 unit. These bales then explode (simultaneously)
with blast radius 2, and so on — at time t, bales explode with radius t,
triggering the next wave with radius t+1.

Determine the maximum number of hay bales that can explode from a single
launch by choosing the optimal starting bale.

Constraints: N ≤ 100, positions in [0, 1,000,000,000]

Sample Input:              Sample Output:
6                          5
8
5
6
13
3
4

Explanation:
  Launch at position 5:
    t=1 (r=1): 5 explodes → detonates 4, 6
    t=2 (r=2): 4,6 explode → detonate 3, 8
    t=3 (r=3): 3,8 explode → can't reach 13
  Total: 5 hay bales.


====================================================================
Solution 1: Simulation for Each Starting Bale (User's Solution)
====================================================================
For each hay bale as the starting point, simulate the chain reaction in both
directions:

  1. Sort the positions first.
  2. For each bale i, simulate leftward explosion:
     - With initial radius 1, find the farthest bale that explodes.
     - If any new bale is caught, update the "begin" point to the farthest
       bale caught, increment radius, and repeat.
     - Stop when no new bale is caught.
  3. Simulate rightward explosion similarly.
  4. Count total bales exploded; update max.

This mirrors the official USACO solution by Nick Wu.

Time Complexity: O(N³) worst-case, but N ≤ 100, so fine.
"""

import sys
sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')

n = int(input())

# Read hay bale positions, sort for simulation
line = []
for _ in range(n):
    line.append(int(input()))
line.sort()

max_v = 0

# Try each hay bale as the starting point
for i in range(n):
    cnt = 1                    # hay bale at index i explodes initially

    # --- Simulate leftward chain reaction ---
    radius = 1
    begin = i                  # index of the bale currently exploding leftward
    cur = begin - 1            # next candidate bale to the left
    found = False              # whether we caught a new bale in this wave
    while begin > 0 and cur >= 0:
        if line[begin] - line[cur] <= radius:
            cnt += 1           # caught this bale
            found = True
            cur -= 1
        else:
            if found:
                # The farthest bale caught becomes the new explosion source
                begin = cur + 1
                radius += 1
                found = False
            else:
                break          # no more bales caught → stop

    # --- Simulate rightward chain reaction ---
    radius = 1
    begin = i                  # index of the bale currently exploding rightward
    cur = begin + 1            # next candidate bale to the right
    found = False
    while begin < n - 1 and cur <= n - 1:
        if line[cur] - line[begin] <= radius:
            cnt += 1           # caught this bale
            found = True
            cur += 1
        else:
            if found:
                # The farthest bale caught becomes the new explosion source
                begin = cur - 1
                radius += 1
                found = False
            else:
                break          # no more bales caught → stop

    max_v = max(max_v, cnt)

print(max_v)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same idea but organized with a helper function getExplosionIndex() that
# simulates the explosion in one direction and returns the farthest index.
#
# Time Complexity: O(N²)

# import sys
# sys.stdin = open('angry.in', 'r')
# sys.stdout = open('angry.out', 'w')
#
# n = int(input())
# locations = [int(input()) for _ in range(n)]
# locations.sort()
#
#
# def get_explosion_index(locations, start_index, go_left):
#     """Simulate explosion in one direction, return farthest index exploded."""
#     last_explosion_index = start_index
#     current_radius = 1
#     direction = -1 if go_left else 1
#
#     while 0 < last_explosion_index < len(locations) - 1:
#         next_index = last_explosion_index
#         while (0 <= next_index + direction < len(locations) and
#                abs(locations[next_index + direction] - locations[last_explosion_index]) <= current_radius):
#             next_index += direction
#
#         if next_index == last_explosion_index:
#             break                          # no new bale caught
#
#         last_explosion_index = next_index   # new explosion source
#         current_radius += 1                 # radius increases
#
#     return last_explosion_index
#
#
# answer = 1
# for start in range(n):
#     left_most = get_explosion_index(locations, start, True)
#     right_most = get_explosion_index(locations, start, False)
#     num_exploded = right_most - left_most + 1
#     if num_exploded > answer:
#         answer = num_exploded
#
# print(answer)
