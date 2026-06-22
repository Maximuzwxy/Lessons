"""
USACO 2016 February Contest, Bronze - Problem 3: Load Balancing
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=617

Tags: Brute Force, 2D Grid

Problem Description:
-------------------
N cows are at distinct positions (x_i, y_i) on a 2D farm (N ≤ 100, x_i and
y_i are positive odd integers up to B ≤ 1,000,000).

FJ builds two infinite fences:
  - vertical at x = a (a must be even)
  - horizontal at y = b (b must be even)
The fences divide the field into 4 quadrants. Let M = max number of cows in
any single quadrant. Find the minimum possible M.

Sample Input:              Sample Output:
7 10                       2
7 3
5 5
9 7
3 1
7 7
5 3
9 1


====================================================================
Solution 1: Fence at Cow Borders (User's Solution)
====================================================================
Key insight: the optimal fence position only needs to be just past a cow's
coordinate (to the next even integer). So we only need to try fences at
x = cow_x + 1 and y = cow_y + 1 (which makes them even since cow coords are odd).

  1. Store all cow positions.
  2. For each possible vertical fence at pos_x + 1 and horizontal fence at
     pos_y + 1, count cows in each of the 4 quadrants.
  3. Track the maximum quadrant count for this fence pair.
  4. Return the minimum of these maximums across all fence pairs.

Time Complexity: O(N³) worst case (N² fence pairs × N cows per count).
With N ≤ 100, this is fine.

Note: The problem guarantees no fence passes through a cow because cows are
at odd coordinates and fences are at even coordinates (cow_x + 1 is even).
"""

import sys
sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')

n, b = map(int, input().split())

locations_x = []    # x-coordinates of all cows (for fence candidate generation)
locations_y = []    # y-coordinates of all cows
locations = []      # list of (x, y) pairs for quadrant counting

# Read all cow positions
for i in range(n):
    px, py = map(int, input().split())
    locations_x.append(px)
    locations_y.append(py)
    locations.append([px, py])

locations_x.sort()  # not strictly necessary but doesn't hurt
locations_y.sort()


def get_max_num(cross_x, cross_y):
    """
    Count cows in each of the 4 quadrants defined by fences at (cross_x, cross_y).
    Returns the maximum count among the 4 quadrants.
    """
    left_top = 0      # x < cross_x, y > cross_y  (upper left)
    left_bottom = 0   # x < cross_x, y < cross_y  (lower left)
    right_top = 0     # x > cross_x, y > cross_y  (upper right)
    right_bottom = 0  # x > cross_x, y < cross_y  (lower right)

    for x, y in locations:
        if x < cross_x and y > cross_y:
            left_top += 1
        elif x < cross_x and y < cross_y:
            left_bottom += 1
        elif x > cross_x and y > cross_y:
            right_top += 1
        elif x > cross_x and y < cross_y:
            right_bottom += 1

    return max(left_top, left_bottom, right_top, right_bottom)


smallest = n    # worst case: all N cows in one quadrant

# Try fence positions just past each cow's coordinates (cow_x+1, cow_y+1 are even)
for pos_x in locations_x:
    for pos_y in locations_y:
        smallest = min(smallest, get_max_num(pos_x + 1, pos_y + 1))

print(smallest)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same approach; stores x and y in arrays indexed by cow, and uses explicit
# if-statements per quadrant instead of elif (handles cows exactly on the
# fence line, though they can't be due to parity).
#
# Time Complexity: O(N³)

# import sys
# sys.stdin = open('balancing.in', 'r')
# sys.stdout = open('balancing.out', 'w')
#
# n = int(input().split()[0])  # ignore B
#
# x_loc = [0] * n
# y_loc = [0] * n
# for i in range(n):
#     x_loc[i], y_loc[i] = map(int, input().split())
#
# ans = n   # worst case
#
# for i in range(n):
#     for j in range(n):
#         x_div = x_loc[i] + 1   # vertical fence (even)
#         y_div = y_loc[j] + 1   # horizontal fence (even)
#
#         upper_left = upper_right = lower_left = lower_right = 0
#
#         for k in range(n):
#             if x_loc[k] < x_div and y_loc[k] < y_div:
#                 lower_left += 1
#             if x_loc[k] < x_div and y_loc[k] > y_div:
#                 upper_left += 1
#             if x_loc[k] > x_div and y_loc[k] < y_div:
#                 lower_right += 1
#             if x_loc[k] > x_div and y_loc[k] > y_div:
#                 upper_right += 1
#
#         worst_region = max(upper_left, upper_right, lower_left, lower_right)
#         if worst_region < ans:
#             ans = worst_region
#
# print(ans)
