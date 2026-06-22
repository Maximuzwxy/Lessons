# =============================================================================
# USACO 2021 January Contest, Bronze
# Problem 2. Even More Odd Photos
# https://usaco.org/index.php?page=viewproblem2&cpid=1084
# =============================================================================

"""
【Problem Description】
- There are N cows, each with an integer breed ID (1 ≤ ID ≤ 100)
- Farmer John wants to group the cows to maximize the number of groups
- Rules:
  - Each group has ≥ 1 cow
  - The sum of breed IDs in each group alternates: even, odd, even, odd, ...
  - The first group's sum must be even

- Find the maximum possible number of groups

【Input】
- First line: N (number of cows)
- Second line: N integers (breed IDs)

【Output】
- Maximum possible number of groups

【Example 1】
Input:  7
        1 3 5 7 9 11 13
Output: 3
(All cows are odd; group as: [1,3]→4(even), [5,7,9]→21(odd), [11,13]→24(even))

【Example 2】
Input:  7
        11 2 17 13 1 15 3
Output: 5

【Solution 1 - Simulation (commented out)】
Simulate the actual process of combining numbers:
- Separate cows into even and odd lists
- If we have too many odds, combine them into groups:
  - Two odds → one even (combined into a tuple)
  - Three odds → one odd (three into a tuple)
- If too many evens, combine with an odd: even + odd → one odd
- Repeat until counts are balanced (odd == even or odd == even + 1)
- The final result is the number of groups (= len(even) + len(odd))

This approach uses tuples to represent combined groups,
e.g., (3, 5) means "the group formed by cows 3 and 5".

Time: O(N)   Space: O(N)

【Solution 2 - Mathematical (Optimal)】
Key Insight: We only need to know the counts of evens and odds, not their values.
- Let E = number of even cows, O = number of odd cows

Pattern: the groups alternate E, O, E, O, ... (E = even sum group, O = odd sum group)

Case 1: E ≥ O → pattern is E, O, E, O, ..., E
  Answer = 2 × O + 1

Case 2: O > E → we need to convert excess odds:
  - Two odds combine into an even: O -= 2, E += 1
  - Three odds combine into an odd: O -= 3, O += 1 → net O -= 2
  - In both cases, each conversion reduces total groups by 1 but adds 1 useful
    (since two groups of 2 odds each = 2 even-sum groups in the final pattern)

  Let diff = O - E.
  diff % 3 == 0: answer = 2E + 2(diff/3)     (all excess converted as triples or pairs)
  diff % 3 == 1: answer = 2E + 2(diff/3) - 1  (one leftover pair needed)
  diff % 3 == 2: answer = 2E + 2(diff/3) + 1  (one extra group possible)

Time: O(N)   Space: O(1)
"""

# =============================================================================
# Solution 1 - Simulation using Tuples
# (Comment out Solution 2 and uncomment this to use it)
# =============================================================================
# n = int(input())
# origin = list(map(int, input().split()))
# even = []
# odd = []
#
# # Separate cows into even and odd groups
# for num in origin:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#
# # Repeatedly combine groups until balanced
# # Target: len(odd) == len(even) or len(odd) == len(even) + 1
# while True:
#     e = len(even)
#     o = len(odd)
#     if e == o or e == o + 1:
#         break   # Already balanced
#
#     # Too many odds: need to reduce them
#     if o > e:
#         if o - e > 1:
#             # Combine 2 odds → 1 even tuple: (odd1, odd2)
#             # This creates one new even-sum group, reducing odd count by 2
#             even.append((odd.pop(), odd.pop()))
#         else:
#             # Combine 3 odds → 1 odd tuple: (odd1, odd2, odd3)
#             # Three odds sum to odd, so it's still an odd-sum group (net: -2 odds)
#             odd.append((odd.pop(), odd.pop(), odd.pop()))
#
#     # Too many evens: combine even + odd → odd tuple
#     if e > o + 1:
#         # One even + one odd → odd (odd number of groups, net: evens -1)
#         odd.append((even.pop(), odd.pop()))
#
# print(len(even) + len(odd))

# =============================================================================
# Solution 2 - Mathematical / Greedy (Optimal)
# =============================================================================
n = int(input())
origin = list(map(int, input().split()))

odd = even = 0

# Count evens and odds from the input
for num in origin:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Case 1: enough evens to alternate E, O, E, O, ..., E
if even == odd:
    print(odd * 2)
elif even > odd:
    print(odd * 2 + 1)
else:
    # Case 2: more odds than evens, need to convert excess odds
    diff = odd - even
    x = 0

    if diff % 3 == 1:
        x = -1   # One leftover odd cannot form a valid group
    elif diff % 3 == 2:
        x = 1   # Can squeeze in one more group with the remainder

    # Base: 2*even groups from alternating, plus converted excess odds
    t = even * 2 + (diff // 3) * 2 + x
    print(t)