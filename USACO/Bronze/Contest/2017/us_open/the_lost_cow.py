"""
USACO 2017 US Open Contest, Bronze - Problem 1: The Lost Cow
=============================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=735

Tags: Simulation, Math

Difficulty: very_easy

Problem Description:
-------------------
FJ is at position x on a number line. Bessie is at position y (unknown to FJ).
It's dark, so FJ must search using a zig-zag strategy:

  x → x+1 → x-2 → x+4 → x-8 → ...

Each step moves twice as far from his starting position x as the previous
step, alternating directions. Compute the total distance FJ travels until
he reaches Bessie.

Input:  Two space-separated integers x and y (0 ≤ x, y ≤ 1000, x ≠ y).
Output: The total distance traveled.

Sample Input:              Sample Output:
3 6                        9

Explanation:
Step 1: 3 → 4 (dist 1), Bessie not found
Step 2: 4 → 1 (dist 3), Bessie not found
Step 3: 1 → 7 (dist 6), passes Bessie at 6 along the way → adds 6-1=5
Total: 1 + 3 + 5 = 9

====================================================================
Solution 1: Step-by-Step Position Simulation (User's Solution)
====================================================================
Simulate each zig-zag step explicitly. Track `cur_pos` and compute the
next target position as `x ± 2^times`. For each step, check whether
Bessie's position y lies between cur_pos and next_pos. If yes, add the
remaining distance to y and break. Otherwise, add the full segment
distance, update cur_pos, flip direction, and continue.

Time Complexity: O(log |x-y|) — the step size doubles each time.
"""

import sys

sys.stdin = open('lostcow.in', 'r')
sys.stdout = open('lostcow.out', 'w')

x, y = map(int, input().split())

flag = True           # True = moving right, False = moving left
distance = 0
times = 0             # exponent for step size: 2^times
offset = 0
cur_pos = x

while True:
    if flag:
        offset = 2 ** times
    else:
        offset = -2 ** times

    next_pos = x + offset          # target position for this step

    if x < y:                      # Bessie is to the right
        if next_pos < y:           # haven't reached Bessie yet
            distance += abs(cur_pos - next_pos)
            flag = not flag
            cur_pos = next_pos
            times += 1
        else:                      # Bessie is in this segment
            distance += abs(y - cur_pos)
            break
    else:                          # Bessie is to the left
        if next_pos > y:           # haven't reached Bessie yet
            distance += abs(cur_pos - next_pos)
            flag = not flag
            cur_pos = next_pos
            times += 1
        else:                      # Bessie is in this segment
            distance += abs(y - cur_pos)
            break

print(distance)


# =====================================================================
# Solution 2: Official USACO Solution (by Jonathan Paulson) — Python Translation
# =====================================================================
# Key insight: don't track current position at all. Each full "go out and
# back" round trip costs exactly 2 * step_size (there and back to start).
# The final segment where Bessie is found costs just abs(y - x).
#
# At each iteration:
#   - If Bessie lies in the current segment, add abs(y - x) and finish.
#   - Otherwise, add by * 2 (full round trip), double step size, flip direction.
#
# Comparison with Solution 1:
#   - Solution 1: tracks cur_pos explicitly, computes partial distances
#   - Solution 2: never tracks position — just adds round-trip costs and
#                 one final direct distance. Simpler, more mathematical.
#   - Both O(log |x-y|), but Solution 2 is cleaner.
#
# Time Complexity: O(log |x-y|)
#
# import sys
#
# sys.stdin = open('lostcow.in', 'r')
# sys.stdout = open('lostcow.out', 'w')
#
# x, y = map(int, input().split())
#
# ans = 0
# by = 1          # current step size
# dir = 1         # 1 = right, -1 = left
#
# while True:
#     # Check if Bessie is within the current segment
#     if (dir == 1 and x <= y <= x + by) or (dir == -1 and x - by <= y <= x):
#         ans += abs(y - x)    # found Bessie — add remaining direct distance
#         print(ans)
#         break
#     else:
#         ans += by * 2        # full round trip: go by units and back
#         by *= 2              # double step size
#         dir *= -1            # flip direction
