# =============================================================================
# USACO 2022 December Contest, Bronze
# Problem 1. Cow College
# https://usaco.org/index.php?page=viewproblem2&cpid=1251
# =============================================================================

"""
【Problem Description】
- There are N cows, cow i is willing to pay at most c_i tuition
- Farmer John sets a tuition T for all cows
- Only cows with c_i ≥ T will attend
- Revenue = T × (number of cows with c_i ≥ T)
- Find the maximum revenue and the tuition T that achieves it
- If multiple T give the same revenue, choose the smallest T

【Input】
- First line: N (1 ≤ N ≤ 10^5)
- Second line: N integers c_1, ..., c_N (1 ≤ c_i ≤ 10^6)

【Output】
- Maximum revenue and optimal tuition T

【Example】
Input:
4
1 6 4 6
Output:
12 4

Explanation: If T = 4, then 3 cows attend (costs 6, 4, 6), revenue = 3 × 4 = 12

【Solution 1 - Brute Force with Counter (Timeout)】
- Use Counter to count frequency of each tuition value
- For each possible tuition k, calculate total revenue
- Time: O(N²) - too slow for large N

【Solution 2 - Array Indexing (Timeout)】
- Use array to count frequency of each tuition value
- Iterate through all possible tuition values
- Time: O(max_c_i) - still too slow for max_c_i up to 10^6

【Solution 3 - Greedy + Sorting (Optimal)】
Key Insight: After sorting, for any tuition value c_i, all cows at or above
that value will pay c_i.

Algorithm:
1. Sort the tuition costs
2. For each cow at index i (sorted order), consider c_i as tuition
3. Revenue = c_i × (N - i) cows will pay
4. Keep track of maximum revenue

Why this works:
- After sorting: c_1 ≤ c_2 ≤ ... ≤ c_N
- If we set tuition = c_i, cows i, i+1, ..., N will all pay c_i
- Number of paying cows = N - i
- Total revenue = c_i × (N - i)

Time: O(N log N)   Space: O(N)
"""

# =============================================================================
# Solution 1 - Brute Force with Counter (Timeout)
# Time: O(N²), Space: O(N)
# =============================================================================
# from collections import Counter
#
# n = int(input())
# cows = Counter(map(int, input().split()))
#
# max_t = tuition = 0
# cur = 0
#
# for k, v in cows.items():
#     cur = k
#     total = 0
#     for key, value in cows.items():
#         if key >= k:
#             total += k * value
#     if total > max_t:
#         max_t = total
#         tuition = k
#     elif total == max_t:
#         tuition = min(tuition, k)
#
# print(max_t, tuition)

# =============================================================================
# Solution 2 - Array Indexing (Timeout)
# Time: O(max_c_i), Space: O(max_c_i)
# =============================================================================
# n = int(input())
# max_cow = 1000001
# cows = [0] * max_cow
# origin = list(map(int, input().split()))
#
# for i in origin:
#     cows[i] += 1
#
# max_t = tuition = 0
# past = 0
# for j in range(max_cow):
#     total = 0
#     if cows[j] != 0:
#         total = (n - past) * j
#         past += cows[j]
#
#     if total > max_t:
#         max_t = total
#         tuition = j
#     elif total == max_t:
#         tuition = min(tuition, j)
#
# print(max_t, tuition)

# =============================================================================
# Solution 3 - Greedy + Sorting (Optimal)
# Time: O(N log N), Space: O(N)
# =============================================================================
n = int(input())
cows = list(map(int, input().split()))
cows.sort()

max_pay = tuition = 0

# Try each cow's cost as the tuition price
for i in range(n):
    # Revenue if we set tuition = cows[i]
    # All cows from i to N-1 (i.e., N-i cows) will pay
    total = cows[i] * (n - i)

    if total > max_pay:
        max_pay = total
        tuition = cows[i]

print(max_pay, tuition)