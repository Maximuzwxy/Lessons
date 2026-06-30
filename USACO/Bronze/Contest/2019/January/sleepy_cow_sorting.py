"""
USACO 2019 January Contest, Bronze - Problem 2. Sleepy Cow Sorting
===================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=892

Tags: Sorting, Ad Hoc

Difficulty: easy

Problem Description:
-------------------
N cows (1 ≤ N ≤ 100) are in a line in some order p1..pN. The only cow that
pays attention is the one facing FJ (the first in line). In one step, FJ can
tell this cow to move k paces backward (1 ≤ k ≤ N-1), inserting herself after
the k cows she passes.

Goal: find the minimum number of steps to sort the cows into 1,2,...,N.

Observation (official): If k steps suffice, then the last N-k cows must
already be in sorted order relative to each other. Conversely, if the last
N-k cows are already sorted, k steps suffice. So the answer is simply the
number of cows NOT in the sorted suffix — or equivalently, the index (0-based)
where the sorted suffix begins.

Sample Input:       Sample Output:
4                   3
1 2 4 3

Explanation:
Original: [1, 2, 4, 3]. Sorted suffix from the right = just [3] (since 4 > 3).
3 cows before it → answer = 3.

Step 1: cow 1 moves to between 3 and 4 → [2, 4, 1, 3]
Step 2: cow 2 moves between 1 and 3 → [4, 1, 2, 3]
Step 3: cow 4 moves after 3 → [1, 2, 3, 4]

====================================================================
Solution 1: Simulate the Sorting Process
====================================================================
Find the sorted part from the right end (longest suffix in increasing order).
Repeatedly take the first cow, insert her into the sorted suffix at the
correct position, and count how many operations until fully sorted.

This works correctly, but the simulation is unnecessary — the answer is just
the index returned by sorted_part() on the FIRST call. See Solution 2.

Time Complexity: O(N²) — N iterations × O(N log N) sorting per iteration,
but only because we sort the suffix each time. N ≤ 100 so it's fine.
"""

import sys

sys.stdin = open('sleepy.in', 'r')
sys.stdout = open('sleepy.out', 'w')

n = int(input())
line = list(map(int, input().split()))


def sorted_part(l):
    """
    Find the starting index of the longest sorted suffix.
    Scan from right to left: as long as each element < the next, keep going.
    Returns the index where the sorted suffix begins.
    """
    idx = n - 1
    for i in range(n - 1, 0, -1):
        if line[i - 1] < line[i]:
            idx = i - 1      # keep extending left
        else:
            break             # order broken → stop
    return idx


cnt = 0

# Repeatedly: find sorted suffix, move first cow into it
while line != sorted(line):
    index = sorted_part(line)          # start of sorted suffix
    part = line[index:]                # the sorted suffix part

    cur = line[0]                      # the first cow (facing FJ)
    part.append(cur)                   # insert her into sorted part
    part.sort()                        # re-sort the suffix

    line = line[1:index] + part        # rebuild: skip first cow + sorted suffix
    cnt += 1

print(cnt)


# =====================================================================
# Solution 2: Official USACO Solution — Just Find Longest Sorted Suffix
# =====================================================================
# Key insight: the minimum steps = the number of cows BEFORE the sorted suffix.
# No simulation needed. Just scan from right to left and return the index of
# the first element in the sorted suffix.
#
# A cow moves at most once (when she's at the front), so each step adds one
# more cow to the sorted suffix. After k steps, all k previously-unsorted
# cows are placed correctly. The answer is purely the length of the unsorted
# prefix.
#
# Time Complexity: O(N) — single pass from right to left.
#
# Key differences from Solution 1:
# - Solution 1: finds sorted_part + simulates the full process in a loop
# - Solution 2: finds sorted_part once and returns it — the simulation is
#   redundant because each iteration just decreases the answer by 1 anyway.
#   Essentially, sorted_part() directly IS the answer.
#
# import sys
# sys.stdin = open('sleepy.in', 'r')
# sys.stdout = open('sleepy.out', 'w')
#
# n = int(input())
# a = list(map(int, input().split()))
#
# ans = n - 1
# for i in range(n - 2, -1, -1):
#     if a[i] < a[i + 1]:
#         ans = i
#     else:
#         break
#
# print(ans)
