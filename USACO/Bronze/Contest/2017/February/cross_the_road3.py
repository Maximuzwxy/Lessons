"""
USACO 2017 February Contest, Bronze - Problem 3: Why Did the Cow Cross the Road III
===================================================================================
Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=713

Tags: Simulation, Sorting, Greedy

Difficulty: very_easy

Problem Description:
-------------------
N cows (N ≤ 100) queue up at a single gate to enter FJ's farm. Each cow has an
arrival time and a questioning duration (both positive integers ≤ 1,000,000).
Only one cow can be questioned at a time — if multiple cows arrive close
together, they wait in line and are processed one by one.

Example: cow A arrives at time 5 with duration 7 → finishes at 12.
Cow B arrives at time 8 → must wait until 12, then adds 3 → finishes at 15.

Find the earliest possible time by which all cows have finished processing.

Input:  Line 1: N
        Next N lines: arrival_time questioning_duration
Output: A single integer — the minimum time when all cows are done.

Sample Input:              Sample Output:
3                          15
2 1
8 3
5 7

Explanation:
Cow 1 (arrive 2, duration 1): processed 2→3.
Gate idle until cow 3 arrives at 5: processed 5→12.
Cow 2 arrives at 8, waits until 12: processed 12→15.
All done at time 15.

====================================================================
Solution 1: Sort + Greedy Simulation (User's Solution)
====================================================================
Sort cows by arrival time, then process them in order. Track `end` — the time
when the current cow finishes questioning. For each cow:
  - If it arrives after `end`, start immediately at arrival time.
  - Otherwise, it waits and starts when the previous cow finishes.

Time Complexity: O(N log N) (dominated by sorting)
"""

import sys

sys.stdin = open('cowqueue.in', 'r')
sys.stdout = open('cowqueue.out', 'w')

n = int(input())
q = []

for i in range(n):
    q.append(list(map(int, input().split())))
q.sort()                              # sort by arrival time

end = 0

for arrive, question in q:
    if arrive > end:                  # gate is idle → start at arrival
        end = arrive + question
    else:                             # gate is busy → wait, then process
        end += question

print(end)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Same idea but does NOT sort. Instead, repeatedly scans for the earliest
# unprocessed cow (linear search each iteration), simulating the queue.
# This is more Java-style — no sorting needed but O(N^2).
#
# Comparison with Solution 1:
#   - Solution 1 sorts upfront (O(N log N)), then a single O(N) pass
#   - Solution 2 does N linear scans (O(N^2)), no sorting needed
#   - Solution 1 is more Pythonic and efficient; both are fine for N ≤ 100
#
# Time Complexity: O(N^2)
#
# import sys
#
# sys.stdin = open('cowqueue.in', 'r')
# sys.stdout = open('cowqueue.out', 'w')
#
# n = int(input())
# enter = [0] * n
# duration = [0] * n
# processed = [False] * n
#
# for i in range(n):
#     enter[i], duration[i] = map(int, input().split())
#
# nextAvailableTime = 0
#
# for _ in range(n):
#     # Find the earliest unprocessed cow
#     nextToEnter = -1
#     for i in range(n):
#         if not processed[i] and (nextToEnter == -1 or enter[i] < enter[nextToEnter]):
#             nextToEnter = i
#
#     # Process that cow
#     processed[nextToEnter] = True
#     if enter[nextToEnter] > nextAvailableTime:
#         nextAvailableTime = enter[nextToEnter] + duration[nextToEnter]
#     else:
#         nextAvailableTime += duration[nextToEnter]
#
# print(nextAvailableTime)
