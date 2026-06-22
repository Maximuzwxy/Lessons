"""
USACO 2015 December Contest, Bronze - Problem 3: Contaminated Milk
====================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=569

Tags: Brute Force, Simulation, Set Operations

Problem Description:
-------------------
N people (1 ≤ N ≤ 50) attend a milk-tasting party with M types of milk
(1 ≤ M ≤ 50). Exactly one type of milk has gone bad, but Farmer John
doesn't know which one. Anyone who drinks the bad milk will get sick.

Given:
  - D records (1 ≤ D ≤ 1000) of (person p, milk m, time t) — who drank what when
  - S records (1 ≤ S ≤ N) of (person p, time t) — who got sick and when

A person only gets sick from drinking bad milk at a strictly earlier time.
Figure out: among all milk types that could possibly be bad, what is the
maximum number of people who would need medicine?

Sample Input:              Sample Output:
3 4 7 2                    3
1 1 1
1 4 1
1 3 4
1 2 2
3 1 3
2 1 5
2 2 7
1 3
2 8

Explanation:
  Milk 1: Both sick people drank it before getting sick → could be bad.
          Person 3 also drank it → 3 total would need medicine.
  Milk 2: Both sick people drank it before → could be bad. Only 2 total.
  Milk 3: Person 1 drank it at time 4 but got sick at time 3 → cannot be bad.
  Milk 4: Person 2 never drank it → cannot be bad.
  Worst case = 3 (if milk 1 is bad).


====================================================================
Solution 1: Set Intersection — Filter + Count (User's Solution)
====================================================================
Step 1: For each sick person, find the set of milk types they drank BEFORE
        they got sick. These are the "candidate bad milks" for that person.

Step 2: Take the INTERSECTION of all sick people's candidate sets. Only
        milk types common to ALL sick people could possibly be the bad one.

Step 3: For each candidate bad milk, count how many distinct people drank
        it (including those who didn't get sick yet). Take the maximum.

This is a clean, Pythonic approach using set operations instead of nested
boolean checks.

Time Complexity: O(D * S + D * M) ≈ O(1000 * 50) — easily passes Bronze.
"""

import sys
sys.stdin = open('badmilk.in', 'r')
sys.stdout = open('badmilk.out', 'w')

n, m, d, s = map(int, input().split())
drink = []   # list of [person, milk, time]
sick = []    # list of [person, sick_time]

for _ in range(d):
    drink.append(list(map(int, input().split())))

for _ in range(s):
    sick.append(list(map(int, input().split())))

# Step 1: For each sick person, collect milks they drank BEFORE getting sick
candidate_sets = []

for p in sick:
    bad = set()
    for d in drink:
        if p[0] == d[0] and d[2] < p[1]:  # same person, drank BEFORE sick time
            bad.add(d[1])
    candidate_sets.append(bad)

# Step 2: Take intersection — only milks that ALL sick people drank before
bad_milk = set(candidate_sets[0])
for b in candidate_sets:
    bad_milk &= b          # &= is set intersection

# Step 3: For each candidate bad milk, count distinct people who drank it
max_doses = set()

for i in bad_milk:
    for d in drink:
        if d[1] == i:                    # this record is about candidate milk i
            max_doses.add(d[0])          # add the person to the set

# The answer is the count of distinct people (worst-case scenario)
print(len(max_doses))


# =====================================================================
# Solution 2: Official USACO Solution (by Nick Wu) — Python Translation
# =====================================================================
# The official approach iterates over each milk type (1..M) and checks:
#   1. Is this milk type possibly bad?
#      → It is IF every sick person drank this milk BEFORE getting sick.
#   2. If yes, count how many distinct people ever drank this milk.
#   3. Keep the maximum count across all candidate milk types.
#
# This is equivalent to the set intersection approach above, but uses
# explicit boolean checks instead of Python sets. Both are O(M * (D + S)).
#
# Time Complexity: O(M * (D + S))

# import sys
# sys.stdin = open('badmilk.in', 'r')
# sys.stdout = open('badmilk.out', 'w')
#
# n, m, d, s = map(int, input().split())
#
# # Read all drinking records
# person_drink = [0] * d
# milk_drink = [0] * d
# time_drink = [0] * d
# for i in range(d):
#     p, mk, t = map(int, input().split())
#     person_drink[i] = p
#     milk_drink[i] = mk
#     time_drink[i] = t
#
# # Read all sick records
# person_sick = [0] * s
# time_sick = [0] * s
# for i in range(s):
#     p, t = map(int, input().split())
#     person_sick[i] = p
#     time_sick[i] = t
#
# max_can_get_sick = 0
#
# for milk_type in range(1, m + 1):
#     # Check if this milk type can possibly be bad
#     can_be_bad = True
#     for i in range(s):
#         # Does person_sick[i] drink milk_type before time_sick[i]?
#         drank_before = False
#         for j in range(d):
#             if (person_drink[j] == person_sick[i]
#                 and milk_drink[j] == milk_type
#                 and time_drink[j] < time_sick[i]):
#                 drank_before = True
#                 break
#         if not drank_before:
#             can_be_bad = False
#             break
#
#     if can_be_bad:
#         # Count distinct people who drank this milk type
#         drank = [False] * (n + 1)
#         for j in range(d):
#             if milk_drink[j] == milk_type:
#                 drank[person_drink[j]] = True
#         num_drank = sum(drank)
#         if num_drank > max_can_get_sick:
#             max_can_get_sick = num_drank
#
# print(max_can_get_sick)
