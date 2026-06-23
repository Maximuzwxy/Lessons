"""
USACO 2016 January Contest, Bronze - Problem 1: Promotion Counting
====================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=591

Tags: Ad Hoc, Mathematics

Difficulty: very_easy

Problem Description:
-------------------
USACO has four divisions: bronze, silver, gold, platinum. All new participants
start in bronze; scoring perfectly on a contest promotes a participant to the
next-higher division (multiple promotions within one contest are possible).

Given the number of participants in each division before and after a contest,
determine how many were promoted:
  - from bronze to silver
  - from silver to gold
  - from gold to platinum

Constraints: Each count is between 0 and 1,000,000.

Sample Input:              Sample Output:
1 2                        1
1 1                        1
1 1                        1
1 2

Explanation:
  Before: 1 in each division. After: 2 in bronze, 2 in platinum.
  One possible scenario: 2 new participants joined; one promoted all the way
  to platinum, the other stayed in bronze.
  Promotions: 1 bronze→silver, 1 silver→gold, 1 gold→platinum.


====================================================================
Solution 1: New-Participant Accounting (User's Solution)
====================================================================
Track new participants who joined the contest, then compute how many
participants must have left each division (i.e., were promoted).

  1. new_participants = total_after - total_before
  2. b→s: bronze participants who left = bronze_before - (bronze_after - new)
     (new participants start in bronze, so bronze_after includes them)
  3. s→g: silver participants who left = silver_before - (silver_after - b→s)
     (accounts for those promoted from bronze into silver)
  4. g→p: gold participants who left = gold_before - (gold_after - s→g)

Time Complexity: O(1)
"""

import sys
# sys.stdin = open('promote.in', 'r')
# sys.stdout = open('promote.out', 'w')

# Read before/after counts for each division
bronze = list(map(int, input().split()))   # [bronze_before, bronze_after]
silver = list(map(int, input().split()))   # [silver_before, silver_after]
gold = list(map(int, input().split()))     # [gold_before, gold_after]
platinum = list(map(int, input().split())) # [platinum_before, platinum_after]

# Total new participants who joined during the contest
new_participants = (bronze[1] + silver[1] + gold[1] + platinum[1]
                    - bronze[0] - silver[0] - gold[0] - platinum[0])

# How many left each division (promoted to the next)
# New participants start in bronze, so bronze_after includes them
b_s = bronze[0] - (bronze[1] - new_participants)   # bronze → silver
s_g = silver[0] - (silver[1] - b_s)                # silver → gold
g_p = gold[0] - (gold[1] - s_g)                     # gold → platinum

print(b_s)
print(s_g)
print(g_p)


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# A simpler cumulative approach: the number promoted from one division
# equals the change in the count of participants at or above that level.
#
#   gold→platinum = after_platinum - before_platinum
#   silver→gold   = (after_gold+platinum) - (before_gold+platinum)
#   bronze→silver = (after_silver+gold+platinum) - (before_silver+gold+platinum)
#
# Time Complexity: O(1)

# import sys
# sys.stdin = open('promote.in', 'r')
# sys.stdout = open('promote.out', 'w')
#
# bronze_before, bronze_after = map(int, input().split())
# silver_before, silver_after = map(int, input().split())
# gold_before, gold_after = map(int, input().split())
# platinum_before, platinum_after = map(int, input().split())
#
# gold_to_platinum = platinum_after - platinum_before
# silver_to_gold = (gold_after + platinum_after) - (gold_before + platinum_before)
# bronze_to_silver = (silver_after + gold_after + platinum_after) - (silver_before + gold_before + platinum_before)
#
# print(bronze_to_silver)
# print(silver_to_gold)
# print(gold_to_platinum)
