# =============================================================================
# USACO 2019 December Contest, Bronze
# Problem 1. Cow Gymnastics
# https://usaco.org/index.php?page=viewproblem2&cpid=963
# =============================================================================

"""
【Problem Description】
- There are K practice sessions, each with N cows ranked from 1 to N
- For each session, we know the ranking order of all N cows
- Find the number of ordered pairs (i, j) such that:
  "i is ahead of j" is TRUE in ALL K sessions

【Input】
- First line: K (number of sessions), N (number of cows)
- Next K lines: ranking order of N cows for each session
- 1 ≤ K ≤ 10, 1 ≤ N ≤ 100

【Output】
- Number of ordered pairs (i, j) that satisfy the condition in all sessions

【Example】
Input:  3 4   (3 sessions, 4 cows)
        1 2 3 4
        2 1 3 4
        1 2 4 3
Output: 2      (pairs: (1,3) and (1,4))

【Solution 1 - Brute Force】
- Generate all possible ordered pairs (i, j) using permutations
- Check if each pair appears in all K sessions
- Time: O(N² × K)      Space: O(N²)
"""

# Solution 1
import sys
from itertools import permutations
from itertools import combinations
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
sessions = []
for _ in range(k):
    sessions.append(list(map(int, input().split())))

# Generate all possible ordered pairs (i, j) where i != j
# e.g., for n=4: (1,2), (1,3), (1,4), (2,1), (2,3), ...
per = list(permutations([i for i in range(1, n + 1)], 2))
pairs = []
num = 0

# For each session, compute all unordered pairs (a, b) where a appears before b
# e.g., [1,2,3,4] -> [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
for s in sessions:
    pairs.append(list(combinations(s, 2)))

# For each possible ordered pair (i, j), check if it holds in ALL sessions
# A pair (i, j) holds in a session if (i, j) appears in that session's combinations
for c in per:
    flag = True
    for p in pairs:
        if c not in p:  # If this pair doesn't appear in current session, it fails
            flag = False
            break
    if flag:
        num += 1

print(num)

# =============================================================================
"""
【Solution 2 - Optimized】

Key Insight: If a pair (i, j) never appears as (i before j) in the FIRST session,
it cannot satisfy the condition in all sessions.

Therefore, we only need to check pairs that appear in the first session,
instead of all N×(N-1) possible pairs.

Time: O(N² × K) but with smaller constant (only checks ~N²/2 pairs)
Space: O(N²)
"""

# Solution 2
import sys
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')
from itertools import combinations

k, n = map(int, input().split())
sessions = []
for _ in range(k):
    sessions.append(list(map(int, input().split())))

pairs = []
num = 0

# Extract all pairs from each session
for s in sessions:
    pairs.append(list(combinations(s, 2)))

# Only check pairs that appear in the FIRST session
# If (i, j) wasn't in the right order in session 1, it can't be consistent
for c in pairs[0]:
    ret = True
    for p in pairs:
        if c not in p:  # If current session doesn't have this pair, skip
            ret = False
            break
    if ret:
        num += 1
print(num)