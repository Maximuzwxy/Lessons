# =============================================================================
# USACO 2020 December Contest, Bronze
# Problem 2. Daisy Chains
# https://usaco.org/index.php?page=viewproblem2&cpid=1060
# =============================================================================

"""
【Problem Description】
- There are N flowers in a row, flower i has p_i petals
- For every pair (i, j) where 1 ≤ i ≤ j ≤ N, Bessie takes a photo of flowers i to j
- A photo has an "average flower" if there exists a flower whose petal count equals
  the average of all flowers in that photo
- Count how many photos have an average flower

【Input】
- First line: N (1 ≤ N ≤ 100)
- Second line: N integers p_1 ... p_N (1 ≤ p_i ≤ 1000)

【Output】
- Number of photos that have an average flower

【Example】
Input:
4
1 1 2 3
Output:
6

Explanation:
- 4 single-flower photos (each has average = its own value)
- Range (1,2): [1,1] has average = 1 (exists in range)
- Range (2,4): [1,2,3] has average = 2 (exists in range)

【Solution - Brute Force】
For each possible range [i, j], check if it has an average flower:
- Calculate sum of the range
- If sum % length == 0, the average is an integer
- Check if that average value exists in the range

Time: O(N^3)   Space: O(N)
- There are O(N^2) ranges
- Each range check takes O(N) to sum + O(N) to search
- With N ≤ 100, this is fast enough
"""

n = int(input())
p = list(map(int, input().split()))

num = 0

# Enumerate all possible ranges [i, j]
for i in range(n):
    for j in range(i, n):
        # Extract the subarray from i to j (inclusive)
        flowers = p[i:j + 1]

        # Calculate average: if sum % length == 0, average is integer
        if sum(flowers) % (j - i + 1) == 0:
            average = sum(flowers) // (j - i + 1)
            # Check if average value exists in the range
            if average in flowers:
                num += 1

print(num)