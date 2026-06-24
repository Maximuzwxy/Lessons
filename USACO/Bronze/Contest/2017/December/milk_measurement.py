"""
USACO 2017 December Contest, Bronze - Problem 3: Milk Measurement
==================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=761

Tags: Simulation

Difficulty: normal

Problem Description:
-------------------
FJ owns 3 cows: Bessie, Elsie, and Mildred. Each starts at 7 gallons/day.
He takes N periodic measurements (N ≤ 100) over 100 days, each recording a
day, cow name, and change (+/- a nonzero integer). Measurements may be out
of chronological order. At most one measurement per day.

FJ displays the picture(s) of whichever cow(s) currently have the highest
milk output (ties → all tied cows displayed). Count how many times the
displayed picture(s) must change over the 100 days.

Input:  Line 1: N
        Next N lines: day cow_name change  (day 1..100, change nonzero)
Output: A single integer — number of display changes.

Sample Input:              Sample Output:
4                          3
7 Mildred +3
4 Elsie -1
9 Mildred -1
1 Bessie +2

Explanation:
  Day 1: Bessie +2 → 9, sole leader → change (1)
  Day 4: Elsie -1 → 6, Bessie still sole leader → no change
  Day 7: Mildred +3 → 10, new sole leader → change (2)
  Day 9: Mildred -1 → 9, ties Bessie → leader set changes → change (3)
  Total changes = 3.

====================================================================
Solution 1: Sort + Set Comparison (User's Solution)
====================================================================
Sort measurements by day, then process only days with measurements.
Maintain a dict of milk amounts and a `photo` set of current leaders.
After each measurement:
  1. Update the cow's milk amount.
  2. Compute the new set of cows with max milk.
  3. If the set differs from `photo` → display changed, increment count.
This avoids iterating over all 100 days — only processes relevant days.

Time Complexity: O(N log N) (dominated by sorting).
"""

import sys

sys.stdin = open('measurement.in', 'r')
sys.stdout = open('measurement.out', 'w')

n = int(input())
m = []
for i in range(n):
    day, name, change = input().split()
    m.append([int(day), name, int(change)])

m.sort(key=lambda x: x[0])                  # sort by day

photo = {'Bessie', 'Elsie', 'Mildred'}      # initially all tied at 7
d = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}

cnt = 0

for day, name, change in m:
    d[name] += change                        # update milk amount

    max_v = max(d['Bessie'], d['Elsie'], d['Mildred'])

    ph = set()                              # compute new leader set
    for k, v in d.items():
        if v == max_v:
            ph.add(k)

    if photo != ph:                          # display changed
        cnt += 1
        photo = ph

print(cnt)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Does NOT sort. Instead iterates days 1..100 and scans all notes to find
# any changes on that day. Uses boolean flags (bessieOn, elsieOn, mildredOn)
# to track which cows were on the display "yesterday". After applying any
# changes for the current day, compares old flags with new flags.
#
# Time Complexity: O(100 × N) = O(N) with constant 100.
#
# import sys
#
# sys.stdin = open('measurement.in', 'r')
# sys.stdout = open('measurement.out', 'w')
#
# n = int(input())
# day = [0] * n
# cow = [""] * n
# change = [0] * n
# for i in range(n):
#     d_str, c, ch = input().split()
#     day[i] = int(d_str)
#     cow[i] = c
#     change[i] = int(ch)
#
# bessieMilk = elsieMilk = mildredMilk = 7
# bessieOn = elsieOn = mildredOn = True       # day 0: all tied
# dayAdjust = 0
#
# for currDay in range(1, 101):
#     for i in range(n):
#         if day[i] == currDay:
#             if cow[i] == "Bessie":
#                 bessieMilk += change[i]
#             elif cow[i] == "Elsie":
#                 elsieMilk += change[i]
#             elif cow[i] == "Mildred":
#                 mildredMilk += change[i]
#
#     highestMilk = max(bessieMilk, elsieMilk, mildredMilk)
#     bessieOnNext = bessieMilk == highestMilk
#     elsieOnNext = elsieMilk == highestMilk
#     mildredOnNext = mildredMilk == highestMilk
#
#     if (bessieOn != bessieOnNext or
#             elsieOn != elsieOnNext or
#             mildredOn != mildredOnNext):
#         dayAdjust += 1
#
#     bessieOn = bessieOnNext
#     elsieOn = elsieOnNext
#     mildredOn = mildredOnNext
#
# print(dayAdjust)


# =====================================================================
# Solution 3: Official USACO Solution (by Brian Dean) — Python Translation
# =====================================================================
# Precomputes cumulative milk rates day-by-day using a 2D array:
#   rates[c][d] = milk for cow c on day d (after applying changes up to d).
# Then iterates days 1..100, comparing is_highest(c, d-1) vs is_highest(c, d).
#
# Comparison:
#   - Solution 1: sorts and only processes days with actual measurements.
#                 Uses a set for leaders, very Pythonic and efficient.
#   - Solution 2: loops all 100 days, scans all notes on each day. Simple
#                 but does unnecessary work on measurement-free days.
#   - Solution 3: precomputes full 3×101 rate table, then one linear scan.
#                 Elegant but memory-heavy for larger problems.
#   - Solution 1 is the most natural approach: sort, simulate, compare sets.
#
# Time Complexity: O(N log N) for Solution 1, O(100 × N) for Solution 2,
#                  O(3 × 100 + N) for Solution 3.
#
# import sys
#
# sys.stdin = open('measurement.in', 'r')
# sys.stdout = open('measurement.out', 'w')
#
# n = int(input())
# changes = [[0] * 101 for _ in range(3)]    # 0=Bessie, 1=Elsie, 2=Mildred
# rates = [[0] * 101 for _ in range(3)]
#
# for _ in range(n):
#     d, name, x = input().split()
#     d = int(d); x = int(x)
#     if name == "Bessie":   c = 0
#     elif name == "Elsie":  c = 1
#     else:                  c = 2
#     changes[c][d] = x
#
# # Cumulative rates: day 0 = initial 7
# for c in range(3):
#     rates[c][0] = 7
#     for d in range(1, 101):
#         rates[c][d] = rates[c][d-1] + changes[c][d]
#
#
# def is_highest(c, d):
#     highest = max(rates[0][d], rates[1][d], rates[2][d])
#     return rates[c][d] == highest
#
#
# num_changes = 0
# for d in range(1, 101):
#     if (is_highest(0, d-1) != is_highest(0, d) or
#             is_highest(1, d-1) != is_highest(1, d) or
#             is_highest(2, d-1) != is_highest(2, d)):
#         num_changes += 1
#
# print(num_changes)
