"""
USACO 2017 January Contest, Bronze - Problem 1: Don't Be Last!
=================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=687

Tags: Simulation, Sorting

Problem Description:
-------------------
FJ owns 7 cows: Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, Henrietta.
Each day he records milk amounts per cow. Any cow not in the log produces 0.

Given N log entries (N ≤ 100, each cow + amount ≤ 100), find the cow with the
second-smallest total milk production. More precisely: let M be the minimum
total; output the cow whose total is minimal among all totals > M. If multiple
cows tie for this, or all cows produce exactly M, output "Tie".

Sample Input:              Sample Output:
10                         Henrietta
Bessie 1
Maggie 13
Elsie 3
Elsie 4
Henrietta 4
Gertie 12
Daisy 7
Annabelle 10
Bessie 6
Henrietta 5

Explanation:
  Totals: Bessie=7, Elsie=7, Daisy=7 → all tie for minimum (7).
  Henrietta=9 is the second-smallest → output Henrietta.


====================================================================
Solution 1: Dict + Counter + Set (User's Solution)
====================================================================
1. Initialize a dict with all 7 cow names mapped to 0.
2. Read N entries, accumulate milk per cow in the dict.
3. Extract values to a list; find min and max.
4. If min == max, all cows have the same total → "Tie".
5. Otherwise: get unique sorted values, take the second smallest.
6. Use Counter to check frequency of the second smallest value:
   - If freq > 1 → "Tie"
   - If freq == 1 → find and print the cow name.

Leverages Python's Counter and set to avoid manual frequency counting.

Time Complexity: O(N + 7) ≈ O(N), Space Complexity: O(1) (7 cows fixed).
"""

import sys
from collections import Counter

sys.stdin = open('notlast.in', 'r')
sys.stdout = open('notlast.out', 'w')

# All 7 cows initialized to 0 (absent from log = 0 milk)
d = {
    'Bessie': 0,
    'Elsie': 0,
    'Daisy': 0,
    'Gertie': 0,
    'Annabelle': 0,
    'Maggie': 0,
    'Henrietta': 0
}

l = []

n = int(input())
for i in range(n):
    name, amount = input().split()
    d[name] += int(amount)               # accumulate milk per cow

# Gather all milk totals
for k, v in d.items():
    l.append(v)

min_v = min(l)
max_v = max(l)

c = Counter(l)                           # frequencies of each milk total

if min_v == max_v:
    print('Tie')                         # all cows produce the same amount
else:
    # Unique sorted values → second element is second smallest
    ll = sorted(list(set(l)))
    r = ll[1]                            # second smallest distinct value
    if c[r] > 1:
        print('Tie')                     # multiple cows share second place
    elif c[r] == 1:
        for k, v in d.items():           # find the cow with this total
            if v == r:
                print(k)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# Uses parallel arrays (names list + milk amount array) instead of a dict.
# A helper function findCowIndex() does linear search to map names to indices.
#
# Finding second minimum:
#   1. Scan once for the global minimum.
#   2. Scan again for the smallest value strictly > minimum = second minimum.
#   3. Scan a third time to count how many cows have the second minimum.
#      If exactly 1 → print name; else → "Tie".
#
# More verbose (Java-style) but same O(1) time for 7 cows.

# import sys
# sys.stdin = open('notlast.in', 'r')
# sys.stdout = open('notlast.out', 'w')
#
# cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
# amount = [0] * len(cows)
#
# n = int(input())
# for _ in range(n):
#     name, milk = input().split()
#     milk = int(milk)
#     # Linear search to find cow index
#     for j in range(len(cows)):
#         if cows[j] == name:
#             amount[j] += milk
#             break
#
# # Find minimum milk amount
# min_amount = min(amount)
#
# # Find second smallest (smallest value strictly greater than min)
# second_amount = 10**7
# for v in amount:
#     if v > min_amount and v < second_amount:
#         second_amount = v
#
# # Count how many cows have the second smallest amount
# index_of_second = -1    # -1 = not found yet
# for j in range(len(amount)):
#     if amount[j] == second_amount:
#         if index_of_second == -1:
#             index_of_second = j
#         else:
#             index_of_second = -2   # tie detected
#
# if index_of_second >= 0:
#     print(cows[index_of_second])
# else:
#     print("Tie")
