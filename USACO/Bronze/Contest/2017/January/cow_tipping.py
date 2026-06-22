# USACO 2017 January Contest, Bronze
# Problem 3. Cow Tipping
# https://usaco.org/index.php?page=viewproblem2&cpid=689

import sys
sys.stdin = open('cowtip.in', 'r')
sys.stdout = open('cowtip.out', 'w')

n = int(input())
cows = []

for i in range(n):
    cows.append(list(map(int, list(input()))))

def toggle(a, b):
    for x in range(a):
        for y in range(b):
            if cows[x][y] == 0:
                cows[x][y] = 1
            else:
                cows[x][y] = 0

cnt = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if cows[i][j] == 1:
            toggle(i + 1, j + 1)
            cnt += 1

print(cnt)

