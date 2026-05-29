# =============================================================================
# USACO 2017 US Open Contest, Bronze
# Problem 2. Bovine Genomics
# https://usaco.org/index.php?page=viewproblem2&cpid=736
# =============================================================================

"""
【Problem Description】
- There are N "spotty" cows and N "plain" cows, each with a genome string of length M
- Genome consists of only 4 characters: A, C, G, T
- Find the number of positions (columns) where NO spotty cow shares the same
  character with ANY plain cow
- These positions are called "interesting" positions

【Input】
- First line: N (number of cows per breed), M (genome length)
- Next N lines: genome strings of spotty cows
- Next N lines: genome strings of plain cows
- 1 ≤ N, M ≤ 100

【Output】
- Number of "interesting" positions

【Example】
Input:
3 8
AATCCCAT
GATTGCAA
GGTCGCAA
ACTCCCAG
ACTCGCAT
ACTTCCAT
Output:
1

【Solution】
For each position i, check if any plain cow shares a character with spotty cows
- Build a set of all spotty characters at position i
- Check each plain cow's character at position i against the set
- If no plain cow's character is in the set, position i is "interesting"

Time: O(N × M)     Space: O(1) - set size is bounded by 4 (A,C,G,T)
"""

import sys
sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')

n, m = map(int, input().split())
spotty = []
plain = []
num = 0

# Read spotty cow genomes
for _ in range(n):
    spotty.append(list(input()))

# Read plain cow genomes
for _ in range(n):
    plain.append(list(input()))

# Check each position independently
for i in range(m):
    gen = set()  # Set of spotty characters at position i
    flag = True  # Assume position i is "interesting" until proven otherwise

    # Collect all spotty cow characters at position i
    for j in range(n):
        gen.add(spotty[j][i])

    # Check if any plain cow has the same character at position i
    for k in range(n):
        if plain[k][i] in gen:
            flag = False  # Not interesting if there's a match
            break

    if flag:
        num += 1

print(num)