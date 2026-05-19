# USACO 2017 US Open Contest, Bronze
# Problem 2. Bovine Genomics
# https://usaco.org/index.php?page=viewproblem2&cpid=736

import sys
# sys.stdin = open('cownomics.in', 'r')
# sys.stdout = open('cownomics.out', 'w')

n, m = map(int, input().split())
spotty = []
plain = []
num = 0

for _ in range(n):
    spotty.append(list(input()))

for _ in range(n):
    plain.append(list(input()))

for i in range(m):
    gen = set()
    flag = True
    for j in range(n):
        gen.add(spotty[j][i])
    for k in range(n):
        if plain[k][i] in gen:
            flag = False
            break
    if flag:
        num += 1

print(num)





